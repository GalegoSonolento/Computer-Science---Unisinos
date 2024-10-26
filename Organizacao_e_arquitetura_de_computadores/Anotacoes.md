## Pertinências
- processadores ainda n conseguem manipular sinal analógico
- um overflow é uma operação com resultado maior do que os bits suportados
- LSB - bit menos significativo
- MSB - bit mais signigicativo
- ULA é o principal componente de um bloco de dados 
- [img do 1° slide com o ciclo de dados]
    - o processador é montado pela ula e o controle
    - quem calcula mesmo é a ULA
- considções de reset são representadas com setas nas máquinas de estado 
    - normalmente n são representados nas tabelas, mas variam à vontade, é só configurar direito
- memória RAM n faz parte do processador
    - a única são os registradores
- ISA - Conjunto de Instruções de uma Arquitetura
- PC - registrador de indexação das memórias
- o tamanho do barramento de memória n depende tanto assim da arquitetura
    - a qunatidade de memória RAM possível de ser endereçada varia conforme a quantidade de endereços que o sistema pode dar
- 'end' são as marcações de endereço que estou buscando
- o parelismo de instruções depende de quantas vezes dá pra dividir o processador (divido em 100, tenho 100 paralelos)
    - o problema disso é q se acontece alguma lentidão a gente mata umas 50-70 instruções (hazards)
    - processadores bem projetados n devem ter hazards estruturais
- a forwarding unit vai fzr o controle do chaveamento do *bypass* pra conflito de dados
    - se n é estall ou espera
- processo de declaração de variáveis
    done    halt                            end of program
    five    .fill   5
    neg1    .fill   -1
    stAddr  .fill   start                   will contain the address of start (2)
    - esses .fill marcam as viariáveis
- lables são marcações (como start) - permitem marcações dinâmicas (variáveis mesmo)
- Em processadores MIPS o R0 sempre é uma constante de zero
- os melhores desempenhos de hardware são quando existe implementação de forwarding e especulação de hazard de controle
- hazards estruturais nunca deveriam existir
    - resolvidos na organização do processador
- N dá pra implementar pipeline no Neander/CISC purinho
    - precisa de um esquema pra simular máquina Harvard/RISC
- única coisa q muda entre processadores multiciclo e com pipeline é a unidade de controle
- B | D | E | M | WB -> processos didáticos básicos de um processo pra execução (B-instrução/D-dados/E-execução/M-memória/WB-escrita de resultados)
- Hazards impedem a execução da próxima instrução de algum modo (somente em pipeline pra mais complexas)
- escrita nos registradores em WB acontece no começo e leitura (armação) da operação em D é no final, ent dá pra dx as duas no mesmo clock
- pra ativar o forwarding, o registrador necessário precisa ser o mesmo do destino da operação anterior
    - Lw (load word) gera o load user hazard - esse dado só sai depois da leitura de memória, a próxima linha nem vai ter acesso pq o dado nem ao menos existe
        - resolve usando duas técnicas - bypass/forwarding/reordenação + stall
- instruções inválidas quando a predição falha em hazards de controle, ela continua executando, mas o sistema só n deixa elas escreverem na memória
    - são essencialmente instruções inúteis
    - previsão estática
- previsão dinâmica
    - só funciona pq códigos repetem muitas instruções
    - histórico de decisões n é fixo
    - 

DATA: 27/Fev/2024
# Revisão de sistemas digitais, circuitos sequencias e fsm, Simulador de Computador
## Processador
Faz parte da arquitetura de Von Neuman. A arquitetura abrange uma Unidade de controle que manda nos comandos e um Ciclo de dados elaborado com flip-flops JK, em sistemas sequenciais de estado (o processador tem uma máquina de estados dentro dele basicamente)
- calcular, processsar e devolver o processamento
- circuito digital
    - Recebe instruções que dizem como o dado processado deve se comportar
- processadores são programáveis e tem instruções definidas pra processamento dos dados q ele recebe
- o simples é entender que ele é um operador simples
- memórias são elementos externos ao processador
    - apesar de algumas interfaces dele terem memórias
        - a principal no caso
    - registradores ficam dentro do processador (na maioria dos casos)
