### Q01
**Pergunta:** Como criar uma função em Python que calcula a média de uma lista?

**Resposta do assistente:**

## 5. Funções

Funções permitem organizar um conjunto de instruções que pode ser reutilizado.

```python
def calcular_media(notas):
    return sum(notas) / len(notas)
```

A função pode ser utilizada da seguinte forma:

```python
media = calcular_media([7, 8, 9])
```

📚 Fonte: Python básico

---

### Q02
**Pergunta:** Como verificar a quantidade de valores ausentes em cada coluna de um DataFrame?

**Resposta do assistente:**

## 2. Identificação de valores ausentes

Em Pandas:

```python
df.isna().sum()
```

Essa operação permite verificar a quantidade de valores ausentes em cada coluna.

📚 Fonte: Pré-processamento de dados

---

### Q03
**Pergunta:** Como filtrar um DataFrame para manter apenas registros cuja idade seja maior ou igual a 18 anos?

**Resposta do assistente:**

## 3. Condicionais

Estruturas condicionais permitem executar diferentes trechos de código dependendo de uma condição.

```python
idade = 20
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

---

## 3. Criação de um DataFrame

Um DataFrame pode ser criado a partir de um dicionário

```python
dados = {
    "nome": ["Ana", "João", "Maria"],
    "idade": [20, 25, 22]
}

