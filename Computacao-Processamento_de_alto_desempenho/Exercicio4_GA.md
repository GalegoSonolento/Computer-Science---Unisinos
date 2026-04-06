Responda, em grupos, e entregue até a prova do GA
1) **Por que um processo mais lento pode comprometer o desempenho de uma aplicação de Fases paralelas;** Esse processo compromete à partir do momento que temos, por exemplo, threads de usuário, de modo que esta uma thread atrasa as demais em um caso de acesso à recursos. Ou ainda, mesmo com threads de sistema, para seguir ao meu próximo passo, necessariamente preciso da resposta da minha thread retardatária; de modo que esta espera é cascateada para as threads subsequentes no nosso "grafo" de estados e estas parmanecem ociosas enquanto a mais lenta dita o ritmo de execução do programa completo (problema que é geralmente associado à gerenciamento de recursos).

2) Na sua opinião, qual a diferença entre Bag-of-tasks e Master-Slave;

3) **O que você entende por grão de paralelismo;** Entendo que o grão é a razão da computação pela comunicação (G = Computação/Comunicação). Temos que aplicações com grãos grossos terão bastante tempo de uso de processador (CPU Bound, mais computação) e ferão uma sequência de cálculos antes de retornarem ao programa principal; de forma que são mais trivialmente paralelizáveis e tem uso recorrente em Clusters, por exemplo. Grãos finos requerem mais tempo de comunicação (I/O Bound, mais tempo de barramento) e são, dessa forma, mais complexas em sua parelização (normalmente usam processadores vetoriais), uma vez que é fácil cair no revés do barramento (Lei de Amdahl).

4) Eu tenho uma aplicação que transforma uma foto colorida em preto e branco. Ela vale ser paralelizada? Se sim, como você faria?

5) Quais são os desafios na modelagem de aplicações Divisão-e-Conquista e Pipeline?