Alguns do conteúdos (ainda mais os textos grandes em outros arquivos .txt) podem ter sido gerados por IA porque 1) po é muito texto e 2) o NotebookLM do Google é bastante competente no que ele faz e faço os testes dele com frequência - eu ainda tomo muitas notas em papel, então n enche meu saco.

- Apautação
- Avaliação
- PAD
    - História
    - Von Neumann
    - Memória
    - Barramento
    - Pipeline

- i386
    - cisq
- com mais cores o clock precisa ser reduzido
    - Power wall foi em 4GHz +-
- memory wall reflete a diferença entre acesso de memória e processamento
    - leitura/escrita no HD - memória não-volátil é bastante mais lenta
- o game changer é o barramento entre o processador e as memórias
- O grande problema de PAD é dinâmica de fluidos
- HPC -> High Performance Computing 
- Escalabilidade: manter a mesma qualidade de serviço aquém da demanda enviada à ele
    - QTOS!
- não dá pra fazer computador sem cache
    - diminuição de gab entre processador e memória
- AMD e Intel sabem fazer até 512 cores - não temos
    - Gargalo de Von Neumann impeded
    - 128 cores no mesmo barramento precisam do Juiz - não vale a pena
    - Browser é quem mais usa paralelismo (web-sockets)
    - Sem demanda de verdade
- 


Achar a "Equação Internacional". Dada uma aplicação com i interações, e estágios e o tempo de estágio em n, qual é o tempo t para execução desse programa
T = ((i + e) - 2) * n

05 de Março de 2025
# Paralelismo no chip
- máquinas hyperthreading - TLP - instruções de programas diferentes pra execução por clock
    - tem problemas pra aplicações singulares
    - Multi-core -> toda máquina multicode é um TLP
- aplicações monocore serão prejudicadas por TLP (execução com ILP pode potencializar)
    - competição por recursos escassa
- computadores têm configurações diferentes de TLP dependendo dos usos
    - multicores caros tem mais unidades funcionais
        - diferença entre chip caro e barato
- Intel e AMD checam estatística e montam o acesso variando com o uso
- busca de mais instruções por programa (thread) - competição de recursos
- Hyperthreading - TLP - replica registradores
    - gargalo serão recursos compartilhados (e memória funcional)
    - 1 core físico e dois ou mais virtuais
    - Circuito integrado (CI) menor e compartilhado
        - menos calor e consumo de energia
- SMP - Simetric Multiprocessor - Multiprocessador Simétrico
    - mundo paralelo com diferentes CI - mais quente e caro
    - gasta mais silício
    - histórica
    - dual ou quad-prcessor (em contrapartida em hoje sendo dual ou quad-core)

# Aplicações paralelas
- com imagem, por exemplo
    - larga um quadrante/bit/etc pra computar multicore e devolver mais tarde
    - sincronismo bastante delicado
    - dependência (tem relações com  DAG)
        - sempre trava computação
    - Balanceamento de carga
    - Deadlocks
        - qunado não paralelizar
- existe uma quantidade ideal de recursos para uma construção
    - analogia do muro
        - 1 pedreiro = 30 dias
        - 2 pedreiros = 22 dias
        - 4 pedreiros = 16 dias
        - 8 pedreiros = 12 dias
        - 16 pedreiros = 20 dias
        - análie de dependências
- existem programas ainda que são melhores sequenciais
- **Lei de Amdhal**
    - speedup
    - Sp = ts/tp - tempo sequencial dividido por processadores
- a partir disso dá pra ver a metrica de eficiência
    - consumo de energia

# Arquiteturas paralelas
- **classificação de Flynn**
    - SISD, SIMD, MISD, MIMD
- Multiprocessador/multicore - memórias compartilhadas
    - várias threads
- Multicomputador -> clusters
    - comunicação é por rede e sockts
    - vários processos em pcs diferentes
