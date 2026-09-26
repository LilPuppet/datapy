# Pandas

## 1. Conceito

Pandas é uma biblioteca Python utilizada para manipulação e análise de dados estruturados.

As principais estruturas utilizadas são `Series` e `DataFrame`.

Um `DataFrame` representa uma estrutura tabular composta por linhas e colunas.

## 2. Importação

A biblioteca normalmente é importada utilizando

```python
import pandas as pd
```

## 3. Criação de um DataFrame

Um DataFrame pode ser criado a partir de um dicionário

```python
dados = {
    "nome": ["Ana", "João", "Maria"],
    "idade": [20, 25, 22]
}

df = pd.DataFrame(dados)
```

## 4. Visualização dos dados

Para visualizar as primeiras linhas

```python
df.head()
```

Para visualizar as últimas linhas

```python
df.tail()
```

Para obter informações sobre as colunas e seus tipos

```python
df.info()
```

Para obter estatísticas descritivas

```python
df.describe()
```

## 5. Seleção de colunas

Uma coluna pode ser selecionada utilizando

```python
df["idade"]
```

Múltiplas colunas podem ser selecionadas utilizando

```python
df[["nome", "idade"]]
```

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

## 7. Ordenação

Para ordenar um DataFrame

```python
df.sort_values("idade")
```

Para ordenar de forma decrescente

```python
df.sort_values("idade", ascending=False)
```

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

## 9. Valores duplicados

Para identificar linhas duplicadas

```python
df.duplicated().sum()
```

Para remover duplicatas

```python
df.drop_duplicates()
```

## 10. Agrupamento

O método `groupby()` permite realizar operações agrupadas.

Exemplo

```python
df.groupby("cidade")["idade"].mean()
```

Esse código calcula a idade média para cada cidade.

## 11. Combinação de DataFrames

O método `merge()` pode ser utilizado para combinar DataFrames relacionados.

```python
resultado = pd.merge(
    df_alunos,
    df_escolas,
    on="id_escola",
    how="inner"
)
```

O tipo de junção deve ser escolhido de acordo com a relação desejada entre os dados.

## 12. Boas práticas

Durante a manipulação de dados com Pandas:

- verifique os tipos das colunas;
- examine valores ausentes antes de removê-los;
- identifique possíveis duplicatas;
- valide os resultados após transformações;
- evite modificar dados sem compreender o impacto da operação;
- utilize nomes de colunas claros e consistentes.