df = pd.DataFrame(dados)
```

---

## 6. Filtragem

É possível selecionar linhas que atendam a uma condição

```python
df[df["idade"] >= 20]
```

Também é possível combinar condições

```python
df[(df["idade"] >= 20) & (df["idade"] <= 25)]
```

O operador `&` representa AND para condições entre Series.

📚 Fonte: Python básico, Pandas

---

### Q04
**Pergunta:** Para que serve o método groupby()?

**Resposta do assistente:**

## 10. Agrupamento

O método `groupby()` permite realizar operações agrupadas.

Exemplo

```python
df.groupby("cidade")["idade"].mean()
```

Esse código calcula a idade média para cada cidade.

📚 Fonte: Pandas

---

### Q05
**Pergunta:** Devo sempre remover todas as linhas que possuem valores ausentes?

**Resposta do assistente:**

## 8. Valores ausentes

Para verificar valores ausentes

```python
df.isna().sum()
```

Para remover linhas que possuem valores ausentes

```python
df.dropna()
```

Para preencher valores ausentes

```python
df["idade"].fillna(0)
```

A estratégia de tratamento deve considerar o significado da variável e o contexto da análise. Não existe uma estratégia universalmente correta para todos os conjuntos de dados.

---

## 9. Valores duplicados

Para identificar linhas duplicadas

```python
df.duplicated().sum()
```

Para remover duplicatas

```python
df.drop_duplicates()
```

📚 Fonte: Pandas

---

### Q06
**Pergunta:** O que é One-Hot Encoding e quando ele pode ser utilizado?

**Resposta do assistente:**

## 6. Variáveis categóricas

Variáveis categóricas representam grupos ou categorias.

Exemplo:

```text
sexo
------
Feminino
Masculino
Feminino
```

Algoritmos de aprendizado de máquina geralmente precisam que essas informações sejam representadas numericamente.

Uma técnica comum é o One-Hot Encoding.

Com Pandas:

```python
pd.get_dummies(df, columns=["sexo"])
```

O resultado cria colunas binárias para representar as categorias.

📚 Fonte: Pré-processamento de dados

---

### Q07
**Pergunta:** Qual é a diferença entre média e mediana?

**Resposta do assistente:**

## 3. Estatísticas descritivas

Algumas medidas importantes são:

- média: valor médio das observações;
- mediana: valor central após ordenar os dados;
- mínimo e máximo: extremos observados;
- desvio padrão: medida de dispersão em torno da média;
- quartis: valores que dividem os dados em partes.

A média pode ser sensível a valores extremos, enquanto a mediana tende a ser mais robusta.

📚 Fonte: Análise exploratória de dados (EDA)

---

### Q08
**Pergunta:** Correlação entre duas variáveis significa que uma causa a outra?

**Resposta do assistente:**

## 5. Correlação

A correlação mede a associação entre duas variáveis numéricas.

No Pandas:

```python
df.corr(numeric_only=True)
```

Correlação não implica causalidade. Uma associação entre duas variáveis não demonstra que uma causa a outra.

📚 Fonte: Análise exploratória de dados (EDA)

---

### Q09
**Pergunta:** Qual gráfico pode ser utilizado para observar a distribuição de uma variável numérica?

**Resposta do assistente:**

## 8. Escolha do gráfico

A escolha depende da pergunta que se deseja responder:

| Objetivo | Visualização |
|---|---|
| Observar distribuição | Histograma |
| Comparar categorias | Barras |
| Comparar distribuições | Boxplot |
| Observar relação entre duas variáveis numéricas | Dispersão |
| Observar várias correlações | Heatmap |

---

## 3. Histograma

Histogramas são úteis para observar a distribuição de uma variável numérica.

```python
sns.histplot(data=df, x="idade")
plt.show()
```

Pode ajudar a identificar concentração de valores, assimetria e possíveis padrões na distribuição.

---

## 4. Distribuição

É importante observar como os valores de uma variável estão distribuídos.

Um histograma pode ajudar a identificar concentração de valores, assimetria e possíveis padrões.

📚 Fonte: Visualização de dados, Análise exploratória de dados (EDA)

---

### Q10
**Pergunta:** Qual gráfico pode ajudar a identificar possíveis valores extremos?

**Resposta do assistente:**

## 4. Distribuição

É importante observar como os valores de uma variável estão distribuídos.

Um histograma pode ajudar a identificar concentração de valores, assimetria e possíveis padrões.

---

## 3. Histograma

Histogramas são úteis para observar a distribuição de uma variável numérica.

```python
sns.histplot(data=df, x="idade")
plt.show()
```

Pode ajudar a identificar concentração de valores, assimetria e possíveis padrões na distribuição.

---

## 6. Valores extremos

Valores extremos, ou outliers, são observações que se afastam consideravelmente do comportamento predominante dos dados.

Um boxplot pode auxiliar na identificação visual de possíveis valores extremos.

Um valor extremo não deve ser automaticamente removido. É necessário verificar se representa um erro, uma situação legítima ou uma característica importante da população.

📚 Fonte: Análise exploratória de dados (EDA), Visualização de dados

---

### Q11
**Pergunta:** Qual é a diferença entre regressão e classificação?

**Resposta do assistente:**

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

---

## 7. Classificação

Modelos de classificação são utilizados quando a variável-alvo representa categorias.

Exemplos de algoritmos incluem árvores de decisão, regressão logística e alguns métodos baseados em vizinhos.

---

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

📚 Fonte: Machine Learning

---

### Q12
**Pergunta:** Qual é a finalidade de separar os dados em treinamento e teste?

**Resposta do assistente:**

## 8. Vazamento de dados

Data leakage ocorre quando informações que não deveriam estar disponíveis durante o treinamento são utilizadas de maneira que forneça vantagem indevida ao modelo.

Uma prática importante é separar os dados de treinamento e teste antes de ajustar transformações que aprendem parâmetros a partir dos dados.

---

## 5. Separação entre treinamento e teste

Uma prática comum é dividir os dados em conjuntos de treinamento e teste.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

O conjunto de treinamento é utilizado para ajustar o modelo, enquanto o conjunto de teste é utilizado para avaliar seu desempenho em dados que não foram utilizados no treinamento.

---

## 10. Overfitting

Overfitting ocorre quando o modelo se ajusta excessivamente aos dados de treinamento e apresenta desempenho inferior em dados não utilizados durante o treinamento.

Uma forma de identificar o problema é comparar o desempenho do modelo em treinamento e teste.

📚 Fonte: Pré-processamento de dados, Machine Learning

---

### Q13
**Pergunta:** O que é overfitting?

**Resposta do assistente:**

## 10. Overfitting

Overfitting ocorre quando o modelo se ajusta excessivamente aos dados de treinamento e apresenta desempenho inferior em dados não utilizados durante o treinamento.

Uma forma de identificar o problema é comparar o desempenho do modelo em treinamento e teste.

📚 Fonte: Machine Learning

---

### Q14
**Pergunta:** O que é data leakage?

**Resposta do assistente:**

## 11. Data leakage

Data leakage ocorre quando informações que não deveriam estar disponíveis no processo de treinamento acabam sendo utilizadas pelo modelo de maneira inadequada.

Isso pode produzir uma avaliação artificialmente otimista.

Transformações que aprendem parâmetros a partir dos dados devem ser ajustadas no conjunto de treinamento e depois aplicadas aos demais conjuntos.

---

## 8. Vazamento de dados

Data leakage ocorre quando informações que não deveriam estar disponíveis durante o treinamento são utilizadas de maneira que forneça vantagem indevida ao modelo.

Uma prática importante é separar os dados de treinamento e teste antes de ajustar transformações que aprendem parâmetros a partir dos dados.

📚 Fonte: Machine Learning, Pré-processamento de dados

---

### Q15
**Pergunta:** O que é clustering?

**Resposta do assistente:**

## 8. Clustering

Clustering busca organizar observações em grupos de acordo com suas características.

O K-Means é um exemplo de algoritmo de clustering.

```python
from sklearn.cluster import KMeans

