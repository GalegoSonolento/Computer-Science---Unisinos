Briefing: Resolução de Problemas e Busca Local

Sumário Executivo

Este documento sintetiza os princípios fundamentais da resolução de problemas via algoritmos de busca, com foco especial em técnicas de Busca Local. Diferente dos métodos de busca tradicionais (informados ou não-informados) que visam encontrar um caminho até um objetivo, a busca local prioriza a identificação de uma solução viável ou ótima dentro de um espaço de estados, sem a necessidade de registrar o caminho percorrido.

Os principais destaques incluem:

* Eficiência de Memória: A busca local é extremamente vantajosa por manter apenas o estado atual (ou uma população restrita), sendo ideal para espaços de busca imensos.
* Algoritmos Chave: Foram analisados o Hill Climbing (subida de encosta), Simulated Annealing (têmpera simulada) e Algoritmos Genéticos.
* Desafios de Otimização: O maior obstáculo nessas abordagens é evitar que o algoritmo fique preso em máximos locais, cordilheiras ou platôs, que impedem o alcance do ótimo global.
* Aplicações Práticas: Problemas como as N-Rainhas, coloração de grafos e roteamento de veículos são exemplos clássicos onde essas técnicas são aplicadas com sucesso.


--------------------------------------------------------------------------------


1. Fundamentos da Busca em IA

A busca é definida como o processo de encontrar uma sequência de ações para atingir um objetivo quando uma única ação não é suficiente. Um problema de busca é formalmente estruturado pelos seguintes componentes:

* Estado inicial: O ponto de partida.
* Conjunto de ações: Movimentos possíveis a partir de um estado.
* Modelo de transição de estados: Define o resultado de cada ação.
* Teste de objetivo: Determina se o estado atual é o alvo.
* Função de custo de caminho: Atribui um valor numérico a cada caminho.

1.1. Categorias de Busca

Tipo de Busca	Características	Exemplos
Não-informada (Cega)	Acesso apenas à definição do problema.	Busca em largura, Busca em profundidade.
Informada	Utiliza conhecimento específico (heurísticas).	Busca Gulosa (f(n)=h(n)), Busca A* (f(n)=g(n)+h(n)).
Busca Local	Foco na solução final, não no caminho.	Hill Climbing, Algoritmos Genéticos.


--------------------------------------------------------------------------------


2. O Paradigma da Busca Local

A busca local é aplicada quando o caminho para o objetivo é irrelevante. Ela opera explorando a "vizinhança" da solução atual.

2.1. Vantagens e Representação

* Eficiência: Exige pouca memória por não armazenar a árvore de busca.
* Representação de Estado: A escolha da estrutura de dados é crítica. No problema das 8-rainhas, o uso de um vetor (ex: [5, 6, 7, 4, 5, 6, 7, 6]) é significativamente mais eficiente que uma matriz, permitindo calcular sucessores de forma rápida (56 sucessores para o caso de 8 rainhas).

2.2. Paisagem do Espaço de Estados

O algoritmo navega por uma "topografia" definida por uma função objetivo ou de utilidade:

* Ótimo Global: O ponto de maior utilidade (ou menor custo) em todo o espaço.
* Ótimo Local: Um ponto que é melhor que seus vizinhos, mas inferior ao ótimo global.
* Platô: Uma área plana onde a função objetivo não varia, dificultando a direção da busca.
* Cordilheira: Sequência de ótimos locais difíceis de navegar.


--------------------------------------------------------------------------------


3. Algoritmos de Busca Local

3.1. Hill Climbing (Subida de Encosta)

Este algoritmo move-se iterativamente para o vizinho que apresenta a maior melhora imediata.

* Características: É um algoritmo guloso e incompleto (pode ficar preso).
* Desempenho no Problema das 8-Rainhas: Partindo de estados aleatórios, o algoritmo fica preso em ótimos locais em 86% das vezes. Se permitir movimentos em platôs, a taxa de erro cai para 6%, mas o número de passos aumenta consideravelmente.
* Variações:
  * Estocástico: Escolhe um vizinho melhor aleatoriamente.
  * Primeira Escolha: Implementa o primeiro vizinho melhor encontrado.
  * Reinício Aleatório: Executa a busca várias vezes a partir de pontos iniciais distintos.

3.2. Simulated Annealing (Têmpera Simulada)

Inspirado na metalurgia, este algoritmo combina a subida de encosta com a caminhada aleatória para evitar ótimos locais.

* Lógica: Aceita sempre movimentos de melhora. Movimentos de piora são aceitos com uma probabilidade baseada na Temperatura (T).
* Temperatura: Diminui gradualmente com o tempo. Se o resfriamento for lento o suficiente, o algoritmo garante encontrar o ótimo global com probabilidade próxima a 1.

3.3. Algoritmos Genéticos (AG)

Técnica de busca local inspirada na seleção natural e evolução das espécies.

* População: Mantém um conjunto de soluções (indivíduos/cromossomos).
* Função de Aptidão (Fitness): Avalia a qualidade de cada indivíduo.
* Ciclo Evolutivo:
  1. Seleção: Indivíduos mais aptos têm maior chance de reprodução (métodos: roleta, torneio, elitismo).
  2. Cruzamento (Crossover): Combina características de dois pais para gerar descendentes (ex: One-point, Two-point, Uniform). Foca na intensificação da busca.
  3. Mutação: Altera aleatoriamente partes do indivíduo com baixa probabilidade para garantir diversificação e evitar convergência prematura.


--------------------------------------------------------------------------------


4. Conclusões e Recomendações

O documento ressalta que a busca local é essencial para problemas onde o espaço de busca é vasto demais para algoritmos ótimos tradicionais.

4.1. Resumo Comparativo de Completude

* Hill Climbing: Incompleto e eficiente.
* Caminhada Aleatória: Completa, porém extremamente ineficiente.
* Simulated Annealing: Completo se o cronograma de temperatura for adequado.

4.2. Boas Práticas para Algoritmos Genéticos

Segundo as recomendações técnicas (Gendreau e Potvin, 2010), para obter melhores resultados em AGs:

* Prefira a seleção por torneio em vez da roleta.
* Utilize taxas de mutação adaptativas.
* Incorpore informações específicas do domínio do problema.
* Garanta a manutenção da diversidade de soluções na população.
* Execute o algoritmo múltiplas vezes para validar a consistência dos resultados.
