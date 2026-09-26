# Visualização de dados

## 1. Conceito

A visualização de dados utiliza representações gráficas para facilitar a identificação e comunicação de padrões, distribuições e relações presentes nos dados.

Python possui bibliotecas como Matplotlib e Seaborn para criação de gráficos.

## 2. Matplotlib e Seaborn

Importações comuns:

```python
import matplotlib.pyplot as plt
import seaborn as sns
```

Matplotlib fornece recursos gerais para criação e personalização de gráficos. Seaborn oferece funções de alto nível voltadas especialmente para visualização estatística.

## 3. Histograma

Histogramas são úteis para observar a distribuição de uma variável numérica.

```python
sns.histplot(data=df, x="idade")
plt.show()
```

Pode ajudar a identificar concentração de valores, assimetria e possíveis padrões na distribuição.

## 4. Gráfico de barras

Gráficos de barras são apropriados para comparar valores entre categorias.

```python
sns.countplot(data=df, x="categoria")
plt.show()
```

Também podem ser utilizados para representar valores agregados por grupo.

## 5. Boxplot

Boxplots permitem visualizar mediana, quartis e possíveis valores extremos.

```python
sns.boxplot(data=df, x="categoria", y="valor")
plt.show()
```

São úteis para comparar a distribuição de uma variável numérica entre grupos.

## 6. Gráfico de dispersão

Scatterplots ajudam a visualizar a relação entre duas variáveis numéricas.

```python
sns.scatterplot(data=df, x="idade", y="renda")
plt.show()
```

Podem revelar tendências, agrupamentos e possíveis valores extremos.

## 7. Heatmap de correlação

Uma matriz de correlação pode ser visualizada por meio de um heatmap:

```python
corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True)
plt.show()
```

O gráfico facilita a identificação visual de associações entre variáveis numéricas.

## 8. Escolha do gráfico

A escolha depende da pergunta que se deseja responder:

| Objetivo | Visualização |
|---|---|
| Observar distribuição | Histograma |
| Comparar categorias | Barras |
| Comparar distribuições | Boxplot |
| Observar relação entre duas variáveis numéricas | Dispersão |
| Observar várias correlações | Heatmap |

## 9. Cuidados

Uma visualização pode induzir interpretações equivocadas quando possui escalas inadequadas, excesso de elementos ou representação desproporcional.

Recomenda-se:

- utilizar títulos e rótulos claros;
- escolher escalas coerentes;
- evitar informações desnecessárias;
- considerar o tipo das variáveis;
- interpretar o gráfico em conjunto com o contexto dos dados.

Uma associação visual não demonstra necessariamente causalidade.
