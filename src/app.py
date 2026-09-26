"""
DataPy Assistant — Aplicação funcional
=======================================

Assistente virtual que responde dúvidas de Python/Pandas/EDA/Pré-processamento/
Machine Learning/Visualização de dados com base nos arquivos .md da pasta `data/`.

Modo de funcionamento
----------------------
Por padrão, o assistente roda 100% OFFLINE: ele indexa a base de conhecimento
localmente (sem nenhuma chamada de rede) e responde de forma extrativa, citando
sempre a fonte usada. Isso garante que ele nunca "invente" uma resposta — se a
base não tem informação suficiente, ele diz isso claramente.

Se a variável de ambiente ANTHROPIC_API_KEY estiver definida, o assistente usa
o trecho recuperado da base como contexto e pede a um modelo de linguagem
(Claude) para reescrever a resposta de forma mais natural — mas sempre restrito
ao conteúdo recuperado (ver prompts em docs/prompts.md).

Como usar
---------
    python src/app.py                # abre um chat interativo no terminal
    python src/app.py "sua pergunta" # responde uma única pergunta e encerra

Também pode ser importado como módulo:

    from app import DataPyAssistant
    assistant = DataPyAssistant()
    resposta = assistant.answer("O que é overfitting?")
"""

from __future__ import annotations

import math
import os
import re
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

# --------------------------------------------------------------------------- #
# Configuração
# --------------------------------------------------------------------------- #

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Pontuação mínima (0 a 1, aproximadamente) para considerar que a base tem
# informação suficiente para responder. Abaixo disso, o assistente admite
# que não sabe / está fora do escopo, em vez de arriscar uma resposta ruim.
SCORE_THRESHOLD = 0.12

TOP_K = 3  # número de trechos candidatos avaliados para montar a resposta

STOPWORDS = set(
    """
    a as o os um uma umas uns de do da dos das em no na nos nas por para com
    sem sob sobre e ou mas que se ao aos à às é são foi ser estar como isso
    esse essa esses essas este esta estes estas qual quais quando onde porque
    já não sim mais menos muito pouco entre até desde após antes também só
    seu sua seus suas meu minha meus minhas nosso nossa eu tu ele ela nós
    vós eles elas me te lhe nos vos lhes qualquer cada outro outra
    """.split()
)

SOURCE_LABELS = {
    "python_basico.md": "Python básico",
    "pandas.md": "Pandas",
    "pre_processamento.md": "Pré-processamento de dados",
    "analise_exploratoria.md": "Análise exploratória de dados (EDA)",
    "machine_learning.md": "Machine Learning",
    "visualizacao.md": "Visualização de dados",
}


# --------------------------------------------------------------------------- #
# Estruturas de dados
# --------------------------------------------------------------------------- #

@dataclass
class Chunk:
    source: str          # nome do arquivo de origem
    title: str           # título da seção (##)
    text: str            # conteúdo da seção
    tokens: Counter = field(default_factory=Counter)


def _fold_accents(word: str) -> str:
    """Remove acentos (ex.: 'média' -> 'media') para unificar grafias."""
    normalized = unicodedata.normalize("NFKD", word)
    return "".join(c for c in normalized if not unicodedata.combining(c))


def _stem(word: str) -> str:
    """Stemming bem simples: usa o radical (5 primeiros caracteres) da
    palavra sem acento, o que já é suficiente para aproximar variações como
    'calcula' / 'calcular' / 'calculado' ou 'filtrar' / 'filtragem' num corpus
    pequeno como este, sem depender de bibliotecas externas de NLP."""
    folded = _fold_accents(word)
    return folded[:6] if len(folded) > 6 else folded


def tokenize(text: str) -> List[str]:
    """Tokenização simples: minúsculas, separa identificadores de código
    (ex.: `calcular_media` -> `calcular` `media`), remove stopwords e aplica
    um stemming leve para aproximar variações morfológicas da mesma palavra.

    Propositalmente NÃO removemos os blocos de código: nomes de função/método
    (ex.: `fillna`, `groupby`, `boxplot`, `train_test_split`) carregam bastante
    sinal sobre o assunto do trecho e ajudam a recuperação a acertar perguntas
    do tipo "como faço X".
    """
    text = text.lower()
    text = text.replace("_", " ")
    text = re.sub(r"[^a-zà-ÿ0-9 ]", " ", text)
    words = [t for t in text.split() if t and t not in STOPWORDS and len(t) > 1]
    return [_stem(w) for w in words]