## Arquitetura x organização
### Arquitetura
- atributos visiveis ao programador e impactam diretamente a execução do programa
- conjuntos de instruções, qtde de bits e mecanismos de E/S influenciam
### Organização
- referente à parte interna
- implementação do hardware
- sinais de controle ,tecnologia de memória, transistores, ...
- n necessariamente interfere na programação, mas sim como ele funciona por baixo dos panos
## Sistemas digitais
- números limitados de valores (0 e 1)
- pulso ou n pulso
    - embasamento do sinal digital
- Bit - unidade mínima (0 ou 1)
- Byte - 8bits
- Palavra - sequência de bytes do tamanho da arquitetura
- Trabalha-se com bases:
    - decimal
    - binária
    - octal - bem pouco utilizada
    - hexadecimal - escalas de cor ou texto em arquivos
### Conversão de decimal
- fazer por divisões sucessivas
- pega o valor decimal e divide ele várias vezes pelo valor da base
- quando chegar em um valor igual ou menor q a base, para
- monta a sequência na ordem invertida e monta o binário, hexadecimal, etc
## Aritmética binária
- é igual uma soma decimal só q com 2 números
- um bit de estouro é um carry
- a subtração tbm é igual a decimal
## Circuitos combinacionais fundamentais
### Multiplexador (mux)
- tem um seletor de entradas pra escolher um pra saída
- Ele basicamente escolhe qual das entradas vai ir pra saída
### Demultiplexador
- Um entrada é quebrada em uma das saidas
- tbm possui um seletor dentro pra dizer qual saída foi agraciada
### XOR - C=A(+)B
- ou exclusivo
- comportamento dela é identico a uma soma binária
- entradas precisa estar em estados diferentes pra saída ser c/ carga (1) - verdadeira
### Meio somador - Half adder
- as entradas vão pro XOR e saem um ADD com C
- [inserir img do meio somador]
### Somador completo (full adder)
- leva em conta o carry out das operações anteriores
- tem basciamente um meio somador dentro pra geração de carry
- [img do somador completo]
- com somadores complestos dá pra fzr uma soma binária de palavra
### Unidade Lógica Aritmética (ULA)
- ula é um componente de operação de unidades lógicas aritméticas
- so uma das operações é mapeada pra saída
- a ula permite um número x de operações
- bota 2 valores q chegam nas entradas do multiplexador
- o seletor pega qual das operações vai ser realizada
## Circuitos sequenciais
- sempre precisa ter uma maneira de resetar
    - n dá pra garantir q tá em zero
        - só com reset
- Execução de sequência
- Precisa de um sinal de clock
- Depende das entradas e do estado anterior do ritmo
### Flip flop SR
- retem informação dentro do clock
- mantém essa info até uma condição ser feita
- base pra elementos de memória
- as duas entradas positivas vão dar abiguidade e n retornar uma saída (manter a q existe muito provavelmente)
### Flip flop D
- montam os registradores dos processadores
- veirifca entradas nas bordas de subida ou descida
- saída só muda no momento de alteração de clock
- sem o clock ele n muda o dado de entrada nunca
    - tá sempre sobreescrevendo o dado salvo
    - se necessário posso deixar de reter a info por querer
### Registrador
Esses registradores são máquinas puras de estado montadas com flip-flops JK. Precisam existir tantos quantos bits o processador processa.
- clocks comuns
- uma saída pra cada flip-flop FK
- unidade de memória mais básica do processador
### FSM - Finite State Machine - máquinas de estados finitos
Máquinas de estado finitos normalmente são ou de Mealy ou de Moore. Normalmente a usabilidade de uma máquina de Mealy é mais simples.
- um contador tem uma só sequencia, mas é bastante parecido com um FSM
- percorrem sequências de estados
- definição de sequencias de passos
- a função é gerar sequências de controle
- Mealy
    - saída depende de estado e entradas
    - estado é um circulo com o nome
    - cada estado da máquina de estados é uma contagem
    - dependendo da condição pra chegar no estado tal o valor de saída pode mudar
    - saída é apresentada na transição
- Moore
    - só depende do estado
    - estado é um circulo com o nome e a saída
    - trocou o estado a saída modifica
- máquinas de estado só os principais componentes dentro de um bloco de controle
- máquinas de estado normalmente levam pra algum lugar
- <img src = "imgs/Representacao_de_uma_maquina_de_estados_meanly.png">
### Flip-flop JK
- clock na subida
- guarda info
- J e K regem as condições de transição
- J=0 e k=0 Q n muda
- J=1 e K=1 Q inverte
- J=1 e K=0 -> 1
- J=0 e K=1 -> 0
- as operações devem ser feitas bit a bit - as respostas são as condições que mudam do atual pro próximo
- vai ter um flip-flop pra cada bit
- Aqui nesse cálculo dá pra aplicar Karnaugh