modelo = KMeans(n_clusters=3, random_state=42)
grupos = modelo.fit_predict(X)
```

O número de grupos deve ser escolhido considerando o problema e critérios de avaliação apropriados.

---

## 3. Aprendizado não supervisionado

No aprendizado não supervisionado não existe necessariamente uma variável-alvo conhecida.

Uma tarefa comum é o clustering, utilizado para identificar grupos de observações com características semelhantes.

📚 Fonte: Machine Learning

---

### Q16
**Pergunta:** Tenho uma variável de renda com valores muito diferentes de escala em relação às demais variáveis. O que devo considerar antes de treinar determinados modelos?

**Resposta do assistente:**

## 6. Gráfico de dispersão

Scatterplots ajudam a visualizar a relação entre duas variáveis numéricas.

```python
sns.scatterplot(data=df, x="idade", y="renda")
plt.show()
```

Podem revelar tendências, agrupamentos e possíveis valores extremos.

---

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

---

## 4. Variáveis preditoras e variável-alvo

Em um problema supervisionado, as variáveis utilizadas para realizar previsões são chamadas de variáveis preditoras ou atributos.

A variável que o modelo tenta prever é chamada de variável-alvo.

Exemplo:

```text
X = idade, renda, escolaridade
y = nota
```

Nesse caso, idade, renda e escolaridade são preditoras e nota é a variável-alvo.

📚 Fonte: Visualização de dados, Machine Learning

---

### Q17
**Pergunta:** Meu DataFrame possui muitas linhas duplicadas. Posso removê-las automaticamente?

**Resposta do assistente:**

## 9. Valores duplicados

Para identificar linhas duplicadas

```python
df.duplicated().sum()
```

Para remover duplicatas

```python
df.drop_duplicates()
```

---

## 4. Duplicatas

Duplicatas podem ser identificadas com:

```python
df.duplicated().sum()
```

E removidas com:

```python
df = df.drop_duplicates()
```

Antes de remover duplicatas, deve-se verificar se os registros realmente representam observações repetidas.

📚 Fonte: Pandas, Pré-processamento de dados

---

### Q18
**Pergunta:** Tenho duas variáveis numéricas com correlação alta. Posso afirmar que uma causa a outra?

**Resposta do assistente:**

## 5. Correlação

A correlação mede a associação entre duas variáveis numéricas.

No Pandas:

```python
df.corr(numeric_only=True)
```

Correlação não implica causalidade. Uma associação entre duas variáveis não demonstra que uma causa a outra.

📚 Fonte: Análise exploratória de dados (EDA)

---

### Q19
**Pergunta:** Quero comparar a distribuição das notas entre diferentes grupos de estudantes. Qual visualização pode ser adequada?

**Resposta do assistente:**

## 5. Boxplot

Boxplots permitem visualizar mediana, quartis e possíveis valores extremos.

```python
sns.boxplot(data=df, x="categoria", y="valor")
plt.show()
```

São úteis para comparar a distribuição de uma variável numérica entre grupos.

---

## 5. Funções

Funções permitem organizar um conjunto de instruções que pode ser reutilizado.

```python
def calcular_media(notas):
    return sum(notas) / len(notas)
