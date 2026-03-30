Briefing: Resolução de Problemas via Busca Local e Satisfação de Restrições

Sumário Executivo

Este documento sintetiza as metodologias de resolução de problemas em Inteligência Artificial baseadas em Busca Local e Problemas de Satisfação de Restrições (CSP). Enquanto a busca tradicional foca no caminho para atingir um objetivo, a busca local prioriza a solução final, sendo ideal para problemas de otimização onde o estado inicial é irrelevante. Paralelamente, os CSPs introduzem uma representação fatorada do estado, decompondo-o em variáveis, domínios e restrições. A eficiência nessas abordagens é alcançada através de representações de dados otimizadas (como vetores em vez de matrizes), heurísticas de seleção de variáveis (como Minimum Remaining Values) e técnicas de propagação de restrições para reduzir o espaço de busca antes mesmo da exploração exaustiva.


--------------------------------------------------------------------------------


1. Busca Local e Otimização

A busca local é aplicada quando o caminho percorrido até a solução não possui importância, focando exclusivamente em encontrar o estado que satisfaça o objetivo ou maximize/minimize uma função de utilidade.

1.1 Características Fundamentais

* Foco na Solução: Mantém-se apenas a solução atual (estado incumbente), descartando os caminhos percorridos.
* Exploração de Vizinhança: A partir de um estado, exploram-se estados adjacentes para encontrar melhorias.
* Eficiência de Representação: O uso de estruturas de dados simplificadas é crítico. No problema das n-rainhas, representar o tabuleiro como um vetor (onde o índice é a coluna e o valor é a linha) é significativamente mais eficiente que o uso de matrizes.
* Aplicações Comuns: Problemas de n-rainhas, coloração de grafos e roteamento de veículos.

1.2 O Horizonte de Busca (Landscape)

A eficácia da busca local depende da topografia do espaço de estados, definida por uma função objetivo:

* Ótimo Global: O melhor estado possível em todo o espaço.
* Máximo/Mínimo Local: Estados que são melhores que seus vizinhos, mas inferiores ao ótimo global.
* Platôs (Flat Local Maximum): Áreas onde a função objetivo é constante, dificultando a direção do movimento.
* Ombros (Shoulder): Regiões planas que podem levar a melhorias adicionais.

1.3 Algoritmos Representativos

Algoritmo	Descrição
Hill Climbing	Explora iterativamente a vizinhança e move-se apenas se houver melhora (subida de encosta). É ganancioso e não olha além da vizinhança imediata.
Simulated Annealing	Técnica que permite movimentos "piores" para escapar de máximos locais, baseada no resfriamento gradual.
GRASP / ILS	Metaheurísticas que utilizam buscas locais iterativas ou procedimentos adaptativos aleatórios para explorar o espaço de forma mais robusta.


--------------------------------------------------------------------------------


2. Problemas de Satisfação de Restrições (CSP)

Diferente da busca atômica (onde o estado é uma "caixa preta"), o CSP utiliza uma representação fatorada, permitindo que algoritmos de propósito geral identifiquem quais partes do estado violam restrições.

2.1 Componentes do CSP

Um problema CSP é definido pelo conjunto \{X, D, C\}:

* Variáveis (X): Elementos que precisam de valores (ex: regiões em um mapa).
* Domínios (D): Conjunto de valores possíveis para cada variável (ex: cores {vermelho, verde, azul}).
* Restrições (C): Regras que limitam as combinações de valores permitidos.

2.2 Estados no CSP

* Parcial: Algumas variáveis possuem valores atribuídos.
* Completo: Todas as variáveis possuem atribuições.
* Consistente: Nenhuma restrição é violada. Uma solução é uma atribuição completa e consistente.

2.3 Tipos de Restrições

* Unária: Restringe o valor de uma única variável (ex: SA \neq verde).
* Binária: Relaciona duas variáveis (ex: SA \neq NSW).
* Global / Alta Ordem: Envolve múltiplas variáveis. O exemplo clássico é o AllDiff, onde todas as variáveis de um conjunto (como uma linha de Sudoku) devem possuir valores distintos.


--------------------------------------------------------------------------------


3. Propagação de Restrições e Consistência Local

A propagação de restrições visa reduzir o domínio das variáveis antes ou durante a busca, eliminando valores que comprovadamente não podem fazer parte de uma solução.

* Consistência de Nó: Garante que todos os valores no domínio de uma variável satisfaçam suas restrições unárias.
* Consistência de Aresta: Garante que para cada valor no domínio de uma variável X, existe um valor no domínio de Y que satisfaz a restrição binária entre elas.
* Consistência de Caminho: Avalia a consistência de triplas de variáveis.
* k-consistência: Generalização onde, dada uma atribuição consistente para k-1 variáveis, sempre existe um valor para a k-ésima variável.


--------------------------------------------------------------------------------


4. Algoritmos de Busca para CSP

A busca principal em CSPs é o Backtracking, que é essencialmente uma busca em profundidade (DFS) adaptada para atribuições de variáveis.

4.1 Heurísticas para Melhoria de Desempenho

A ordem em que as variáveis e valores são escolhidos impacta drasticamente a velocidade da busca:

* Minimum Remaining Values (MRV): Escolhe a variável com o menor número de valores "legais" restantes.
* Degree Heuristic: Escolhe a variável envolvida no maior número de restrições com outras variáveis não atribuídas.
* Least-Constrained Value: Escolhe o valor que deixa a maior flexibilidade (mais opções) para as variáveis vizinhas no grafo de restrições.

4.2 Inferência Durante a Busca

* Forward Checking: Sempre que uma variável é atribuída, o algoritmo olha para as variáveis vizinhas e remove valores inconsistentes. Isso permite antecipar falhas antes que o algoritmo explore ramos sem saída.
* Salto para Trás (Backjumping): Em vez de retroceder apenas um nível no conflito, o algoritmo volta diretamente para a variável que causou a impossibilidade da atribuição atual, evitando repetir erros em ramos irrelevantes.