DATA:12/Mar/24
# Arquitetura e organização de computadores: visão geral, Componentes do computador e organização interna.
- dentro do bloco de controle existe uma máquina de estados
    - alterações nesses estados dependem de entradas
- bloco de dados processa as operações
    - composto de ULAs
## Von Neuman
- memória única pra dados e instruções
### Processador Neandor
- n existe implementação física - e para fins educacionais
#### Arquitetura
- copmutador pega o código e manda pra assembly > depois ainda monta os bits (linguagem de máquina) - que é realmetne gravado na memória RAM
- como o código é escrito independe da arquitetura
    [adicionar marcador 1]
    - mas o assembly disso depende bastante
    - versionamento está presente
[Adicionar table ISA do slide]
- os registradores funcionam como variáveis
- CISC
    - possui várias funções com acesso à memória
[adicionar marcador 2]
##### Formato das instruções
- NOT, NOP - 1byte
- STA, OR, AND, LDA, ADD, JMP, JN, JZ - 2 bytes - 1 pro dado e outro pra marcação de variável
##### características gerais
- propósito geral armazenam dados
    - 8bit
- propósito específico tem funções específicas
    - PC - 8bit
- de estado
    - 2bit
- sempre calculados em múltiplos de 2
##### ciclo de busca
- busca
    - buscar instrução e copiar com o RI (registrador)
        - vai ser trabalhado aqui
    - PC incrementa pra próxima operação
    - 
- decodificação
- busca de operandos

#### Organização
- 256 posições x 8 bits
    - nessa arquitetura de 8bits
    - arquiteturas mais robustas tem mais endereços de memória (precisam de mais bits)
- sempre com 2 flipxflops
##### transferências necessárias
- AC, PC, RI, RDM, REM, N, Z - todos registradores
- todos os elementos têm controles

#### trans entre regs.
- NOP
    - busca a instrução da memória 
    - joga pro registrador
    - incremente no PC
    - REM <- PC
    - read; incremento
    - RI <- RDM
- STA - armazena acumulador
    - 2 bytes
    - busca é sempre igual
    - tem a fase de execução
        - armazenamento
        - lê o endereço de armazenamento
        - incrementa o PC
        - pega o dado do AC (acumulador)
        - salva na memória
    - REM <- PC
    - read; incremento
    - RI <- RDM
    - REM <- PC
    - read; incremento
    - REM <- RDM
    - RDM <- AC
    - write
- LDA
    - mesmo esquema do STA
    - N e Z indicam se o valor do registrador é Negativo ou Zero
- ADD (soma)
    - busca e execução
- OR 
    - igual
- AND
    - muda só a operação
- NOT
    - busca e inverte o valor direto de AC pra AC
- Funções de desvio incondicional
    - JMP (jump)
        - onde estou
        - para onde desvio
        - busca e puxa da mem(PC)
- devio condicinal
    - JN (jump condicional)
        - parecido com o jump, mas antes tem uma valização nas flags N e Z
    - JZ
        - igual
- HLT (halt)
    - finalização do programa
#### sistema de memória
- memória tem coneçoes de entrada e saída
- o PC define onde é escrito
    - mas existe uma porta (REM - Registrador de Endereço de Memória) que manda a informação de endereço
- quem realmente escreve é o RDM - Registrador de Dado de Memória
- read and write são marcadores da função a ser feita
    - vem da unidade de controle
[colocar marcação 3]
##### Operações
- x <- MEM(y) na realidade tbm tem passos dentro
    - REM <-
    - read
    - x <- RDM
    - esses processos acontecem dentro da memória 
- o PC é quem regitra o valor do y
- incremento do PC pode ser feito em paralelo
- 

## Harvard
- duas memórias, uma de dado e outra de instruções
- em tese posso ler duas informações ao mesmo tempo
### processador MIPS
- utilizado dentro do Harvard

## Tipos de instruções
- existem tipos de instruções para o processador
### RISC
- instruções simples
- LOAD e STORE
    - únicas funções que acessam memória
- limitada nos acessos ao hardware
    - ainda pode acessar registradores
