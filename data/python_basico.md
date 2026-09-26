# Python básico para análise de dados

## 1. Variáveis

Variáveis são utilizadas para armazenar valores que podem ser utilizados durante a execução de um programa.

Exemplo:

```python
idade = 25
nome = "Ana"
altura = 1.65
```

Python possui tipagem dinâmica, portanto não é necessário declarar explicitamente o tipo da variável.

## 2. Estruturas de dados

### Listas

Listas armazenam múltiplos valores em uma única estrutura e podem conter elementos de diferentes tipos.

```python
idades = [18, 20, 25, 30]
```

Um elemento pode ser acessado pelo seu índice:

```python
idades[0]
```

O índice começa em zero.

### Dicionários

Dicionários armazenam informações utilizando pares de chave e valor.

```python
aluno = {
    "nome": "Ana",
    "idade": 20
}
```

Um valor pode ser acessado pela sua chave:

```python
aluno["nome"]
```

## 3. Condicionais

Estruturas condicionais permitem executar diferentes trechos de código dependendo de uma condição.

```python
idade = 20
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

## 4. Laços de repetição

O `for` pode ser utilizado para percorrer elementos de uma coleção.

```python
idades = [18, 20, 25]
for idade in idades:
    print(idade)
```

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

## 6. Tratamento de erros

O `try` e o `except` podem ser utilizados para tratar situações em que uma operação pode gerar uma exceção.

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
```

## 7. Boas práticas

Ao desenvolver análises em Python, recomenda-se:

* utilizar nomes de variáveis claros;

* dividir operações complexas em funções menores;

* evitar repetição desnecessária de código;

* utilizar comentários quando contribuírem para a compreensão;

* verificar os tipos dos dados antes de realizar operações;

* tratar possíveis erros durante o processamento.

## 8. Aplicação em análise de dados

Python é frequentemente utilizado em análise de dados devido à disponibilidade de bibliotecas especializadas, como Pandas para manipulação de dados, Matplotlib e Seaborn para visualização e Scikit-learn para aprendizado de máquina.

