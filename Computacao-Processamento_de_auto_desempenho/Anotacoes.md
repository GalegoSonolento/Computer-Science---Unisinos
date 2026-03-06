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
    - COMA - Cache-Only Memory Architecture
        - máquinas de cluster
        - acesso restrito às memórias cache
- cache e replicação funcionam superbem quando a maioria das operações são de leitura