- normalmente usado por arquiteturas harvard
### CISC
- instruções complexas
- qql instrução pode acessar memória 
    - pode gerar problemas
- podem operar com dados de registrador e memória para fzr qualquer cálculo
- normalmente usado por arquiteturas von neuman
- comandos com tamanhos de bytes diferentes
- diferentes tempos pra processamento

DATA: 19/Mar/24
<img src = "imgs/Anotacao_1_aula_3.png">
<img src = "imgs/Anotacao_2_aula_4.png">

### O conceito de speed up
- ganho de desempenho de máquina multiciclo vs pipeline
- T_pipeline = T_sempipeline/num estágios da pipeline -> isso é teórico
    - teórico porque na prática existe uma equalização de execuções, já q a pipeline precisa paralelizar as instruções.
    - às veses isso come tempo

DATA: 26/Mar/24
# Hazards
- conflitos na execuçã
- problemas q causam a próxima instrução a pular um ciclo de clock
[inserir anotação 1]

DATA: 28/Maio/2024
# Memória
A hierarquia de memória funciona de forma piramidal, sendo que as memórias mais rápidas (e caras) ficam mais perto do topo (cache). As memórias secundárias (HD e/ou SSD) são as mais lentas quando comparados às memórias de cache (e bastante mais baratas também).

<img src="imgs/hierarquia_de_memorias.png">

Normalmente existem dois lvl de cache, um dentro do processador (L1, L2, etc) e outra na parte de fora, mais perto da memória principal (DRAM)
Existe uma unidade para medir a taxa de acertos das páginas de informação lançadas para as memórias cache. Isso serve como um benchmark importante, já que o pouco espaço precisa de conjuntos mais agregados de memória para execução dos programas. 
- Siga a fórmula h = número acertos/total de acessos
    - considere um acerto uma informação já presente em cache

- Um princípio interessante é o da localidade
    - temporal significa que se um espaço de memória foi referenciado ele provavelmene será novamente em um curto espaço de tempo
    - espacial significa que se uma informação foi referenciada, provavelmente as posições próximas a ela também o serão em um curto espaço de tempo

- memórias cache são montadas com tecnologia SRAM e são bastante caras e pequenas.
- memória principal (DRAM) tem múltiplos acessos de memória e facilita comunicação rápida
    - deadlocks podem afetar o tempo de acesso
- um fato interessante é que, para colocar pipelines na estrutura Von Neumann, foi necessário criar memórias intermediárias para acesso múltiplo (Cache de instruções e Cache de Dados) para as instruções Misc funcionarem propriamente
- a criação de caches unificadas entre as caches separadas e a memória principal foi criada para diminuir o tempo de acesso e manter as caches primárias no mesmo clock do relógio.
    - em múltiplos processadores existem múltiplos pares de cache nível 1 ligados a uma mesma memória principal

# Entradas e saídas
- E/S aborda o problema dos múltiplos padrões de entrada e saída
- E/S dividem a entrada em linhas de endereço, dados e controle, todas com os próprios canais

<img src="imgs/arquitetura_entrada_e_saida.png">

<img src="imgs/estruturacao_de_coms_es_com_cpu.png">

- a E/S é precisa ser tratada de alguma maneira já que os dados não tem uma entrada constante muitas vezes
    - é possível tratar programando a CPU para realizar esse check na E/S a cada x tempo e ler o q ela manda
    - pedir pra colocar um DEMON na E/S e avisar a CPU toda vez que algo entrar na fila para ser escrito
    - ou ainda usar um DMA, que vai fzr todo o trabalho e só mandar o dado mastigado pra CPU
        - é importante deixar anotado que o DMA sevre muito bem como um intermediário entre a CPU e os dispositivos de E/S, pq ele permite a CPU trabalhar em outras tarefas enquanto ele lida com os dados entrando ou saíndo
        - ´bom ter em mente que ele ainda precisa de um canal de comunicação de dados diretamente com a CPU no barramento, ent arquiteturas com barramento único serão prejudicadas com interrupções mais frequentes
            - as arquiteturas mais modernas já montam barramento especificamente pra entrada e saída que são geridos pelos DMAs
            - assim só a comunicação entre DMA e CPU pega no barramento principal

