# Avaliação do DataPy Assistant

Testes executados em: 26/09/2026, rodando `python src/app.py` (modo offline,
sem chave de API) contra as 24 perguntas de `perguntas.md`. As respostas
completas geradas nesse teste estão em `docs/respostas_teste.md`.

## Critérios

Cada resposta foi avaliada com quatro critérios, pontuação de 0 a 2:

- **Correção:** a resposta apresenta informações tecnicamente corretas?
- **Relevância:** a resposta responde diretamente à pergunta?
- **Clareza:** a explicação é compreensível para o público-alvo?
- **Aderência à base:** a resposta está de acordo com as informações disponíveis na base de conhecimento?

Pontuação máxima por pergunta: 8 pontos.

## Tabela de resultados

| ID | Correção | Relevância | Clareza | Aderência | Total | Observações |
|---|---:|---:|---:|---:|---:|---|
| Q01 | 2 | 2 | 2 | 2 | 8 | Recuperou exatamente a seção "Funções", com o exemplo `calcular_media`. |
| Q02 | 2 | 2 | 2 | 2 | 8 | Resposta direta com `df.isna().sum()`. |
| Q03 | 2 | 1 | 1 | 2 | 6 | Trouxe "Condicionais" (Python básico) antes de "Filtragem" (Pandas) por sobreposição de palavras ("idade", "maior", "18"); a resposta certa está lá, mas misturada com conteúdo menos relevante. |
| Q04 | 2 | 2 | 2 | 2 | 8 | `groupby()` explicado com exemplo. |
| Q05 | 2 | 2 | 2 | 2 | 8 | Explica que não existe estratégia universal e mostra alternativas (dropna/fillna). |
| Q06 | 2 | 2 | 2 | 2 | 8 | One-Hot Encoding com `pd.get_dummies`. |
| Q07 | 2 | 2 | 2 | 2 | 8 | Contraste direto entre média e mediana, incluindo sensibilidade a outliers. |
| Q08 | 2 | 2 | 2 | 2 | 8 | Deixa claro que correlação não implica causalidade. |
| Q09 | 2 | 2 | 2 | 2 | 8 | Tabela de escolha de gráfico + histograma. |
| Q10 | 2 | 2 | 2 | 2 | 8 | Explica boxplot para outliers dentro do trecho de "Valores extremos". |
| Q11 | 2 | 2 | 2 | 2 | 8 | Regressão vs. classificação com exemplos de cada uma. |
| Q12 | 2 | 2 | 1 | 2 | 7 | Resposta correta (separação treino/teste), mas o trecho de "Vazamento de dados" aparece antes do trecho mais direto, deixando a resposta um pouco menos objetiva. |
| Q13 | 2 | 2 | 2 | 2 | 8 | Definição direta de overfitting. |
| Q14 | 2 | 2 | 2 | 2 | 8 | Definição de data leakage (levemente redundante por vir de dois arquivos, mas consistente). |
| Q15 | 2 | 2 | 2 | 2 | 8 | Clustering + K-Means + contexto de aprendizado não supervisionado. |
| Q16 | 1 | 0 | 1 | 2 | 4 | **Falha de recuperação:** a seção ideal ("Escalonamento", com `StandardScaler`) não entrou no top-3 retornado; o assistente respondeu com trechos sobre gráfico de dispersão e boas práticas gerais, que não respondem à pergunta sobre escala de variáveis. Nenhuma informação incorreta foi dita, mas a resposta não resolve a dúvida. |
| Q17 | 2 | 2 | 2 | 2 | 8 | Indica que duplicatas devem ser verificadas antes de remover automaticamente. |
| Q18 | 2 | 2 | 2 | 2 | 8 | Mesma resposta robusta de Q08, correlação ≠ causalidade. |
| Q19 | 2 | 1 | 1 | 2 | 6 | Recuperou "Boxplot" (correto) mas incluiu também "Funções" (Python básico), sem relação com a pergunta, por sobreposição lexical fraca. |
| Q20 | 2 | 2 | 2 | 2 | 8 | Combina overfitting + separação treino/teste + boas práticas — resposta completa. |
| Q21 | 2 | 2 | 2 | 2 | 8 | Reconheceu corretamente que está fora do escopo (infraestrutura de servidores). |
| Q22 | 2 | 2 | 2 | 2 | 8 | Reconheceu corretamente que está fora do escopo (desenvolvimento mobile). |
| Q23 | 2 | 2 | 2 | 2 | 8 | Reconheceu corretamente que está fora do escopo (finanças pessoais). |
| Q24 | 2 | 2 | 2 | 2 | 8 | Reconheceu corretamente que está fora do escopo (infraestrutura de banco de dados/cloud). |

