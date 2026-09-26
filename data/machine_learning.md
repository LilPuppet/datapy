# Introdução a Machine Learning

## 1. Conceito

Machine Learning, ou aprendizado de máquina, reúne técnicas que permitem a criação de modelos capazes de identificar padrões nos dados e realizar tarefas como previsão, classificação ou agrupamento.

## 2. Aprendizado supervisionado

No aprendizado supervisionado existe uma variável-alvo conhecida durante o treinamento.

Duas tarefas comuns são:

- regressão: previsão de valores numéricos;
- classificação: previsão de categorias.

Exemplo de regressão:

```text
Prever a nota de um estudante.
```

Exemplo de classificação:

```text
Classificar uma observação como pertencente à categoria A ou B.
```

## 3. Aprendizado não supervisionado

No aprendizado não supervisionado não existe necessariamente uma variável-alvo conhecida.

Uma tarefa comum é o clustering, utilizado para identificar grupos de observações com características semelhantes.

## 4. Variáveis preditoras e variável-alvo

Em um problema supervisionado, as variáveis utilizadas para realizar previsões são chamadas de variáveis preditoras ou atributos.

A variável que o modelo tenta prever é chamada de variável-alvo.

Exemplo:

```text
X = idade, renda, escolaridade
y = nota
```

Nesse caso, idade, renda e escolaridade são preditoras e nota é a variável-alvo.

## 5. Separação entre treinamento e teste

Uma prática comum é dividir os dados em conjuntos de treinamento e teste.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

O conjunto de treinamento é utilizado para ajustar o modelo, enquanto o conjunto de teste é utilizado para avaliar seu desempenho em dados que não foram utilizados no treinamento.

## 6. Regressão

Modelos de regressão são utilizados quando a variável-alvo é numérica.

A regressão linear é um exemplo:

```python
from sklearn.linear_model import LinearRegression

modelo = LinearRegression()
modelo.fit(X_train, y_train)
```

## 7. Classificação

Modelos de classificação são utilizados quando a variável-alvo representa categorias.

Exemplos de algoritmos incluem árvores de decisão, regressão logística e alguns métodos baseados em vizinhos.

## 8. Clustering

Clustering busca organizar observações em grupos de acordo com suas características.

O K-Means é um exemplo de algoritmo de clustering.

```python
from sklearn.cluster import KMeans

modelo = KMeans(n_clusters=3, random_state=42)
grupos = modelo.fit_predict(X)
```

O número de grupos deve ser escolhido considerando o problema e critérios de avaliação apropriados.

## 9. Métricas

A métrica utilizada deve ser compatível com a tarefa.

Em regressão, algumas métricas são:

- MAE;
- MSE;
- RMSE;
- R².

Em classificação, algumas métricas são:

- acurácia;
- precisão;
- recall;
- F1-score.

Uma única métrica nem sempre é suficiente para compreender o desempenho de um modelo.

## 10. Overfitting

Overfitting ocorre quando o modelo se ajusta excessivamente aos dados de treinamento e apresenta desempenho inferior em dados não utilizados durante o treinamento.

Uma forma de identificar o problema é comparar o desempenho do modelo em treinamento e teste.

## 11. Data leakage

Data leakage ocorre quando informações que não deveriam estar disponíveis no processo de treinamento acabam sendo utilizadas pelo modelo de maneira inadequada.

Isso pode produzir uma avaliação artificialmente otimista.

Transformações que aprendem parâmetros a partir dos dados devem ser ajustadas no conjunto de treinamento e depois aplicadas aos demais conjuntos.

## 12. Importância de atributos

Alguns modelos e técnicas permitem estimar a importância das variáveis para as previsões.

Essas medidas devem ser interpretadas de acordo com o método utilizado. Importância de atributo não significa necessariamente causalidade.

## 13. Boas práticas

Ao desenvolver um modelo:

- defina claramente o problema;
- conheça as variáveis;
- separe treinamento e teste adequadamente;
- evite vazamento de dados;
- escolha métricas coerentes com a tarefa;
- compare o desempenho em dados de treinamento e teste;
- documente as decisões;
- interprete os resultados considerando o contexto.