DATA: 11/Junho/2024
# Arquiteturas paralelas
- máquinas escalares produzem uma instrução por ciclo de máquina
- máquinas superescalares (pipelines) mais de uma instrução por ciclo de máquina
    - umas 2 instruções mais ou menos
    - tem mais de uma ULA dentro do processador e vai buscando as instruções conforme o número de ULAs
    - mais de u fluxo de instruções
    - os cores são virtuais tbm -> normalmente são dois fluxos por processador
- o limite de clock da tecnologia de silício existente hj são 5GHz (literalmente)
    - até dá pra ultrapassar mas precisa cuidar mto pra n queimar e perder informações

## Taxonomia de Flynn
A classificação de Flynn (1972) é a mais utilizada. Ele se
baseia nas possíveis unicidade e multiplicidade dos fluxos de
instruções e de dados para definir quatro tipos de arquiteturas:
- SISD (Single Instruction Stream, Single Data Stream):
computadores sequenciais
- SIMD (Single Instruction Stream, Multiple Data Streams):
computadores vetoriais e matriciais
- MISD (Multiple Instruction Streams, Single Data Stream):
não existem (HENNESSY et al., 2003; STALLINGS, 2002)
- MIMD (Multiple Instruction Streams, Multiple Data Streams):
arquiteturas com múltiplos processadores independentes

## Processamento Paralelo
- 2 ou mais processadores simultaneamente reslvendo o mesmo problema
    - n só montar 2 pc na rede
- em computadores matriciais (GPUs) - SIMD (Single Instruction Stream, Multiple Data Streams)
    - uma única instrução consegue manipular vários dados ao mesmo tempo
## MIMD (Multiple Instruction Stream, Multiple Data Stream)
    - vários fluxos e vários processadores (processadores independentes) pra solução do mesmo problema
    - compartilhada
        - controle
        - un. processamento
        - isso em todos os pares
        - todas compartilham a msm memória
        - vai ser uma arquitetura multicore maior
        - várias unidades de controle gerenciada por 1 OS
    - distribuída
        - máquinas completas alimentando o mesmo banco de dados
        - interligadas por sistemas de comunicação
        - em cima do OS tem mais uma camada de gerenciamento das máquinas
        - é um cluster basicamente
- processadores tem aplicações distintas em diferentes situações
    - o desempenho pode ser problemático se n usar a ferramenta certa para o trabalho
- multiprocessamento simétrico precisa de todos os processadores iguais numa msm interconexão
    - tbm na msm memória
    - SMP - simetrical multi processor
    - todos enxergam os mesmo endereços de memória
        - o endereçamento é único pra tds
    - arquitetura comummente encontrada em sistemas de end-user
    - sem processador especializado
    - Crossbar - matriz com os múltiplos caminhos de acesso
        - a memória se fragmenta mas ainda é um único espaço de endereço
        - bastante cara
    - UMA - Uniform Memory Access
        - todo mundo leva um tempo x pra acessar posições de memória
    - barramento de tempo compartilhado
        - a estrutura ainda continua a mesma de um processador
        - evita conflito de dados
        - os processadores ocupam o barramento pra usar o slot de tempo
    - o mais difundido é o barramento compartilhado com cache
- Acesso não-uniforme na memória (NUMA)
    - único espaço de memória
    - processadores em nós
        - própria cache e principal no barramento
    - conceitos de memória local e global
    - tudo dentro de uma mesma placa de silício
    - nã são exatamente comuns
        - usadas em aplicações científicas e supercomputadores
        - modelagem, previsão do tempo ,...
    - endereçamento contínuo
- clusters
    - máquinas separadas
    - nós de integração ao cluster
    - podem ser um recurso de comp unificado
    - resolvendo o msm problema
    - massa única de processamento
    - conectados em interface de rede
    - escalabilidade absoluta
    - incremental 
        - dá pra ficar adicionando mais nós no cluster
    - disponibilidade
        - se alguns nós falharem o sistema completo não cai

## Cluster
É um grupo de computadores completos/autônomos
(usualmente chamados nós) interconectados, que podem
trabalhar juntos, como um recurso de computação unificado,
criando a ilusão de uma máquina única.
Os nós são geralmente conectados através de uma porta de E/S
(geralmente interfaces de rede) de alto desempenho.
Atualmente eles são utilizados com sistemas gerenciadores de
bancos de dados, com servidores WEB e, principalmente, para
processamento. paralelo.

