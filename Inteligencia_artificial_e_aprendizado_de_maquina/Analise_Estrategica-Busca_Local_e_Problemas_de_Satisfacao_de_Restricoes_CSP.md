Análise Estratégica: Busca Local e Problemas de Satisfação de Restrições (CSP)

Sumário Executivo

Este documento sintetiza os fundamentos de dois paradigmas cruciais na resolução de problemas em Inteligência Artificial: a Busca Local e os Problemas de Satisfação de Restrições (CSP). Enquanto a busca tradicional foca no caminho para atingir um objetivo, a busca local prioriza a viabilidade ou otimização do estado final, sendo ideal para problemas de larga escala e otimização. Paralelamente, os CSPs introduzem uma representação fatorada do estado, decompondo-o em variáveis, domínios e restrições, o que permite o uso de heurísticas de propósito geral e técnicas de propagação de restrições para reduzir drasticamente o espaço de busca. Os principais destaques incluem a transição de estados atômicos para representações estruturadas e a aplicação de algoritmos como Hill Climbing e Backtracking com heurísticas avançadas.


--------------------------------------------------------------------------------


1. Busca Local e Otimização

A busca local opera sob a premissa de que o caminho percorrido no espaço de busca é irrelevante; o foco reside estritamente na solução (o estado final).

Conceitos Fundamentais

* Foco na Solução: Diferente da busca em largura ou profundidade, a busca local mantém apenas o estado atual e tenta melhorá-lo explorando sua vizinhança.
* Aplicações Típicas: Problema das 8-rainhas, coloração de grafos, roteamento de veículos e problemas de otimização industrial.
* Eficiência de Representação: No problema das n-rainhas, a representação por matriz é considerada ineficiente. A utilização de vetores (onde cada posição representa uma coluna e o valor a linha da rainha) é significativamente mais eficaz.

Paisagem do Espaço de Estados (Horizonte de Busca)

A eficiência dos algoritmos de busca local depende da topografia da função objetivo:

* Máximo Global: O ponto de maior utilidade em todo o espaço.
* Máximo Local: Um ponto superior aos seus vizinhos, mas inferior ao máximo global, onde algoritmos simples podem ficar "presos".
* Platôs e Ombros (Shoulders): Regiões onde a função objetivo é plana, dificultando a progressão para estados melhores.

Algoritmos de Destaque

* Hill Climbing (Subida de Encosta): Expande iterativamente o vizinho que mais melhora o resultado atual. Não olha além da vizinhança imediata.
* Simulated Annealing: Técnica que permite "pulos" para estados piores para evitar máximos locais, diminuindo a probabilidade desses pulos ao longo do tempo.
* Outros Métodos: Iterated Local Search (ILS), GRASP e Path Relinking.


--------------------------------------------------------------------------------


2. Problemas de Satisfação de Restrições (CSP)

A transição fundamental nos CSPs é a mudança de um estado atômico (indivisível) para uma representação fatorada.

Estrutura de um CSP

Um problema é definido pelo triplo (X, D, C):

* X (Variáveis): O conjunto de elementos que precisam de valores.
* D (Domínios): O conjunto de valores possíveis para cada variável.
* C (Restrições): Regras que determinam quais combinações de valores são permitidas.

Tipos de Restrições

Tipo	Descrição	Exemplo
Unária	Restringe o valor de uma única variável.	SA \neq \text{verde}
Binária	Relaciona os valores de duas variáveis.	SA \neq NSW
Alta Ordem	Envolve três ou mais variáveis (intervalos).	Between(X, Y, Z)
Global	Envolve um número arbitrário de variáveis.	AllDiff (ex: Sudoku)

Propagação de Restrições e Consistência

A propagação visa eliminar valores inconsistentes dos domínios antes ou durante a busca:

