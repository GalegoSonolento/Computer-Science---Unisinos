Responda, em grupos, e entregue até o dia da Prova do GA
1) O que você entende por reprodutibilidade de resultados numa execução em cluster? Reprodutibilidade pode ser entendida como a manutenção do ambiente de teste através de todo o espaço de pesquisa. Em clusters, a alocação de espaço e processamento é feita necesariamente, à fim de que recursos sejam "perdidos" durante um processamento e se garanta a previsibilidade de isolamento. Além disso, todas as máquinas do cluster precisam ser homogêneas, de outra forma, alocações em máquinas diferentes, mesmo que dentro do memso cluster, atingiriam resultados diferentes. 

2) Como a velocidade da CPU pode impactar no desempenho da Rede? A variar do uso da CPU e de seu poder de processamento (dado que o TCP/IP é executado à nível de software), o gargalo na comunicação de rede será ela. Por mais que o thouput de rede passe pela placa, o processamento do dado e do overhead ainda é montado pela CPU, desse modo, ela pode se tornar um gargalo se não for mantido o devido cuidado.

3) Por que, nativamente, o TCP atua com bufferização de dados?

4) O que você etende por controle de Jitter?

5) Monte uma tabela comparativa entre cluster e grid computing.