-> Anotações da cadeira
-> disciplina baseada no livro do CORMEN - Algoritmos: teoria e prática
-> Professora: Andriele Busatto do Carmo

DATA: 12/Aug/24
# Introdução - Complexidade de algoritmos, Recursos e Utilização de recursos por algoritmos
Algoritmos são *scripts*, ou passos, para a resolução de um problema qualquer (alguns são conhecidos e outros não).
Os algoritmos precisam resover problemas, certo, mas classificar um problema geralmente é um tanto complicado, por isso eles são quebrados em *instâncias*, e é nelas que os algoritmos irão agir.
Usualmente, para um algoritmo ser bem sucedido em sua função, ele precisa ser *correto* (resolve o problema da melhor forma para todas as instãncias), *eficiente* (usa *espaço* - e.g. memória - e *tempo* - literalmente - de forma decente - e.g. não explode o uso de RAM ou demora anos para finalizar) e *fácil de implementar* (preferncialmente evite dar 4 mortais, 3 piruetas e 45 cambalhotas para escrever).
Observemos o problema do caixeiro viajante. É um problema famoso que envolve passar em todas as cidades da maneira mais efetiva possível, evitando repetições e no tempo mais curto (evitando repetir rotas). A soluação desse problema existe, mas é uma busca exaustiva para cada novo cenário e pode chegar a n! permutações. Isso faz desse problema um *NP-Completo* (mais sobre isso no futuro); o que significa que algumas instâncias desse problema podem levar anos para serem completas.
Outro exemplo pode ser o do ator de cinama. Consiste no ator produzir o máximo de lucro, produzindo o máximo de filmes (todos os filmes dão o mesmo retorno). A resposta para esse problema consiste nele produzir o maior número de filmes (sem overlapping); a resposta é: sempre produzir o filme com término mais cedo de todos os disponíveis. Nesse caso, a resposta pode ser bastante rápida, uma vez que a análise é, em si, pequena.
Existem algumas formas de mostrar a corretude de um algoritmo. Uma delas pode ser por *prova e contra-exemplo*, demonstrando uma instância ou exemplo em que a resposta não é suficiente ou não pode ser aplicada. Outra forma famosa (mas mais complexa) é a *indução matemática e recursão*; induções matemáticas levam em conta *caso base*, *hipótese* e *caso geral*. Usualmene provas matemáticas são mais confiáveis e "garantem" a confiabilidade do código.

Ok, existem vários algoritmos e maneiras de mostrá-los como mais efetivos, mas qual o melhor?
Alguns fatores devem ser colocados em jogo na hora de escolher um algoritmo para uso (em algoritmos de ordenação, por exemplo):
- a quantidade de itens a ordenar
- como os elementos estão ordenados no momento
- possíveis restrições nos valores dos elementos
- a arquitetura do computador
- o tipo dos dispositivos de armazenamento utilizados: memória principal, disco
A escolha do algoritmo passa por todos esses itens (no nosso exemplo de algoritmos de ordenação). Usualmente, na comparação de 2 algoritmos, eles terão melhor desempenho em situações distintas. Assim como em limites, existe um *ponto de inflexão*. Pegue, por exemplo, o *Insertion sort* (C_1n²) e o *Merge sort* (C_2nlgn) e considere que C_1 < C_2. Para valores *n* baixos, o Insertion sort vence por ter uma constante de funcionamento menor; todavia, a natureza exponencial dele faz com que isso não mais compense para valores de n maiores que o ponto de inflexão.
-> Tenha em mente que, para valores tendendo ao infinito, logaritmos são respostas mais favoráveis.



- normalmente soluções menos eficientes tem mais facilidade de implementação
    - dificilmente acontece o contrário
    - por isso análise de complexidade é necessária
        - vai q é tão complexo que dá a volta
- alguns algoritmos não podem ter complexidades menores ou já chegaram em locais estagnados ou soluções "próximas da ideal"
- algoritmos precisam resolver independentemente da **instância**
    - instãncias -> diferentes entradas
- sempre conheça o seu problema
    - algoritmos de escalonamento -> existem vários
        - mas ainda assim casos diferentes requerem estruturas diferentes
- se a prova do algorimo funciona ele é favorável
    - abrir mão de algumas coisas pode ser ideial 
- algoritmo não é a implementação do algoritmo
    - algoritmo tem no máximo um pseudocódigo para facilitar a compreensão
    - colocar código como resposta é ruim
        - implementa algumas escritas desnecessárias pra entendimento geral do algoritmo
    - artigos entregam pseudocódigo
- casos de teste diferentes pras soluções (outas instâncias) vão calejar a solução
- a busca de uma solução absoluta geralmente leva pra um n! (fatorial)
    - busca exaustiva é caro
- prova de funcionamento de algortimo é só se for por indução matemática mesmo 
    - não-corretude funciona como provas de conceito e testes
    - ainda preciso usar isso pra provar que ele realmente tem a complexidade que eu estou dizendo que ele tem
- soluções candidatas podem não estar corretas
- historicamente implementações escolhem minimizar **espaço** ou **tempo**
- Tempo constante na análise é um tempo desvinculado
    - normalmente chama de *c*
    - tempos que o sistema usa pra operações não relacionadas com a atividade do algoritmo
    - eles podem influenciar o resultado final (podem variar entre os algoritmos)
- N suficientemente grande ou entrada suficientemente grande
    - isso aqui é pra dizer que passa do ponto de inflexão e vale a pena usar o algoritmo mais lerdo (mas que cresce mais lentamente)
    - tendência de N ao infinito