1. Consistência de Nó: Todos os valores no domínio da variável satisfazem as restrições unárias.
2. Consistência de Aresta (Arco): Garante que, para cada valor em um domínio, exista um valor correspondente no domínio da outra variável que satisfaça a restrição binária.
3. Consistência de Caminho: Avalia a consistência de um par de variáveis em relação a uma terceira.
4. K-Consistência: Generalização que garante que, dada uma alocação para k-1 variáveis, existe um valor consistente para a k-ésima variável.


--------------------------------------------------------------------------------


3. Busca e Inferência em CSPs

A resolução de CSPs frequentemente combina a busca sistemática com técnicas de inferência para antecipar falhas.

Busca com Retrocesso (Backtracking)

É uma versão da busca em profundidade (DFS) específica para CSPs.

* Aloca valores a uma variável por vez.
* Retrocede (backtrack) quando uma variável não possui valores consistentes com as alocações anteriores.

Heurísticas de Seleção

A ordem em que variáveis e valores são escolhidos impacta drasticamente o desempenho:

* Minimum Remaining Values (MRV): Escolhe a variável com o menor número de valores "legais" restantes.
* Degree Heuristic (Heurística de Grau): Escolhe a variável envolvida no maior número de restrições com outras variáveis não atribuídas.
* Least-Constrained Value: Escolhe o valor que deixa a maior flexibilidade para as variáveis vizinhas.

Inferência: Forward Checking

Sempre que uma variável é alocada, o algoritmo remove dos domínios das variáveis vizinhas os valores que agora se tornaram inconsistentes. Isso permite detectar falhas precocemente antes mesmo de expandir o nó.


--------------------------------------------------------------------------------


4. Teste de Conhecimento (Baseado no Conteúdo)

Este teste visa avaliar a compreensão dos temas de busca local e representação por restrições.

Questões Objetivas

1. No problema das n-rainhas, por que a representação por vetor é preferível à representação por matriz? a) Porque ocupa mais espaço na memória, facilitando o acesso. b) Porque cada posição do vetor já elimina implicitamente a possibilidade de duas rainhas ocuparem a mesma coluna. c) Porque permite a visualização direta do tabuleiro. d) Não há vantagem técnica, apenas estética.

2. O que caracteriza um estado "Consistente" em um Problema de Satisfação de Restrições? a) Todas as variáveis possuem valores atribuídos. b) Apenas algumas variáveis possuem valores atribuídos. c) Nenhuma restrição do problema é violada pela alocação atual de valores. d) O algoritmo de busca já terminou sua execução.

3. Qual heurística de CSP foca em escolher a variável que possui o menor número de opções válidas em seu domínio? a) Degree Heuristic. b) Least-Constrained Value. c) Forward Checking. d) Minimum Remaining Values (MRV).

4. Na busca local (Hill Climbing), qual é o principal risco de uma topografia com "máximos locais"? a) O algoritmo encontrar a solução ótima global muito rápido. b) O algoritmo parar de evoluir por acreditar que encontrou o melhor ponto, quando há outros superiores fora da vizinhança. c) O algoritmo entrar em um loop infinito entre dois estados iguais. d) A função de custo se tornar negativa.

Questões Dissertativas

5. Explique o funcionamento da restrição global "AllDiff" utilizando o exemplo do Sudoku. Resposta esperada fundamentada na fonte: A restrição AllDiff exige que todas as variáveis envolvidas tenham valores distintos. No Sudoku, ela é aplicada a cada linha, coluna e bloco 3 \times 3, garantindo que os números de 1 a 9 não se repitam nesses conjuntos. Ela pode ser simplificada em um conjunto de restrições binárias de desigualdade (ex: A1 \neq A2).

6. Diferencie Consistência de Nó de Consistência de Aresta. Resposta esperada fundamentada na fonte: A consistência de nó refere-se ao cumprimento de restrições unárias (uma única variável), como SA \neq \text{verde}. A consistência de aresta refere-se a restrições binárias entre duas variáveis, garantindo que para cada valor no domínio de X haja um valor correspondente em Y que satisfaça a relação entre elas.


--------------------------------------------------------------------------------


Gabarito das Questões Objetivas: 1: b | 2: c | 3: d | 4: b
