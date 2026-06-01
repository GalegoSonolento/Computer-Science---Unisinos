Lista de Exercícios 2 GB - Computação de Alto Desempenho

**1) O que você entende por heurística?**
Heurística é uma abordagem prática para realizar descobertas ou resolver problemas por meio de métodos simplificados, sem considerar todas as variáveis envolvidas. É uma forma de chegar a uma conclusão aproximada de maneira rápida. Ex.: largar um lápis para testar a gravidade, desconsiderando fatores como massa e atmosfera, ainda permite verificar de forma prática se ele cai em determinado período.

**2) Tenho 5 tarefas, cada qual com 5i. Tenho 3 recursos, cada qual com capacidade de 10i/s. Qual o tempo de execução?**
O tempo de execução é de 1 segundo.

**3) Tenho:**

**T1 = 10i**
**T2 = 5i**
**T3 = 20i**
**R1 = 5i/s**
**R2 = 10i/s**

**Qual o tempo com RR? E o ótimo?**
O tempo com RR é 6s, e o ótimo é 2,5s, onde o R1 executa apenas T1, e R2 executa T2 e T3.

**4) Por que a métrica (1 - load) * CPU é tão importante e usada?**
Essa métrica é utilizada para controle e Load Balancing; uma vez que ela demonstra o espaço disponível para alocação.
Em um cenário tal qual o seguinte:
tenho os cáculos de:
R1 = 1GHz, 60% load = 400MHz
R2 = 750MHz, 10% load = 675MHz
R3 = 2GHz, 80% load = 400MHz

Temos que o R2 será o mais adequado para, por exemplo, adicionar load (processos, threads, etc.) dado que ele ainda possui 675MHz à 10% de load; dessa forma, podemos mitigar overload, manter o sistema balanceado e impedir que, por exemplo, R3 torne-se o "Pedreiro mais lento".

**5) Dê exemplos de emprego de List Scheduling.**
De maneira geral, list Scheduling pode ser empregado em qualquer situação de PAD.
Alguns exemplos que podemos demonstrar seriam:
- cálculo de previsão do tempo
- Load Balancing em clusters
- escalonamento (inclusive em grid)
- fractal de mandelbrot