# --------------------------------------------------------------------------- #
# Indexação da base de conhecimento
# --------------------------------------------------------------------------- #

class KnowledgeBase:
    def __init__(self, data_dir: Path = DATA_DIR):
        self.data_dir = data_dir
        self.chunks: List[Chunk] = []
        self.idf: dict[str, float] = {}
        self._load()
        self._build_idf()

    def _load(self) -> None:
        for path in sorted(self.data_dir.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            # divide por cabeçalhos de nível 2 (##), mantendo o título junto
            sections = re.split(r"(?m)^##\s+", text)
            # a primeira parte (antes do primeiro ##) é a introdução/título do doc
            intro = sections[0]
            for section in sections[1:]:
                lines = section.split("\n", 1)
                title = lines[0].strip()
                body = lines[1] if len(lines) > 1 else ""
                full_text = f"## {title}\n{body}".strip()
                chunk = Chunk(source=path.name, title=title, text=full_text)
                chunk.tokens = Counter(tokenize(full_text))
                self.chunks.append(chunk)

    def _build_idf(self) -> None:
        n_docs = len(self.chunks)
        df: Counter = Counter()
        for chunk in self.chunks:
            for term in chunk.tokens:
                df[term] += 1
        self.idf = {
            term: math.log((n_docs + 1) / (freq + 1)) + 1
            for term, freq in df.items()
        }

    @staticmethod
    def _tf(freq: int) -> float:
        # frequência sublinear (1 + log(tf)): evita que uma única palavra
        # repetida muitas vezes num trecho (ex.: "variável" 7 vezes) domine o
        # placar sozinha em relação a trechos com mais termos distintos.
        return 1.0 + math.log(freq) if freq > 0 else 0.0

    def _score(self, query_tokens: Counter, chunk: Chunk) -> float:
        if not query_tokens or not chunk.tokens:
            return 0.0
        shared = set(query_tokens) & set(chunk.tokens)
        # Uma única palavra em comum costuma ser coincidência (ex.: "aplicação"
        # aparecendo em contextos completamente diferentes). Exigimos pelo
        # menos 2 termos de conteúdo em comum — a não ser que a própria
        # pergunta só tenha 1 termo de conteúdo (ex.: "O que é overfitting?").
        min_shared = min(2, len(query_tokens))
        if len(shared) < min_shared:
            return 0.0
        dot = 0.0
        for term, qfreq in query_tokens.items():
            if term in chunk.tokens:
                idf = self.idf.get(term, 1.0)
                dot += self._tf(qfreq) * self._tf(chunk.tokens[term]) * (idf ** 2)
        # normalização simples pelo tamanho dos vetores
        q_norm = math.sqrt(sum((self._tf(f) * self.idf.get(t, 1.0)) ** 2 for t, f in query_tokens.items())) or 1.0
        c_norm = math.sqrt(sum((self._tf(f) * self.idf.get(t, 1.0)) ** 2 for t, f in chunk.tokens.items())) or 1.0
        cosine = dot / (q_norm * c_norm)
        # fração dos termos da pergunta que foram encontrados no trecho:
        # ajuda a penalizar trechos que só compartilham termos genéricos
        coverage = len(shared) / len(query_tokens)
        return cosine * (0.5 + 0.5 * coverage)

    def search(self, query: str, top_k: int = TOP_K) -> List[tuple[Chunk, float]]:
        query_tokens = Counter(tokenize(query))
        scored = [(chunk, self._score(query_tokens, chunk)) for chunk in self.chunks]
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]


# --------------------------------------------------------------------------- #
# Assistente
# --------------------------------------------------------------------------- #