- organizações de memória
    - UMA - Uniform Memory Access
        - todos os cores no mesmo barramento na mesma memória
        - computador Default
        - acesso com o mesmo tempo
        - árbrito de acesso à memória
    - NUMA - Non-Uniform memory Access
        - acessos em tempos diferentes
        - Espaços de endereçamento
        - acesso mais rápido em alguns trechos
        - o interessante é ter um bom compilador aqui
        - o benefício é o paralelismo de acesso de memória
        - precisa de um compilador top de linha
    - COMA - Cache-Only Memory Architecture
        - máquinas de cluster
        - acesso restrito às memórias cache
        - basicamente não existe mais
    - NORMA
        - ambiente multicomputador
        - NO Remote Memory Access
- cache e replicação funcionam superbem quando a maioria das operações são de leitura
- MIMD - top de linha multicore e computador
- SIMD - GPUs
    - CUDA
    - OpenCL
- Multicomputadores
    - NOW - Network of Workstations
        - baixo custo
        - computadores interligados
        - catapultada pela Ethernet - sim, o cabão de rede
            - 16 Mpbs
    - COW - Cluster of Workstations
        - NOW forte
        - Hacks
        - espaço pra máquinas dimensionado em U (U's)
        - uso exclusivo
        - NIC - Network Interface Card - placa de rede
        - Switch interno pra toda a configuração de rede
        - clusters homogêneos são perante aos nós
            - nós de processamento iguais
            - heterogêneo é o contrário
    - Cluster computer
        - um conjunto de máquinas normalmente homogêneas ligadas por uma rede dedicada para uma tarefa em comum
        - instação por PXE - todas as máquinas precisam ser iguais
        - KVM - plataforma com um monitor teclado video e mouse
            - digital
            - dá pra selecionar a máquina do cluster e não jogar um VGA em cada máquina
        - NIS - Network Information System - evitar incompatibilidade
        - NFS - Network File System
        - SSH - trabalhar na porta 22
            - Substitui o telnet
            - criptografado
            - SSH sem senha
                - depois do primeiro login, já dentro do cluster
                - SSH sem senha pros nós
                - chaves públicas e privadas
        - Pthreads e MPI
        - Resource Ger
        - depuração de código em sistemas paralelos é mais complexo
            - sem debug
            - mas tem geração de rastros de processos
            - coloque os rastros em uma tool de visualização
            - análise sempre post mortem - Pajé
- Cluster - reprodução de resultados e exclusividade
    - pode usar o cluster do PPG inclusive (fala com os caras)
    - o gerenciador dá as máquinas exclusivamente (mais ngm pode fazer SSH nas máquinas)
        - se elas forem iguais também -> validação científica
    - reprodução de dados validada
- **Grid computing**
    - 86 - ethernet
    - cluster que não precisa estar necessariamente dentro da minha empresa
    - rede mais ampla de computadores
    - conexão de laboratórios
    - não vingou mto no começo
    - AWS nasce em 2005 e basicamente **mata** esse processo

# Redes de Interconexão
- Multiplexação é muito importante
    - demultiplexão do outro lado
    - necessário em qualquer meio compartilhado
    - Top - **Temporal**
- Time sharing
- sender rápido e receptor lerdo
- CPU ainda controla o quão rápido o processo de rede funciona (velocidade de rede)
    - rede lerda pode ser CPU no gargalo e/ou processador defasado
- latência é o tempo mínimo de abrir o canal de coms
    - pacote de 0 bites nao tem um pacote de zero bites no final do processo
- CSMA/CD
    - CD -> backof exponencial pra evitar colisões
        - 2^x (x = num da colisão) - escolhe 0, 1, ...x localmente pra tentar enviar de novo
        - Ethernet não é escalável ... com HUB
- tempo de desfazer o processo é infinitamente mais ligeiro do que montar os pacotes
- letência != tempo de comunicação
    - tempo de coms é != de 0 bites (qql coisa)
- 100 bytes (1 latência) != 10x 10 bytes (10 latências)
    - por isso se faz bufferização 
        - algoritmos de Nagle
        - Bufferização de vários pacotes
- Largura de banda
    - B = dados/tempo = Megabits/segundo
    - TPS - Transações por Segundo
    - Fast Ethernet = 100 Megabits por segundo - 100Mbps
    - Jitter
        - Internet da rua é dinâmica
        - controle de Jitter do browser - bufferiza os frames de um vídeo por exemplo   
- Em rede cabeada de cluster, dedicada e de alta velocidade é sereno usar UDP
    - chance de perder pacotes é bem pequena
    - e tem transmissão de dados pequenos (não vai compilar 1 mega de pacote)
    - dado pequeno é de 1 byte até 64MB
- Infiniband é pra resolver o problema da Ethernet ser lenta
    - mta coisa em software no ethernet (TCP)
    - criado em 2003
    - joga tudo na placa de rede
    - uso extensivo de hardware
    - RDMA - inscrição de ponteiro remota - zero copy

# Modelagem de Apliações Paralelas
- Parte mais complexa
- cheque o trecho com mais computação e com mais rotinas (loops)
    - rotinas que podem ser executadas em paralelo são nossas amigas
- dependência e sincronização é o que pode quebrar nossas pernas
- pra saber se vale a pena paralelizar tem q ver a aplicação e a entrada de dados
- Filtro de Mediana - suavização de bordas
- DAG-> Grafo Dirigido Aciclico

# Programação paralela utilizando memória distribuída
- normalmente se aceita o send assíncrono, não o receive (não faz mto sentido)
- MPI usa broadcast com teorías de árvore
- Sincriniazao com barreias
    - vários processos executando - operação coletiva
    - espera todo mundo chegar pra avançar (gargalo)

# Biblioteca MPI
- padrão de código
- número de processo está fora da linha de comando
    - só passa os binários p/s máquinas
- MPI faz bastante parte da comunicação interna dos clusters

```C
#include <mpi.h>
#include <stdio.h>

int main(int argc, char ***argv)
{
    MPI_Init(&argc, &argv);

    printf("Hello, World!\n");

    MPI_Finalize();
    return 0;
}
```

- lógica de código mestre-escravo (if-else dentro do main)

# Computação em cloud e PAD
- conceitos de 1992 -> modelo de pagamento e virtualização são apareceram em 2003
- A diferenciação do cloud vem da elasticidade
    - ao encontro de long running applications -> cloud permite criação de checkpoints e Disaster Recovery
- Temos sistemas reativos (treshholds) e proativos
- temos máquinas verticais (resizing) ou horizontais (aumentando lâminas e recursos)
- fracamente acoplados não geram dependências entre processos
    - bag-of-tasks
    - pipelines
    - divisão e conquista
        - tem bastante o jeito da elasticidade
    - paralelo de barreira
        - problemas levam na barreira
        - diminuir os superprocessos pode ser uma resposta
        - elasticidade não cola mto - talvez migração de processos fosse melhor
            - em runtime
- heurísticas boas de compução e rápidas sao preferíveis
- Alterar a aplicação pra colocar na cloud é melhor se for com o menor nível de esfoço possível
- No kit do AWS o nome disso é lambda
- Programar em Kuda pra cluster é o game
    - n precisa mudar muita coisa pra Cloud depois
- política de escalonamento n tem balanceamento de carga por padrão
    - lançamento de threads -> escalonador do SO -> thread-core
    - lançamento de uma aplicaão MPI -> reserva de recursos (nó) - files.txt -> MPI run -np <x_processos> prog files.txt - processo de mapeamento (round-robin, na maioria dos casos)
- Round Robin
    - mais comum na internet
    - ótimo em sistemas homogêneos
    - pode náo ser o ótimo (na maioria das vezes não é) em sistemas heterogêneos
    - padrão do cloud computing
- ótimo nem sempre é o único escalonamento
- ou o recurso ou o consumidor, ou os dois, serão heterogêneos
- Execução Real Time de uma aplicação de PAD é a soma de 2 tempos:
    - T1 - tempo de escalonamento
    - T2 - tempo de execução
- Escalonamentos -> taxonomia (1988 Casavanti e Coulomb)
    - **local**
        1CPU
    - **global**
        - /> 1CPU
        - **dinâmico**
            - ou não tenho informação da aplicação (tarefas ou recursos)
            - ou elas mudam em runtime
            - **fisicamente não distribuído**
                - multicore
            - **fisicamente distribuído**
                - cluster
                - **não cooperativo**
                    - escalonadores não se comunicam
                    - podem dar overload em um Target sem querer
                - **cooperativo**
                    - checa com os recursos (target) e outros escalonadores - chega se recursos estão overloaded e se comunica com os outros escalonadores
                    - **ótimo**
                    - **subótimo**
        - **Estático**
            - não mudam em tempo de execução
            - podem ser heterogêneos
            - **ótimo**
                - estresso todas as possibilidades
                - **filas**
                - **grafo** - principal
                - **Computação matemática**
            - **subótimo**
                - **heurístico**
                    - bom senso
                    - noção da realidade
                    - sem provas
                    - list scheduling (de escalonamento que faz balanceamento de carga)
                - **aproximado**
                    - vai até um nível x da árvore
                    - pega o melhor escalonamento que achar e usa
- Balanceamento de carga - Load Balancing
    - equilíbrio pros rápidos não fiquem parados esperando os lentos por muito tempo
- Escalonador + LB
    - normalmente eles andam juntos
    - métricas p/ LB
        - CPU (ou load), mem (ou load), rede (latência, banda)
    - vazão - sempre usados
        - dados/tempo
        - de dados, tipo TPS (Transaões por Segundo)
    - Ideia -> somar duas métricas (problema da unidade)
        - uniformização de unidades
    - Síncrono
        - período -> x em x tempo verifica o sistema
        - definição de tempo varia
            - período curto
                - mto overhead
                - alta intrusividade
                - impacto em desempenho normal
            - período longo
                - Perda de reatividade
                - tempo demais no overhead - pouca reação
            - a solução pra esses problemas pode ser uma adaptação do sistema
                - dá um chute do período e progride geometricamente conforme está tudo certo
                    - quando encontra um overload quebra o período em 2 pra aumentar a reatividade até estar tudo certo de novo
    - Assíncrono
        - configura e.g. threshold com regras e ações pra elastiticidade reativa
        - monitoramento é função do programa (backend)

# Migração de processos
- sempre precisa de (Migração do processo) -> necessário pra reescalonamento
    - quando
        - quando se lança o balanceamento de carga?
        - Load Balancers monitoram todos os processos
        - LBs funcionam periodicamente (tempo em tempo balanceia)
        - isso serve como referência se a migração é necessária
        - 1º ⲁ = aposta
            - ⲁ balanceado?
            - Sim, ok
            - ⲁ = ⲁ*2
            - balanceado?
            - não
            - balanceamento executado
            - ⲁ = ⲁ/2
        - o que é estar balanceado?
            - uma das implementações é ver todos os tempos dos processos dentro da superstep e montar uma média - distribui todos
            - indústria - >3𝜎 é problema -> controle estatístico de processo (usado em chão de fábrica pra controle)
            - fora de 3𝜎 preciso balancear
    - quem
        - qual processo trocar?
        - qual vai ter uma melhor alocação de recurso 
            - efeitos de comunicação
                - intra-cluster é muito melhor
            - recurso computacional
            - uma força contra a migração é memória
                - jogar o processo de um lugar pro outro tem custo
                - serialização e revival do processo do outro lado custa bastante
            - PM (i,j) = Comp(i,j) + Comm(i,j) - Mem(i,j)
                - PM = Potencial de Migração
                - i = processo
                - j = cluster
                - avaliação de cada processo para cada cluster
                - os componentes passam por normalizaçõ [0, 1]
                - PM = [-1, 2]
    - onde 
        - máquina de dentro do cluster
        - (1-load) * CPU (teórica)
            - métrica de BL
        - migração acontece justamente quando ninguém tá fazendo nada
    - como
        - Checkpointing
        - espelha o processo em disco e espelha na outra máquina
        - *Modelo/arquitetura/framework vende*
        - o como é a tecnologia - junta os dois é um sistema
    - Problemas?
        - Histerese - problema de a atividade ser ativada várias vezes seguidas
            - é como um eco dos estímulos anteriores, nesse caso, é migrar um processo, rodar a análise de novo, e remigrar o processo pro mesmo cluster q ele saiu da primeira vez
- a ideia é fazer grid de vários clusters
- gerenciadores de cluster
    - BSP + MIP + PThreads
    - modelo de aplicação

# Explorando elasticidade de recursos de computação em nuvem para execução de aplicações de alto desempenho iterativa

# Pthreads e MPI
- Thread pool (com ideia de pipeline)
    - app multimídia (transformadas sequenciais)
- comunicação assíncrona: serve pra mascarar latência de rede

# OpenMP: Programação em Memória Compartilhada
- Pthreads é de 1992 (flexível)
- multiprocessing
- API de C
    - d[a pra baixar a biblioteca]
- diretivas de compilação - PRAGMA - diretivas de computação
- permite gerar código paralelo - mas perde um pouco do controle q o pthreads entregava
- #pragmas abrem as janelas de cod paralelo
- é mais interessante pra execução mas tem o trade-off do controle fino
- variável_de_ambiente
    - bash, linux, etc
    - variável tem um valor
    - programa identifica as variáveis do terminal para execução
- tbm tem inserção de barreiras pra execução
- expansão de região paralela com FOR, por exemplo - executa o for todo em um tick ou itens/cores\processos
- sections são sesçoes que ocorrem em paralelo
- utilidade cresce bastante já q o paralelismo está abstraído - flexível e mais rápido de montar
    - ainda tem algumas idiossíncrasias

# Cuda C/C++ Basica
- SIMD - classificação de FLIN
    - máquinas vetoriais
- programa começa no HOST (CPU), executa no Device (GPU) e fecha no Host de novo
- CPU tem operações lógicas que uma GPU n consegue fazer
- paralelismo de dados
    - for e while
    - trabalhos de vetores e matrizes
- fonte de overhead é entre a CPU Mem e a DRAM
- pra execução em GPU precisa de definição de kernel (que é o que a GPU executa)
- __global__ é indicação de GPU chamada à partir do Host
    - compilador separa as execuções do Host e do Device
- mykernel<<1,1>> -> kernel launch -> com parâmetros definidos pra ele
- a DRAM recebe cópias dos dados pra execução
- codaMalloc aloca memória dentro da DRAM
- gargalo é de fato gerenciamento de memória
- p/ running in parallel precisa de add<<< N,1 >>> - entrega vários blocos pra 1 thread
- threads em CUDA são CUDA Threads
- um bloco pode ter diversas threads dentro dele
- add<<<1, N>>> -> 1 bloco pra N threads

# Convergência HPC-Cloud -> Aproveitamento de desciplina
- microsserviços
- gargalos denotam pontos fracos
- Serverless HPC Computing - eveolução direta do On-Premise
- Win-Zip
    - Lossless - sem perder dados - sai 1Gb e devolve 1Gb
    - pro tempo de compressão é preciso ver o Lossy -> bastante usado pra streaming (compressão não tira dado o suficiente pra que seja perceptível)
        - tem uma ideia de interpolação lá na fonte pra pegar só o absulutamente necessário pra exibir do outro lado (salva banda)
- TCP-IP-Ethernet é maravilhoso pra Software (confiabilidade)
    - infiniband soca tudo do TCP dentro do Hardware
- EdgeAI como Filtro
    - IA na berola
    - tinyML - ML super pequena
    - engg e educação do modelo pra usos superespecíficos
- Estatística (data-science)
- dá pra montar multiplexação entre sockets
    - split de dados pra multiplexação e demultiplexação
- zero-copy network é um trava zap!
    - não dá pra travar usando sockets (mas sim com Infiniband - nível de usuário)
- bufferização é feita pra otimizar latência
    - dá pra desabilitar com flush ou com alg de Nigle
- DNS é útil pra tolerância à falhas
- banco de dados serverless pode ter sharding
- SLM praticamente n tem alucinação
    - foco mto pequeno pra alucinar
- STM32 - ST Microelectronics -> estado da arte pra EdgeAI
- hj mto se pede as IAs explicáveis
- 