**Total: 183 / 192 pontos (≈ 95,3%)**

## Observações

- **Respostas consideradas adequadas (nota ≥ 6/8):** 23 de 24 (95,8%).
- **Respostas com informações tecnicamente incorretas:** 0. Em nenhum teste
  o assistente afirmou algo que contradiga a base de conhecimento — os
  problemas encontrados foram de **relevância/foco**, não de correção.
- **Perguntas em que o agente reconheceu corretamente estar fora de
  escopo:** 4 de 4 (Q21–Q24, 100%). O limiar de pontuação mínima
  (`SCORE_THRESHOLD`) se mostrou eficaz para evitar respostas inventadas
  sobre servidores Linux, apps Android, investimentos e bancos de dados na
  nuvem — em todos os casos o assistente admitiu não ter informação
  suficiente em vez de arriscar um palpite.
- **Principais erros encontrados:**
  1. *Sobreposição lexical entre domínios* (Q03, Q19): perguntas de Pandas/
     Visualização às vezes recuperam trechos de Python básico só porque
     compartilham palavras genéricas ("idade", exemplos de código com
     `print`/`def`). O conteúdo correto aparece na resposta, mas nem sempre
     em primeiro lugar.
  2. *Falha de recuperação em pergunta de raciocínio aplicado* (Q16): a
     pergunta sobre escalonamento de variáveis não usa a palavra
     "escalonamento" nem "StandardScaler" diretamente, então o mecanismo de
     busca por palavras-chave não conseguiu conectar a pergunta ao trecho
     certo com prioridade suficiente.
  3. *Redundância moderada* (Q12, Q14): quando dois arquivos da base tratam
     do mesmo conceito (ex.: data leakage aparece em `machine_learning.md`
     e `pre_processamento.md`), a resposta às vezes repete a mesma ideia
     duas vezes.
- **Alterações realizadas na base/no agente após a avaliação:**
  1. A base de conhecimento (`pandas.md`, `pre_processamento.md`,
     `python_basico.md`) tinha problemas de escaping do Markdown original
     (barras invertidas antes de `#`, `[`, `]`, `_`; entidades `&#x20;`; e um
     trecho de `pandas.md` que havia perdido aspas/dois-pontos no exemplo de
     dicionário). Isso foi corrigido antes de indexar a base — sem essa
     limpeza, os blocos de código ficavam ilegíveis e prejudicavam tanto a
     leitura humana quanto a recuperação por palavras-chave.
  2. O mecanismo de busca evoluiu de uma contagem simples de palavras para
     TF-IDF com stemming leve (agrupando variações como "calcula"/
     "calcular"/"calculado" ou "filtrar"/"filtragem"), frequência sublinear
     (para não deixar uma palavra repetida dominar o placar) e uma regra de
     "termos mínimos em comum" para evitar falsos positivos por uma única
     palavra genérica compartilhada — foi assim que as 4 perguntas fora de
     escopo passaram a ser corretamente recusadas.
  3. **Melhoria futura sugerida:** para corrigir o erro de Q16, uma próxima
     versão poderia usar busca semântica (embeddings) em vez de apenas
     correspondência de palavras, ou adicionar sinônimos/tags manuais a
     cada seção da base (ex.: marcar a seção de Escalonamento com palavras-
     chave como "escala", "renda", "diferença de grandeza").
