DATA: 05/Agosto/2025
# Apresentação, conceitos básicos e execícios
- Máquina universal - pode fazer qualquer coisa
- LInguagem
    - Bons resultados vem de bons prompts
    - Se o algoritmo resolve o problema ele é computável
- Alfabeto
    - conjunto finito de caracteres
    - finito (sempre)
    - formação de palavras - *word* - sentença
    - números também é um conjunto {0,...,9}
    - P.R. - palavras reservadas - conceito de linguagens de programação
        - termos usados pela linguagem - variáveis não podem ter esses tempos
    - variáveis n podem começar com números
        - eles já representam valores
    - ε -> já constitui um termo != ∅ ou {}
- Cadeia de símbolos
    - concatenação de 0 ou mais caracteres do meu alfabeto
    - é uma String bem dizer
    - é possível constituir restrições
- Palavra
    - cadeia de símbolos finita
    - Array
    - precisa analisar pra ver se encaixa no alfabeto e se está de acordo com a linguagem
    - & -> cadeia vazia
    - todo alfabeto tem a palavra vazia
        - a menos que Σ exista - alfabeto
        - Σ* -> todas as palavras (qualquer palavra)
        - Σ+ -> todas as palavras menos a vazia {ε}
            - palavra vazia é um conjunto
        - se assume por padrão que a palavra vazia existe
            - analise a linguagem que é montada
- Comprimento ou tamanho de uma palavra
    - primeiros 32 caracteres são válidos em uma variável
        - padrão
    - |W| = definição de cumprimento de palavra
    - |ε| = 0
        - precisa analisar no que a palavra deriva, não no que ela é naquele momento
        - |εabc| = 3 (comprimento)
- Prefixo e sufixo
    - sim, igual o português
    - prefixo e sufixo **não** compreendem a palavra inteira
- Subpalavra
    - palavra encontrada dentro de outra
    - e.g.:sinos em unisinos
    - precisa ser contíguo
    - **nunca** vai ser a palavra inteira
    - pelo menos 2 caracteres da palavra
- Linguagem Formal (Linguagem)
    - alfabeto - conjunto finito que monta infinitas *words* dependendo da linguagem
    - conjunto de palavras sobre um alfabeto
    - L = {w | w = |3|} -> só posso fazer palavras de comprimento 3
        - aqui não tem a palavra vazia
- Concatenação
    - tem um expoente
    - (ab)² = abab
    - ab² = abb
    - tudo que não tiver um expoente
- Concatenação Sucessiva
    - w^0 = ε
    - concatenação com expoentes
    - as duas podem se misturar

DATA: 12/Agosto/2025
# Programas, máquinas e computações
- máquinas podem ser equivalentes entre si e programas
- programas precisam de máquinas
- programas ainda são algoritmos
    - operações e teste com controle
- máquinas interpretam programas
    - todas as funções computadas podem ser representadas em máquinas de turing
- computações
    - interpretações de entradas que geram uma saída
- um programa deve virar um fluxograma e vice-versa
    - testes são operações de condição
- estruturação iterativa é o mais próximo de uma linguagem
- comandos sempre sequenciais
    - condição de saída
- ifs - não-determinísticos
- sequencialidade é sempre uma flecha
- compisições concorrentes não tem uma ordem importante 
    - *threads*
    - "irrelevante"
- qualquer tipo de escolha é não-determinística
- como uma anotação simples, o programa iterativo 

- ordenação seria computação <- contém> máquinas <- contém> programas
- programas devem possuir estruturas de controle e testes

-  Programas
- iden. de operaç~es sempre são letras - instruções
- identificadores de teste (escolha) são Ts (até Tn)
- operação vazia indica encerramento
    - símbolo de check
    - ou colocar um rótulo q n existe na saída

- programa monolítico
    - rotulados
    - formulado com fluxogramas
    - instruções rotuladas (rn)
    - rótulo é uma palavra
    - par ordenado P = (I, r)
        I - conjunto de instuções - significado
        r - instrução/rótulo
    - rótulos únicos para cada instrução
    - sempre INTEGER
    - programas de diferentes tipos podem fazer a mesma coisa
    - P é sempre um programa
    - a manutenção pode ser um problema - prefira códigos estruturados
    - desvios complexos podem ser um problema
    - a seta sempre significa o "faça" nos fluxos
    - etiquetas = rótulos

DATA: 19/Agosto/2025
- programa iterativo
    - ele é, bom, iterativo
    - entrelaça com vários comandos
    - repetições
    - P é um programa
    - operações vazias podem ter sequanciais
        - também pode ser uma operação de saída
        - precisa ter atenção e interpretar o que ele significa no momento
    - composição sequencial V;W -> executa V e logo depois W
        - ; é indicação de sequencial na sequência apresentada
    - organização utilizando chaves
    - é uma notação mais próxima de um pseudo-código
    - uso de parênteses necessário para evitar ambiguidade
    - idente
    - se enquanto e teste todos têm o mesmo símbolo

DATA: 26/Agosto/2025
# Recursividade
- empilhamento
- nem todo programa pode ser escrito na recursividade
- definição de scape é bastante importante
    - expressão vazia funciona
- composição considicional ainda é o T
- continua se chamando (laço próprio)
- E0 - expressão inicial (posso ter vários)
- R1 define E1 e assim vai
- fluxograma ainda continua o mesmo
    - mesmos símbolos e letras
- o sinal de checkmark (√) é basicamente um break
- as chamadas, definições, são sub-rotinas
    - são basicamente funções
