# Sintaxe, semântica e gerenciamento de memória

## semântica
### estática
- em tempo de compilação
- gerenciamento de variáveis
    - declarações
- escopos
- etc

### dinâmica
- construções em tempo de execução
- criações de strings novas, etc

## tipagem
### estática
- sempre tem o mesmo tipo
- se precisa mudar é só com casting
### dinâmica 
- muda o tipo, é só uma variável
- tipo no python

## semÇantica de atribuição e expressões
### atribuição
valor em variável
### expressões
- matemáticas mesmo
- precedências e construções para atribuição de uma variáve

## controle de fluxo
- instruções condicional e de repetição
- controle de execução de um programa

## funções e procedimentos
- chamadas e execuções
- escopo de variável
- definição de palavras-chave, etc

## semântica de tratamento de exceções
- jogar as exceções na tela
- sempre tente usar tratamentos (try(catch))

## análise semântica
- toda linguagem faz uma leitura do código e garante q ele não está fora das regras semânticas
- não utiliza palavras reservadas para outros fins
- garante estrutura do cod fonte
- prepara próximas etapas
### verificação de tipos
- verifica se estão dentro das regras
- compatibilidade entre tipos
- confirma os usos de casting (algumas fazem isso automaticamente)
### resolução de nomes
- mapeia nomenclaturas e declaração de variáveis
- os nomes de objetos etc
### escopo de variáveis
- cuida do uso das variáveis e garante q elas não sejam usadas em lugares inascessíveis
### geração de código intermediário
- C gera uma árvore pro código fonte
- esse meio do caminho serve pra criar um cod em assembly por exemplo pra ser lido pela máquina
### verificação de regras semânticas específicas
- assinaturas de métodos e verifica se as implementações obedecem (Java)
### detecção de erros semânticos
- uso de variáveis não declaradas (erros mais gerais)

# Gerenciamento Automático de Memória e Linguagens de Programação
- é um mecanismo de automação de alocação e liberação
- OS sempre guarda um espaço de memória alocada para usuário
- existe memória virtual q o OS dá uma gerenciada
    - nunca é o espaço físico mesmo, a memória virtual é maior e os programas dão um migué
- OS tem um "garbage coloector" tbm
    - não é uma gestão manual
    - dá pra concentrar mais lógica na aplicação
        - apesar de ainda pode realizar tanto
        - pode ser interessante ter isso em mente
- ter controle evita corrupção de dados e instabilidade de software
    - ainda mais em usos intensos
- redução de erros de assinalar memória alocada e etc
    - vai q estora pegando as memórias no dedão
- manutenção é facilitadas
- gerenciamento automático é normalmetne feito com GC (Garbage Collector)
    - existem alguns algoritmos relacionados à isso
    - ou contagem de referẽncias à algum objeto
## vantagens de gerenciamento automático
- reduz problemas básicos e tira bastante problema das costas do desenvolvedor
- abstrai detalhes bastante complexos
- premite sistemas mais robustos

## desvantagens de gerenciamento automático
- pode levar a dificuldades quando precisa de algo muito efetivo
- menos controle do desenvolvedor sobre os recursos da máquina
- pode impactar a aplicação
- pode gerar sobrecarga de memória

## considerações finais
- eventualmente precisa para pra pensar nisso
- normalmente as funcionalidades utilizam apenas automatização mesmo
- em alguns contextos o controle manual é bastante necessário
    - sistemas embarcados e de alto desempenho pode ser uma escolha mais bem pensada


DATA: 07/Junho/2024
# Progamação imperativa
- paradigma de programação
- precisava cuidar de estados de variável
- multiprocedural com procedimentos mecânicos
- primeiro paradigma (shells ão baseados nisso)
## tempo de vida
- alocação e liberação é montada pelo desenvolvedor
- precisa entregar os tempos de vida na hora de escrever os projetos
    - definição de escopos prioritária
    - estáticas
    - dinâmicas da pilha
        - alocadas em pilhas de memória e tem registros de mudança
        - libera quando termina de rodar o programa
    - variáveis do Heap
        - explícitas
            - malloc vetor e tamanho dele e free - libera mesmo
        - implícitas
            - gerenciamento automático
            - Garbage Collector
            - pra alterações aqui precisa de dump e uma mão pra mexer e configurar
- controle de fluxo é sempre por funções matemáticas
- 

- A facilidade de encapsulamento é bastante absurda quando expandida a niveis maiores

# Programação Funcional
- esquemas matemáticos
- suportado por várias linguagens (aplicativas)
- Linguagens normalmente implementam mais de um paradigma
- início da década de 60
    - atualmente a pilha é linguagem natural
- tapa o buraco da programação imperativa
- LISP - mcCarthy - 1960
    - fácil de sair programando
- mais confiáveis por serem mais fáceis de ler mesmo
    - manutenção também é facilitada
    - significados independentes de contexto
- função lamba (Java)
    - parâmetros de uma função
    - chama a função lambda e passa parâmetros pra ela
- é bastante interessante por ser otimizável, fácil de ler, fácil manutenção, baixa especialidade
    - fazer mais com menos linhas facilita

# Programação lógica
- declarativa
- operações e alfabeto, junto com tds os assets são entregues no começo da programação
- precisa declarar os objetivos alcançáveis do código
- cria uma lógica dentre as declarações
    - pode ser usada em árvores de decisão
    - criação de lógicas pra contextos específicos e montagem de árvores pode gerar caminhos diferentes de tomada de decisão
- IA usa algoritmos lógicos e pode gerar respostas diferentes dependendo de como os tokens são arranjados
    - não -deterministico
- SQL é uma linguagem lógica por exemplo


DATA: 21/Junho/2024
# Concorrência
- sistema pode montar threads
- interação de resposta e capacidade entre as interfaces
- dá sempre pra largar várias threads em várias pipelines pra rodar os processos mais rapidamenteo
- precisa cuidar da latência
    - web principalmente
    - enquanto mexe na máquina somente é de boa
    - threads podem aumentar e estourar o processamento em provisioning na nuvem
    - pode ser q dispare mta thread pra uma aplicação que precisa de pouco em em local com rede de baixa banda
- algumas aplicações podem ter concorrência à nível de I/O no código mesmo
    - I/O é bem mais lento que acessos à memória
    - dá pra usar API nos bancos mas elas competem por acesso
    - frontend só com SQL mata o sistema
        - precisa mudar as consultas todas se mudar alguma coisa
        - usa as API pra facilidar na escalabilidade
- os programas podem concorrer por recursos da máquina e concorrer em background
## condições de corrida
- mais trheads tentam usar dados compartilhados ao mesmo tempo
    - a informações pode estar desatualizada
    - se o programa usar threads, trate os erros propriamente
- pra evitar esses problemas, podemos usar Locks nas variáveis
- libera (release) depois de terminar a operação

# Tratamentos de Exceções e Eventos
- Tratamento de Exceções - Try, Catch e Finally
- Exceções durante a execução de um código podem ser comuns por diversos fatores, tais quais instabilidade de rede, erro em algum PATH, dados incoerentes, divisão por zero, acesso a um arquivo inexistente, etc;
O tratamento de erros evita que o programa “quebre” ou “termine” imediatamente se um erro acontecer, permitindo o programa continuar a rodar apesar dos erros;
O bloco Try engloba o código que pode encontrar uma exceção;
Catch é o bloco onde a exceção é tratada;
Finally detém um bloco que sempre será executado, sem se importar com a ocorrência de exceção ou não.