```

A função pode ser utilizada da seguinte forma:

```python
media = calcular_media([7, 8, 9])
```

---

## 8. Escolha do gráfico

A escolha depende da pergunta que se deseja responder:

| Objetivo | Visualização |
|---|---|
| Observar distribuição | Histograma |
| Comparar categorias | Barras |
| Comparar distribuições | Boxplot |
| Observar relação entre duas variáveis numéricas | Dispersão |
| Observar várias correlações | Heatmap |

📚 Fonte: Visualização de dados, Python básico

---

### Q20
**Pergunta:** Meu modelo apresenta desempenho muito bom no treinamento, mas desempenho bem pior no conjunto de teste. O que pode estar acontecendo?

**Resposta do assistente:**

## 10. Overfitting

Overfitting ocorre quando o modelo se ajusta excessivamente aos dados de treinamento e apresenta desempenho inferior em dados não utilizados durante o treinamento.

Uma forma de identificar o problema é comparar o desempenho do modelo em treinamento e teste.

---

## 5. Separação entre treinamento e teste

Uma prática comum é dividir os dados em conjuntos de treinamento e teste.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

O conjunto de treinamento é utilizado para ajustar o modelo, enquanto o conjunto de teste é utilizado para avaliar seu desempenho em dados que não foram utilizados no treinamento.

---

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

📚 Fonte: Machine Learning

---

### Q21
**Pergunta:** Como configurar um servidor Linux para hospedar uma aplicação web em produção?

**Resposta do assistente:**

Não encontrei essa informação na minha base de conhecimento (Python básico, Pandas, Pré-processamento, Análise Exploratória, Visualização de Dados e Machine Learning). Posso ajudar melhor com dúvidas desses temas — consegue reformular sua pergunta dentro desse escopo?

---

### Q22
**Pergunta:** Como criar um aplicativo Android completo usando Kotlin?

**Resposta do assistente:**

Não encontrei essa informação na minha base de conhecimento (Python básico, Pandas, Pré-processamento, Análise Exploratória, Visualização de Dados e Machine Learning). Posso ajudar melhor com dúvidas desses temas — consegue reformular sua pergunta dentro desse escopo?

---

### Q23
**Pergunta:** Qual é a melhor estratégia de investimento para minha situação financeira?

**Resposta do assistente:**

Não encontrei essa informação na minha base de conhecimento (Python básico, Pandas, Pré-processamento, Análise Exploratória, Visualização de Dados e Machine Learning). Posso ajudar melhor com dúvidas desses temas — consegue reformular sua pergunta dentro desse escopo?

---

### Q24
**Pergunta:** Como configurar um banco de dados PostgreSQL em um servidor AWS?

**Resposta do assistente:**

Não encontrei essa informação na minha base de conhecimento (Python básico, Pandas, Pré-processamento, Análise Exploratória, Visualização de Dados e Machine Learning). Posso ajudar melhor com dúvidas desses temas — consegue reformular sua pergunta dentro desse escopo?
