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
- 