- as subrotinas são declarações (definições - def) de função por assim dizer
- existem tantas subrotinas quanto forem necessárias e todas as subrotinas possuem definição

DATA: 09/Setembro/2025
# Máquinas universais
- simulação de qualquer programa computável
- a mais comun é a máquina de Turing
- cabeça de controle que pode ir pra direita ou esquerda
    - preciso de um símbolo inicial e final
    - MT
    - máquinas sempre infinitas
- maquina de Turing
    - qualquer coisa computável fica na fita
    - alfabeto de entrada
        - determina reconhecimento da Linguagem
    - alfabeto auxiliar
        - registra as validações
        - variações do alfabeto já existente
    - início da fita é um sol
    - final da fita é a letra grega Beta
    - Tem uma porrada de letra grega na verdade
        - M = (∑, Q, δ, q0, F, V, β, ☼)
        ∑ alfabeto de símbolos de entrada.
        Q conjunto de estados possíveis da máquina, o qual é finito.
        δ programa ou função de transição (é uma função parcial).
        q0 estado inicial da máquina, tal que q0 é elemento de Q.
        F conjunto de estados finais, tal que F está contido em Q.
        V alfabeto auxiliar.
        β símbolo especial que representa o branco.
        ☼ símbolo especial de marcador que representa o início da fita.
        - essa notação precisa necessariamente ser escrita junto da máquina de estados para formar, efetivamente, a máquina de Turing
    - na máquina de Turing normalmente n tem um "ir pra frente" depois do final
    - a ideia de validação é uma marcação que já li aquela casa
        - pra isso serve o alfabeto auxiliar
    - formado por estados
        - sempre saio de um pra outro
        - a transição de estado é sempre indicada no fluxo do autômato
            - apesar do desenho sempre ser indo pra direita
    - obrigatoriamente precisa passar pela fita gravando
        - nem q grave o msm símbolo de novo
    - aceita entrada de dado
    - chega em um estado final
        - precisa chegar em qf (validou a fita toda)
        - troca o f pela numeração dos estados
    - dá pra rejeitar entradas
        - que não pertençam ao alfabeto ou linguagem
    - dá pra fazer um loop
    - símbolo inicial tem um loop no q0 pra evitar um estado a mais
        - evita passar por cima do q0
    - alfabeto auxiliar é sempre definido por quem constrói a máquina
    - dá pra gravar alfabeto ou o auxiliar (ou branco ou axiliar) - ∑, V ou β
    - máquinas de Turing são específicas para uma linguagem
        - a fita cria uma máquina de estados que valida uma linguagem
        - fita e máquina de estados
- Conceitos Básicos: 
    - Símbolo: menor unidade.
    - Alfabeto: conjunto de símbolos.
    - Palavra: sequência de símbolos.
    - Linguagem: conjunto de sentenças sobre um alfabeto.
- Tipos de Dados
    - Qualquer conjunto contável que apresente descrição finita (naturais, inteiros, caracteres, valores-verdade, vetores, entre outros). 
    - irracionais não satisfazem essa condição
- a Máquina de Turing é basicamente uma fita (com a informação) com uma cabeça
    - essa cabeça pode tanto ler quanto escrever
    - unidade de controle (o algoritmo mesmo) fica junto dessa cabeça
    - esses algoritmos são montados como máquinas de estado
    - tem no mínimo o mesmo poder de processamento que qualquer máquina de uso geral
    - 𝚷(p, au) = (q, av, m) → 𝚷(estado_atual, simb_lido) = (novo_estado, simb_gravado, sent_movimento)
    - 


DATA: 16/Setembro/2025
# Máquina de norma
- parte de uma máquina universal
- deve ser executável em tempo finito
- deve ser capaz de executar qualquer programa de máquinas reais ou teóricas
- Norma (esposa do Richard Bird) - Number Theoretic Register Machine
- valores de memória (registradores) são todos letras maiúsculas
- programas iterativos
- não recebe uma atribuição completa, precisa somar pra chegar nela
- nomenclatura *usando X* transfere o uso e decremento pra outra variável à vontade de manter a de apoio
- só tem operação de soma e subtração
    - todo o resto precisa ser feito baseado nisso

DATA: 07/Outubro/2025
# Máquinas (continuação)
- agora temos uma 7-upla
- sempre 2 registradores
    - duas entradas e uma saída ou vice-versa
    - assumem valores em N
- aqui é uma comunicação pra monolítico, iterativo ou Turing
    - a descrição da máquina e suas definições precisam ser estabelecidas primeiramente
- máquina já vem com as operações todas descritas
    - e operacional
    - não precisa inserir M
- toda máquina vira qualquer máquina
    - pra virar recursivo precisa de algum grau de recursividade, claro
- com máquinas monolíticas é mais simples de trabalhar com valores
- computação infinita = loop
    - prova de que operação não finaliza
    - "erro"
- valores de testes (normalmente baixos) para testes precisam ser utilizados
- isso é mais perto de um Assembly que os outros
    - descrição de ações mais semelhante
- 7-upla => M = (V, X, Y, πx, πy, ∏F, ∏T) 
- a declaração da máquina aqui passa todas as funções que ela pode exercer
- a computação é sempre inicializada por um par pelo menos (entrada e saída)
    - podem existir N entradas e usualmente uma só saída
- a máquina precisa passar, também, os testes realizados nela para que ela seja possível
    - caso eles falham ou sejam impossúiveis com as funções fornecidas, a tradução está errada
- depois de montar a máquina em dada linguagem (monolítica, iterativa ou recursiva) é necessário verificar se a máquina é finita ou não
    - não, não existe meio termo