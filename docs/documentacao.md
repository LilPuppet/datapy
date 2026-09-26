# Documentação do Agente — DataPy Assistant

## 1. O que é

O **DataPy Assistant** é um assistente virtual que responde dúvidas de quem
está aprendendo análise de dados com Python. Ele usa uma base de
conhecimento própria (arquivos `.md` em `data/`) para dar respostas
confiáveis, simples e sempre com a fonte citada — em vez de "inventar"
explicações como um chatbot genérico faria.

## 2. Para quem ele serve

- Estudantes de cursos de Python/Data Science que estão revisando conceitos.
- Pessoas em transição de carreira para dados, que precisam de um "colega"
  disponível a qualquer hora para tirar dúvidas rápidas.
- Quem está fazendo um projeto prático (ex.: uma EDA ou um modelo simples de
  ML) e quer confirmar um conceito ou lembrar a sintaxe de um comando.

Não é voltado para: especialistas buscando discussões avançadas, nem para
assuntos fora de Python/dados (o assistente reconhece esse limite e diz
isso claramente).

## 3. Escopo de conhecimento

O assistente só responde dentro destes seis temas (arquivos da base):

| Arquivo | Tema |
|---|---|
| `python_basico.md` | Variáveis, estruturas de dados, condicionais, laços, funções, tratamento de erros |
| `pandas.md` | DataFrames, seleção, filtragem, agrupamento, merge, valores ausentes/duplicados |
| `pre_processamento.md` | Valores ausentes, duplicatas, tipos, variáveis categóricas, escalonamento, vazamento de dados |
| `analise_exploratoria.md` | Estatísticas descritivas, distribuição, correlação, valores extremos |
| `visualizacao.md` | Histograma, gráfico de barras, boxplot, dispersão, heatmap |
| `machine_learning.md` | Aprendizado supervisionado/não supervisionado, regressão, classificação, clustering, overfitting, data leakage |

## 4. Como ele deve se comportar

1. **Responder apenas com base na sua base de conhecimento.** Se a
   informação não estiver lá, ele diz isso — nunca inventa.
2. **Reconhecer quando está fora do escopo** (ex.: infraestrutura de
   servidores, apps mobile, investimentos) e admitir a limitação em vez de
   tentar parecer que sabe de tudo.
3. **Ser simples e didático**, com exemplos de código quando fizer sentido.
4. **Nunca confundir correlação com causalidade**, nem recomendar remover
   automaticamente valores ausentes/duplicados/extremos sem contexto — a
   base de conhecimento é enfática nesse ponto, e o comportamento do
   assistente reflete isso.
5. **Sempre citar a fonte** usada para montar a resposta, para transparência.

O detalhamento completo dessas regras, em formato de prompt, está em
[`docs/prompts.md`](prompts.md).

## 5. Limitações conhecidas

- O motor de busca é baseado em palavras-chave (TF-IDF + stemming leve), não
  em compreensão semântica profunda. Isso significa que perguntas com
  vocabulário muito diferente do texto da base (ex.: "minha variável tem
  escalas muito diferentes" em vez de "como faço escalonamento") podem não
  encontrar o trecho ideal. Ver `docs/resultados.md` para exemplos reais
  encontrados na avaliação.
- A base de conhecimento é pequena (6 arquivos) e best-effort — é um
  protótipo, não uma base de conhecimento de produção.
- O assistente não substitui a leitura da documentação oficial de
  Pandas/Scikit-learn/Matplotlib para casos avançados.

## 6. Próximos passos possíveis

- Trocar a busca por palavras-chave por busca semântica (embeddings).
- Expandir a base de conhecimento com mais tópicos (ex.: séries temporais,
  deep learning básico).
- Adicionar uma interface web simples (Streamlit) sobre o mesmo motor de
  `src/app.py`.
