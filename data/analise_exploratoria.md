# Análise exploratória de dados

## 1. Conceito

A Análise Exploratória de Dados (EDA) é uma etapa destinada a compreender as características, distribuições e relações presentes em um conjunto de dados antes da aplicação de análises ou modelos.

O objetivo é identificar padrões, inconsistências, valores ausentes, possíveis valores extremos e relações entre variáveis.

## 2. Inspeção inicial

Algumas operações úteis com Pandas:

```python
df.head()
df.info()
df.shape
df.describe()
```

`head()` mostra as primeiras linhas, `info()` apresenta informações sobre colunas e tipos, `shape` informa dimensões e `describe()` fornece estatísticas descritivas para variáveis numéricas.

## 3. Estatísticas descritivas

Algumas medidas importantes são:

- média: valor médio das observações;
- mediana: valor central após ordenar os dados;
- mínimo e máximo: extremos observados;
- desvio padrão: medida de dispersão em torno da média;
- quartis: valores que dividem os dados em partes.

A média pode ser sensível a valores extremos, enquanto a mediana tende a ser mais robusta.

## 4. Distribuição

É importante observar como os valores de uma variável estão distribuídos.

Um histograma pode ajudar a identificar concentração de valores, assimetria e possíveis padrões.

## 5. Correlação

A correlação mede a associação entre duas variáveis numéricas.

No Pandas:

```python
df.corr(numeric_only=True)
```

Correlação não implica causalidade. Uma associação entre duas variáveis não demonstra que uma causa a outra.

## 6. Valores extremos

Valores extremos, ou outliers, são observações que se afastam consideravelmente do comportamento predominante dos dados.

Um boxplot pode auxiliar na identificação visual de possíveis valores extremos.

Um valor extremo não deve ser automaticamente removido. É necessário verificar se representa um erro, uma situação legítima ou uma característica importante da população.

## 7. Perguntas para orientar uma EDA

Durante uma análise exploratória, algumas perguntas úteis são:

- Quais são as variáveis disponíveis?
- Existem valores ausentes?
- Existem duplicatas?
- Como as variáveis estão distribuídas?
- Existem valores extremos?
- Quais variáveis apresentam associação?
- Existem diferenças entre grupos?
- Há padrões que merecem investigação?

## 8. Boas práticas

Uma EDA deve ser orientada por perguntas e pelo contexto do problema.

Recomenda-se:

- conhecer a origem e o significado das variáveis;
- verificar a qualidade dos dados;
- utilizar estatísticas e visualizações em conjunto;
- investigar resultados inesperados;
- não interpretar correlação como causalidade;
- registrar decisões e observações relevantes.
