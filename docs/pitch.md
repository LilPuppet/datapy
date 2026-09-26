# Pitch — DataPy Assistant

## O problema

Quem está começando em análise de dados com Python esbarra o tempo todo em
dúvidas pequenas, mas que travam o progresso: "como verifico valores
ausentes?", "isso é overfitting?", "posso remover duplicatas direto?".
Buscar isso no Google/ChatGPT funciona, mas traz dois riscos: informação
desatualizada/errada, ou uma resposta genérica demais que não segue o
material que a pessoa está de fato estudando.

## A solução

O **DataPy Assistant** é um assistente virtual restrito a um escopo bem
definido — Python básico, Pandas, pré-processamento, análise exploratória,
visualização e machine learning — que responde **apenas com base numa base
de conhecimento própria**, sempre citando a fonte, e que **admite quando não
sabe** em vez de inventar.

Na prática, isso significa:

- Uma pergunta como *"O que é overfitting?"* recebe a definição exata da
  base, com o exemplo de código relevante.
- Uma pergunta como *"Qual a melhor estratégia de investimento?"* recebe uma
  recusa educada, porque está fora do escopo — em vez de uma resposta
  genérica e sem lastro.

## Como funciona (visão técnica rápida)

1. A base de conhecimento (6 arquivos Markdown) é dividida em seções.
2. Cada pergunta da pessoa usuária é comparada com essas seções usando um
   mecanismo de busca por relevância (TF-IDF com stemming leve).
3. Se a melhor seção encontrada tiver relevância suficiente, o assistente
   monta a resposta a partir dela e cita a fonte.
4. Se não, o assistente diz claramente que não tem essa informação.
5. Opcionalmente, se houver uma chave de API da Anthropic configurada, o
   trecho recuperado é passado como contexto para o Claude reescrever a
   resposta de forma mais natural — sempre restrito ao que foi recuperado.

Isso garante uma aplicação que **funciona hoje, sem custo de API**, e que
pode escalar para respostas mais fluidas quando integrada a um LLM.

## Validação

Testamos o assistente com 24 perguntas cobrindo conhecimento direto,
raciocínio aplicado e casos fora de escopo (ver `docs/perguntas.md`). O
resultado (`docs/resultados.md`):

- **183 de 192 pontos possíveis (~95%)** na avaliação por critérios de
  correção, relevância, clareza e aderência à base.
- **100% de acerto** ao reconhecer perguntas fora do escopo (4 de 4).
- **Zero respostas com informação tecnicamente incorreta.**
- Limitações identificadas e documentadas de forma transparente (ex.: uma
  pergunta sobre escalonamento de variáveis não recuperou a seção ideal por
  causa da diferença de vocabulário entre a pergunta e o texto da base).

## Valor do projeto

- Mostra, de ponta a ponta, como transformar um material de estudo em um
  assistente confiável: base de conhecimento → prompts/regras →
  aplicação → avaliação com métricas reais.
- É **honesto sobre suas próprias falhas**: em vez de esconder erros de
  recuperação, o processo de avaliação os expõe e vira insumo para
  melhorar a base e o motor de busca — um ciclo replicável para qualquer
  outro domínio de conhecimento (não só Python/dados).
- É extensível: a mesma arquitetura serve para qualquer outra base de
  conhecimento (basta trocar os arquivos `.md` em `data/`).
