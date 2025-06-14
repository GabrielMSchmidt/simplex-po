# Implementação do Algoritmo Simplex

> Projeto final da disciplina de Pesquisa Operacional.

Este repositório contém a implementação do **Algoritmo Simplex**, desenvolvida do zero com a linguagem Python. O código abrange desde a leitura e interpretação de um problema de Programação Linear até a execução completa das **Fases 1 e 2** do método para encontrar a solução ótima.

---

## O que é o Algoritmo Simplex?

O **Algoritmo Simplex** é um dos métodos mais famosos e eficientes para resolver problemas de otimização de **Programação Linear (PL)**. O objetivo de um problema de PL é encontrar o valor máximo ou mínimo de uma função linear (chamada função objetivo), sujeito a um conjunto de restrições também lineares.

A intuição por trás do Simplex é geométrica:
1.  O conjunto de todas as soluções viáveis de um problema de PL forma uma região convexa com múltiplos lados, chamada de **polítopo**.
2.  Sabe-se que a solução ótima do problema (se existir) estará sempre em um dos **vértices** (ou "quinas") desse polítopo.
3.  O algoritmo funciona de maneira iterativa, "viajando" de um vértice para um vértice adjacente, sempre buscando melhorar o valor da função objetivo. Ele para quando não consegue encontrar nenhum vértice adjacente melhor, indicando que a solução ótima foi encontrada.

### As Duas Fases

-   **Fase 1**: O objetivo desta fase é encontrar uma solução inicial viável, ou seja, um ponto de partida (um primeiro vértice) para o algoritmo. Ela é necessária quando a origem (todas as variáveis iguais a zero) não é uma solução válida para o problema.
-   **Fase 2**: Partindo da solução viável encontrada na Fase 1, esta é a fase principal do Simplex, que itera entre os vértices do polítopo até atingir a solução ótima do problema.

---

## Funcionalidades Implementadas

-   **Interpretação do Problema**: Leitura de problemas de PL a partir de um formato definido.
-   **Construção do Tableau**: Montagem da tabela (tableau) Simplex na Forma Padrão.
-   **Método Simplex de Duas Fases**: Implementação completa da Fase 1 (para encontrar uma solução viável) e da Fase 2 (para otimização).
-   **Análise de Solução**: Identificação de soluções ótimas, múltiplas soluções, soluções ilimitadas e problemas inviáveis.