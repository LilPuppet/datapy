# Pré-processamento de dados

## 1. Conceito

Pré-processamento é o conjunto de procedimentos utilizados para preparar os dados antes de uma análise ou aplicação de técnicas de aprendizado de máquina.

Dados reais podem apresentar valores ausentes, duplicatas, tipos inadequados, categorias textuais e valores discrepantes.

## 2. Identificação de valores ausentes

Em Pandas:

```python
df.isna().sum()
```

Essa operação permite verificar a quantidade de valores ausentes em cada coluna.

## 3. Tratamento de valores ausentes

Uma possibilidade é remover registros:

```python
df = df.dropna()
```

Outra possibilidade é realizar imputação:

```python
df["idade"] = df["idade"].fillna(df["idade"].median())
```

A escolha depende da quantidade de dados ausentes, da variável e do contexto da análise.

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

## 5. Conversão de tipos

Os tipos das colunas podem ser verificados utilizando:

```python
df.dtypes
```

Uma coluna pode ser convertida utilizando:

```python
df["idade"] = df["idade"].astype(int)
```

A conversão deve ser realizada somente quando o novo tipo for compatível com os dados.

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

## 7. Escalonamento

Alguns algoritmos podem ser influenciados pela escala das variáveis.

Por exemplo:

```text
idade: 18 a 80
renda: 1000 a 50000
```

Uma técnica de padronização é o `StandardScaler` do Scikit-learn:

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
dados_padronizados = scaler.fit_transform(dados)
```

O escalonamento deve ser aplicado de maneira adequada para evitar vazamento de informações entre treinamento e teste.

## 8. Vazamento de dados

Data leakage ocorre quando informações que não deveriam estar disponíveis durante o treinamento são utilizadas de maneira que forneça vantagem indevida ao modelo.

Uma prática importante é separar os dados de treinamento e teste antes de ajustar transformações que aprendem parâmetros a partir dos dados.

## 9. Boas práticas

Antes de iniciar um modelo de Machine Learning:

* conheça as variáveis disponíveis;

* verifique tipos e valores ausentes;

* identifique duplicatas;

* examine valores extremos;

* trate variáveis categóricas adequadamente;

* avalie a necessidade de escalonamento;

* evite vazamento de dados;

* registre as transformações realizadas.