### Exercícios
- **Dê um exemplo de aplicação real em que é necessário usar ordenação:** Ordenar lista telefônica em ordem alfabética
- **Além da velocidade, que outro critério pode ser utilizado para medir eficiência?** Capacidade de processamento de instruções /s
- **Escolha uma estrutura de dados que você conhece, e liste seus prós e contras.** Pilha
Prós:
- FILO
- Ordenamento automático (coloca-se os itens na ordem)
- Fácil de implementar

Contra:
- Ordenamento precisa ser feito fora da pilha
- Inflexibilidade

- **Dê um exemplo de problema real em que somente a melhor solução é permitida, e um exemplo de problema em que uma solução próxima da melhor é “aceitável”.** 
-> apenas melhor permitida: ordenamento de ponto cirúrgico
-> aceiável passa: cara dos correios / roteamento de rede


## Perguntas
- como q faz pra ler esses livros enormes? - Realmente precisa ler os capítulos. De preferência um por vez.
- mesmo que a solução funcione, ela ainda pode ser errada? - Sim, caso ela não seja efetiva em todos os casos, assim como exposto em aula sobre as necessidades básicas de um algortimo.


DATA:19/Aug/24
# Introdução à Análise de Algoritmos: modelos RAM, análise de melhor, pior e caso médio, análise assintótica, propriedades de notações assintóticas e taxas de crescimento de funções e relações de dominância
- dependendo da forma de implementar, mesmo sendo o mesmo algoritmo
    - linguagens diferentes
    - ambientes diferentes
    - hardware diferente
    - todos afetam o tempo de execução do algoritmo
## Modelo RAM
- Random Memory Access
- computador hipotético
- não vincula a informação à uma máquina real
- operações simples
    - soma
    - subtração
    - atribuição
    - ...
    - 1 unidade de tempo na máquina hipotética
- laços e subrotinas são compósitos de operações simples
- armazenar 100 ou 1000 elementos
    - é o mesmo processo, mas o espaço usado é diferente
- não diferencia tipos de acesso de memória (RAM, disco, cache, etc)
- memória infinita
- conta a quantidade de operações relizadas
    - pode ser uma label mesmo
- análise de algoritmo não é implementação
    - é apenas o algoritmo
- por isso máquinas RAM não representam a realidade, só o comportamento do algoritmo
- nesse modelo tenta-se olhar para todas as instâncias (impossível)
    - só 3 importam
    - pior, melhor e médio caso
- analise dos tipos de caso precisa de alguns específico
    - para algoritmos de ordenação
        - já ordenado
        - invesamente ordenado (ao contrário)
        - aleatório
- normalmente se monta um gráfico com a cresente do número de passos
- análise sempre para o tamanho de N
- se pega alguns casos médios para traçar no gráfico e a análise ser mais completa
- a análise é sempre feita em cima do pior caso
    - se ele for razoável, estamos bem
    - mais *reliable* para implementações
- sempre relacionado à instâncias do problema

### Pior caos
- executa *todas* as instruções que o compõe

### Melhor caso
- algoritmo pula alguns passos

### Caso médio
- a média de execução mesmo
- pega o melhor e o pior e faz a média

## Análise assintótica - Big Oh Notation
- trabalhando em termos de limites
- limites inferior e superior
- o comportamento do algoritmo oscila bastante
    - ele pode se comportar de formas diferentes dependendo do tamanho da entrada
    - dificulta nomenclatura específica dos piores casos
- n_0 = N suficientemente grande
    - a partir daqui se mostram as curvas upper bound e lower bound
    - a partir de n_0 a análise segura para N tendendo ao infinito
    - é a partir de onde o upper ou lower cobre a curva da função
- assíntota -> à medida que tende ao infinito o comportamento real e o upper bound se aproximam
- ignora constantes multiplicativas
- tempo constante é o que faz o algoritmo funcionar mas não é relacionado ao tamanho da entrada
- constantes to theta são sempre maiores que zero
    - no theta é o N_0 que serve pros 2
- cuide a ordem de apresentação
    - sempre a função = conjunto
    - notação é errada matemáticamente (sinal de pertence != do de igual, mas aqui pode, azar)
- [1 ]

## Propriedades e notação
- transitividade utiliza uma notação lógica para incluir uma função dentro do domínio de outra

## Taxa de crescimento e funções e relação de dominância
- não existe resposta ideal na vida real
- a notação O tem uma relação de dominância dentro de um grupo
    - quadráticas
    - logaritmicas
    - ...
- tempos logarimicos normalmente estão em pesquisa binária
- 

## Pergutas
- Não existem algoritmos que mudam o bigO dependendo da entrada/execução? - não, existe um bigO para cada ponto da função
- O theta é a média do upper e do lower? - não, theta é a aplicação dos dois e no cenário que ambos funcionam
- Existem valores de O não citados na aula, certo? Eles são muito específicos para serem referenciados ou por que os exemplos (ordenação) caem nos citados? - Existem, mas eles são um pouco mais complexos e não são tão pertinentes nessa altura do campeonato
- a definição é dada olhando o algoritmo mesmo
- constantes normalmente são maiores do que 1 (principalmente c)
- 


### Referências
- The Algorithm Design Manual (Skiena) 
    - Capítulo 1 - Introduction to Algorithm Design
- Introduction to Algorithms (Cormen, et al.)
    - Capítulo 1 - The role of Algorithms in Computing