- Divisão de tarefas entre máquinas completas
- as máquinas são nós
- em tese n tem limite de nós
    - apesar de haver pontos ótimos para determinadas tarefas
    - tradeoff
- redes de Ethernet são bastante úteis pra esse tipo de arquitetura
    - dá pra usar USB ou outros tipos de comunicações
- importante baixa latência
    - normalmente geograficamente concentrados
- exigem custos menores que supercomputadores
- essa arquitetura ficou pra grandes datacenters de cloud
- hradware no cluster pode ser heterogênio - tem uma camada por cima
    - tds as máquinas precisam ter o msm OS pro software de gerenciamento funcionar
- clusters precisam do mínimo de paralelismo pra fazer sentido =
- clusters são bastante propensos à problemas com temperatura

### Cluster de alto desempenho
- aplicações exigentes em processamento
- rapidez
- resultados em tempo hábil
- processamento no talo
- todo o recurso computacional pra resolver a tarefa assignada

### CLuster de alta disponibilidade
- sempre estar disponível para uso
- 99.99% disponível no ano
- ele pode ter variação em seu desempenho durante o período de tempo ligado
    - a única necessidade é sempre oferecer acesso

### Cluster de balanceamento de carga
- mais comuns
- distribuir tarefas uniformemente
- fazer tds os computadores atenderem e executarem
- ERP
- geralmente tem um *buster* de balanceamento por baixo
- divide as tarefas baseado nas capacidades das máquinas presentes no cluster e dividir de forma proporcional

### funcionamento de cluster
- composição de hardware normal
- com nós compartilhados o cluster está disponível enquanto n tiver outra tarefa
    - ao invés de ficar osioso ele é utilizado por algum lugar ou alguém
    - geralmente geograficamente distribuído
    - máquinas podem entrar e sair
    - nunca se sabe a capacidade total verdadeira
- nós especializados só tem máquinas dedicadas àquele cluster
- dá pra ter mais de um OS (nós compartilhados) mas é mais complicado de delegar as tarefas
- precisa de um middleware de gerenciaento (camada) - enxerga tds os nós como uma massa de processamento
- MPI (Message Passing Interface)
    - Mecanismo básico de *Sockets*
- middleware fica no nó mestre e o ostros tem demons de monitoramento

### CLuster Beowulf
- NASA, 1994

- MOSIX
    - UNIX e Linux
    - dá suporte pra GPUs
    - permite heterogeneidade
- faz uma diferenciação de máquinas com GPU e somente CPU
    - middleware não aleatoriza suas decisões
- OpenSSI
    - ambientes Linux
    - entrega uma visão única de uma grande máquina virtual
    - alto desempenho e disponibilidade
- Kerrighed
    - parece um SSI

### vantagens e desvantagens
- bom custo enefício
- n precisa depender de só um fornecedor (supercomputadores dependem da manutenção de apenas um fornecedor)
- facilmente escalável
- bem customizável
- FPGA - hardware reconfigurável - precisa reconfigurar pra atuar como diversos tipos diferentes de componentes
    - processadores são acoplanos nisso aqui
    - dependendo da demanda ele reconfigura o hardware pra atender melhor os tipos de aplicação
- difícil das máquinas estarem geograficamente distribuídas
- se a rede é ruim o desempenho cai
- cluster n é a solução pra tudo
    - Hash n se usa cluster pro exemplo

# Virtualização

## Máquinas virtuais
- usa os recursos da máquina hospedeira
- pode ser outro OS - elas são isoladas
- compartilhamento de recursos

### hipervisor tipo 1
- software implementado no bare-metal em cima do hardware
- em cima ficam as máquinas virtuais
- sem oS na máquina Host
- implementado em alguns clusteres
- kernel da VM passa pelo hypervisor
- complexos de configuração

### hipervisor tipo 2
- funciona em cima do sistema operacional da máquina
- VM's rodam aqui por cima
- podem ter OS's diferentes

### Contâiners
- funções simplificadas de kernel
- permissões diferentes
- implementação leve de uma VM
- ganha bastante espaço no OS
- Docker
    - manipulação de contâiners
- Kubernets (K8s)
    - gerenciamento de contâineres
    - escalonamento
    - contâiners funcionam como clusteres
- é insatalado e já pode sair rodando


### Referências
- D. A. Patterson e J.L. Henessy, Computer Organization and Design: The Hardware/Software Interface, Morgan Kauffman, 5° edição, 2013.