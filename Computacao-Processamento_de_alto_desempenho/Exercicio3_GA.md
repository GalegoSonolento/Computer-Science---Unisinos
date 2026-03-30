Responda, em grupos, e entregue até o dia da Prova do GA
1) O que você entende por reprodutibilidade de resultados numa execução em cluster?
Reprodutibilidade pode ser entendida como a manutenção do ambiente de teste através de todo o espaço de pesquisa. Em clusters, a alocação de espaço e processamento é feita necesariamente, à fim de que recursos sejam "perdidos" durante um processamento e se garanta a previsibilidade de isolamento. Além disso, todas as máquinas do cluster precisam ser homogêneas, de outra forma, alocações em máquinas diferentes, mesmo que dentro do memso cluster, atingiriam resultados diferentes. 

2) Como a velocidade da CPU pode impactar no desempenho da Rede?
A variar do uso da CPU e de seu poder de processamento (dado que o TCP/IP é executado à nível de software), o gargalo na comunicação de rede será ela. Por mais que o thouput de rede passe pela placa, o processamento do dado e do overhead ainda é montado pela CPU, desse modo, ela pode se tornar um gargalo se não for mantido o devido cuidado.

3) Por que, nativamente, o TCP atua com bufferização de dados?
Essa técnica é implementada devido ao custo de rede, considerando o tempo de envio e o desperdício ao enviar pacotes muito pequenos com muito overhead. A bufferização busca evitar esse desperdício ao acumular dados antes de enviar, formando pacotes maiores e mais eficientes.
Além disso, essa bufferização também utiliza um timer para evitar que os dados fiquem presos esperando mais informações, garantindo que o envio ainda aconteça em tempo adequado.

4) O que você etende por controle de Jitter?
O controle de jitter busca minimizar variações de tempo de execução, visando trazer um desempenho mais consistente e eficiente para sistemas paralelos.

5) Monte uma tabela comparativa entre cluster e grid computing.

Critério        Cluster                         Grid

Máquinas        Máquinas paralelas              Componentes distribuídos
Composição      Replicação de computadores      União de clusters
Domínio(s)      Único                           Diferentes
Controle	    Centralizado	                Não centralizado
Comunicação     Troca de mensagens              Interfaces e protocolos padrão