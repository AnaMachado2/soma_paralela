# 1. Descrição do Problema

O programa implementado tem como objetivo **calcular a soma de um grande conjunto de números inteiros armazenados em um arquivo texto**. Cada linha do arquivo contém um valor pertencente ao conjunto {-1, 0, 1}.

O algoritmo utilizado percorre o arquivo linha por linha convertendo os valores para inteiros e acumulando a soma em uma variável.

Nos experimentos foi utilizado um arquivo contendo aproximadamente **1.000.000 de números**.

A paralelização foi implementada dividindo o arquivo em partes e processando cada parte com **múltiplas threads** simultaneamente.

O objetivo da paralelização é **reduzir o tempo total de execução** do programa utilizando os múltiplos núcleos do processador.

A complexidade aproximada do algoritmo é **O(n)**, pois cada elemento do arquivo é processado apenas uma vez.

---

# 2. Ambiente Experimental

Os experimentos foram realizados no seguinte ambiente:

| Item                        | Descrição                         |
| --------------------------- | --------------------------------- |
| Processador                 | Processador do computador pessoal |
| Número de núcleos           | Multicore                         |
| Memória RAM                 | 8 GB                              |
| Sistema Operacional         | Windows                           |
| Linguagem utilizada         | Python                            |
| Biblioteca de paralelização | threading                         |
| Compilador / Versão         | Python 3                          |

---

# 3. Metodologia de Testes

Os experimentos foram realizados executando o programa nas seguintes configurações:

* 1 thread (execução serial)
* 2 threads
* 4 threads
* 8 threads
* 12 threads

O tempo de execução foi medido utilizando a biblioteca **time** da linguagem Python.

O arquivo utilizado nos testes possui aproximadamente **1 milhão de números inteiros**.

Para cada configuração foi registrado o tempo total de execução do programa e os resultados foram utilizados para calcular o **speedup** e a **eficiência**.

---

# 4. Resultados Experimentais

| Threads | Tempo de Execução (s) |
| ------- | --------------------- |
| 1       | 1,6                   |
| 2       | 0,28                  |
| 4       | 0,30                  |
| 8       | 0,36                  |
| 12      | 0,33                  |

---

# 5. Cálculo de Speedup e Eficiência

Speedup foi calculado pela fórmula:

[
Speedup(p) = \frac{T(1)}{T(p)}
]

Eficiência foi calculada pela fórmula:

[
Eficiência(p) = \frac{Speedup(p)}{p}
]

---

# 6. Tabela de Resultados

| Threads | Tempo (s) | Speedup | Eficiência |
| ------- | --------- | ------- | ---------- |
| 1       | 1,6       | 1       | 100%       |
| 2       | 0,28      | 5,71    | 35%        |
| 4       | 0,30      | 5,33    | 75%        |
| 8       | 0,36      | 4,44    | 55,56%     |
| 12      | 0,33      | 4,84    | 40,40%     |

---

# 10. Análise dos Resultados

Os resultados mostram que o uso de paralelismo reduziu significativamente o tempo de execução do programa em comparação com a versão serial.

O speedup obtido não foi totalmente linear, pois existem custos adicionais associados à criação e gerenciamento das threads.

Observa-se que a eficiência diminui conforme o número de threads aumenta, o que é esperado devido ao overhead de paralelização e à competição por recursos do processador.

Além disso, fatores como sincronização entre threads e acesso à memória podem impactar o desempenho.

---

# 11. Conclusão

O uso de paralelismo trouxe melhoria no desempenho do programa, reduzindo o tempo de execução em relação à versão serial.

O melhor desempenho foi observado com um número moderado de threads, pois o aumento excessivo de threads pode gerar overhead e reduzir a eficiência.

De forma geral, o experimento demonstra que o paralelismo pode melhorar o desempenho de aplicações que processam grandes volumes de dados, desde que seja utilizado de forma adequada.

---
