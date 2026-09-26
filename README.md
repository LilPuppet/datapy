# DataPy Assistant

Assistente virtual que responde dúvidas de quem está aprendendo **análise de
dados com Python** (Python básico, Pandas, pré-processamento, análise
exploratória, visualização de dados e machine learning) — sempre com base
numa base de conhecimento própria, citando a fonte, e admitindo quando não
sabe algo em vez de inventar.

Projeto feito para o desafio **"Construa Seu Assistente Virtual Com
Inteligência Artificial"** (DIO Lab — Bia do Futuro), adaptado para o tema
de assistente de estudos em Python para dados.

![Arquitetura do DataPy Assistant](assets/arquitetura.svg)

## Estrutura do repositório

```
datapy-assistant/
├── README.md                      # este arquivo
├── assets/                        # imagens e diagramas usados na documentação
│   ├── README.md                  # o que colocar aqui (e como referenciar)
│   └── arquitetura.svg            # diagrama do fluxo pergunta → busca → resposta
├── data/                          # base de conhecimento (fonte da verdade)
│   ├── python_basico.md
│   ├── pandas.md
│   ├── pre_processamento.md
│   ├── analise_exploratoria.md
│   ├── visualizacao.md
│   └── machine_learning.md
├── docs/
│   ├── documentacao.md            # passo 1: o que o agente faz, para quem, como se comporta
│   ├── prompts.md                 # passo 3: prompts/instruções do agente
│   ├── perguntas.md               # roteiro de testes (24 perguntas)
│   ├── respostas_teste.md         # respostas reais geradas nos testes
│   ├── resultados.md              # passo 5: avaliação e métricas preenchidas
│   └── pitch.md                   # passo 6: pitch final do projeto
└── src/
    └── app.py                     # passo 4: aplicação funcional (CLI)
```

Cada pasta tem uma responsabilidade clara:

- **`assets/`** — só material visual (diagramas, prints de tela). Nada aqui
  afeta o funcionamento do assistente; é puramente para ilustrar o README e
  o pitch.
- **`data/`** — a base de conhecimento em si. É a "fonte da verdade": se
  você quiser ensinar o assistente sobre um novo assunto, é aqui que entra
  um novo arquivo `.md`.
- **`docs/`** — tudo que é texto/explicação sobre o projeto (não código):
  documentação do agente, prompts, testes e resultados, pitch.
- **`src/`** — o código da aplicação. Se o projeto crescesse, novos módulos
  Python (ex.: uma interface web) entrariam aqui.

## Como rodar

Requer apenas Python 3.10+ (sem dependências externas no modo padrão).

```bash
# Chat interativo no terminal
python src/app.py

# Uma pergunta só
python src/app.py "O que é overfitting?"
```

Saia do chat digitando `sair`.

### Modo opcional com Claude (LLM)

Se quiser respostas reescritas de forma mais natural por um modelo de
linguagem (em vez do modo extrativo padrão), defina a variável de ambiente
`ANTHROPIC_API_KEY` antes de rodar. Sem essa variável, o assistente
funciona 100% offline.

```bash
export ANTHROPIC_API_KEY="sua-chave-aqui"
python src/app.py
```

## Os 6 passos do desafio

| Etapa | Onde está |
|---|---|
| 1. Documentação | [`docs/documentacao.md`](docs/documentacao.md) |
| 2. Base de conhecimento | [`data/`](data/) |
| 3. Prompts | [`docs/prompts.md`](docs/prompts.md) |
| 4. Aplicação funcional | [`src/app.py`](src/app.py) |
| 5. Avaliação e métricas | [`docs/resultados.md`](docs/resultados.md) (baseado nos testes em [`docs/perguntas.md`](docs/perguntas.md) e nas respostas reais em [`docs/respostas_teste.md`](docs/respostas_teste.md)) |
| 6. Pitch | [`docs/pitch.md`](docs/pitch.md) |

## Resultado da avaliação (resumo)

- **183/192 pontos (~95%)** nos critérios de correção, relevância, clareza
  e aderência à base, em 24 perguntas de teste.
- **100%** de acerto ao reconhecer perguntas fora do escopo do assistente.
- **0** respostas com informação tecnicamente incorreta.
- Limitações reais de recuperação de informação foram encontradas e
  documentadas com transparência — ver a seção "Observações" em
  [`docs/resultados.md`](docs/resultados.md).

## Como funciona por dentro

1. A base de conhecimento (`data/*.md`) é dividida em seções (por
   cabeçalho `##`).
2. Cada pergunta é comparada com essas seções usando uma busca por
   relevância (TF-IDF simplificado, com stemming leve e frequência
   sublinear, implementada sem dependências externas).
3. Se a melhor seção encontrada tiver pontuação de relevância acima de um
   limiar mínimo, o assistente monta a resposta a partir dela — sempre
   citando a fonte.
4. Se não houver informação suficiente, o assistente diz isso claramente
   em vez de arriscar uma resposta ruim ou inventada.
5. Opcionalmente, com uma chave de API da Anthropic configurada, o mesmo
   trecho recuperado é usado como contexto para o Claude reescrever a
   resposta de forma mais natural, seguindo as mesmas regras (ver
   [`docs/prompts.md`](docs/prompts.md)).