OUT_OF_SCOPE_MESSAGE = (
    "Não encontrei essa informação na minha base de conhecimento (Python básico, "
    "Pandas, Pré-processamento, Análise Exploratória, Visualização de Dados e "
    "Machine Learning). Posso ajudar melhor com dúvidas desses temas — "
    "consegue reformular sua pergunta dentro desse escopo?"
)

SYSTEM_PROMPT_PATH = BASE_DIR / "docs" / "prompts.md"


class DataPyAssistant:
    def __init__(self, use_llm: Optional[bool] = None):
        self.kb = KnowledgeBase()
        # decide automaticamente se usa LLM (Claude) para reescrever a resposta
        self.use_llm = use_llm if use_llm is not None else bool(os.environ.get("ANTHROPIC_API_KEY"))

    def answer(self, question: str) -> str:
        question = question.strip()
        if not question:
            return "Pode digitar sua pergunta sobre Python, Pandas, EDA, pré-processamento, ML ou visualização de dados?"

        results = self.kb.search(question, top_k=TOP_K)
        best_score = results[0][1] if results else 0.0

        if best_score < SCORE_THRESHOLD:
            return OUT_OF_SCOPE_MESSAGE

        # inclui outros trechos candidatos apenas se estiverem "próximos" do
        # melhor resultado — evita diluir a resposta com trechos pouco
        # relacionados só porque compartilham 1-2 palavras genéricas
        cutoff = max(SCORE_THRESHOLD * 0.6, best_score * 0.5)
        relevant = [(chunk, score) for chunk, score in results if score >= cutoff]

        if self.use_llm:
            try:
                return self._answer_with_llm(question, relevant)
            except Exception as exc:  # fallback silencioso para o modo offline
                print(f"[aviso] Falha ao chamar o modelo de linguagem ({exc}). Usando modo offline.", file=sys.stderr)

        return self._answer_extractive(question, relevant)

    # ---------------------------------------------------------------- #
    def _answer_extractive(self, question: str, relevant: List[tuple[Chunk, float]]) -> str:
        parts = []
        sources = []
        for chunk, _score in relevant:
            parts.append(chunk.text.strip())
            label = SOURCE_LABELS.get(chunk.source, chunk.source)
            if label not in sources:
                sources.append(label)

        body = "\n\n---\n\n".join(parts)
        fontes = ", ".join(sources)
        return f"{body}\n\n📚 Fonte: {fontes}"

    # ---------------------------------------------------------------- #
    def _answer_with_llm(self, question: str, relevant: List[tuple[Chunk, float]]) -> str:
        import json
        import urllib.request

        context = "\n\n---\n\n".join(chunk.text for chunk, _ in relevant)
        system_prompt = SYSTEM_PROMPT_PATH.read_text(encoding="utf-8") if SYSTEM_PROMPT_PATH.exists() else (
            "Você é o DataPy Assistant. Responda apenas com base no CONTEXTO fornecido, "
            "de forma simples e didática, em português. Se o contexto não for suficiente, diga isso."
        )
        user_content = f"CONTEXTO:\n{context}\n\nPERGUNTA DA PESSOA USUÁRIA:\n{question}"

        payload = {
            "model": "claude-sonnet-4-6",
            "max_tokens": 600,
            "system": system_prompt,
            "messages": [{"role": "user", "content": user_content}],
        }
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "x-api-key": os.environ["ANTHROPIC_API_KEY"],
                "anthropic-version": "2023-06-01",
            },
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
        return "".join(block.get("text", "") for block in data.get("content", []))


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def main() -> None:
    assistant = DataPyAssistant()

    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
        print(assistant.answer(question))
        return

    print("=" * 60)
    print(" DataPy Assistant — tire suas dúvidas de Python para dados")
    print(" (digite 'sair' para encerrar)")
    print("=" * 60)
    while True:
        try:
            question = input("\nVocê: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAté a próxima!")
            break
        if question.lower() in {"sair", "exit", "quit"}:
            print("Até a próxima!")
            break
        print(f"\nDataPy Assistant:\n{assistant.answer(question)}")


if __name__ == "__main__":
    main()
