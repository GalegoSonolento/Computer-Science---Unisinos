AWS course: https://awsacademy.instructure.com/courses

DATA: 04/Agosto/2025

# Course details, presentation, general information and project definition
Pretty much a presentation class - not much to see here

Não sei qual vai ser a linguagem geral dessas anotações já que a aula e os materiais são todos em inglês, mas isso vai acontecer naturalmente conforme passa o tempo.

Isso aqui vai ter um trabalho em grupo - junto com o Schulz - que vamos precisar montar alguma aplicação de Cloud - preciso ter alguma ideia rápido pra montar isso aqui - o desenho e monragem vai ser totalmente baseado no que pensarmos em fazer. Vai ser mais ou menos um mês pra montar tudo.

A cadeira vai ser toda em inglês, mas sempre tem aquele jeitinho - também vamos precisar estar por dentro dos cursos de AWS - não deve ser mto complicado.

# Cloud Computing Overview
- O conceito de Cloud utiiliza bastante máquinas virtuais
- a moral é, ao invés de utilizar a máquina (servidor) toda (poder completo) usar partes dela apenas (múltiplos "servidores" virtuais - virtualizaćão)
- servićos cloud de verdade permitem variabilidade de usos
- principal vantagem é de fato não precisar administrar o próprio servidor
- Cloud services são normalmente referenciados como SaaS - Sofware as a Service - Software como Servico
- algumas empresas usam o termo IaaS - Infraestructure as a Service - Infraestrutura como Serviço - mas nesse nível elas já oferecem muito mais que uma plataforma comum e usualmente entregam segurança e cursos
    - PaaS - Platform as a Service - Plataforma como Seriço também é um termo utilizado
- no fim das contas, é tudo *utility Computing*, nós, meros mortais, usamos a *public cloud*, enquanto empresas grandes podem se beneficiar de uma *private cloud* específica para eles.

DATA: 11/Agosto/2025
# Cloud Computing definition, deployment, types and applications
- Cloud não é novo, só uma esquematização nova de transação de dados
- usuários são todos chamados de tenants dentro do mundo cloud
- cloud ainda precisa de servidores físicos pra rodar (tudo servidor Linux)
- clouds privadas são consideravelmente mais caras
- existem alguns poucos players no mercado
    - a manutenção é bastante cara
    - a amazon lidera por ordens de grandeza
- na américa do sul normalmente os data centers são localizados em São Paulo e Santiago (Chile)
- User-facing applications -> Quality of Service (QoE) - performance is key
    - some streaming use UDP to share the files
- Inward computation
    - VM's coupled when on the same application
    - without user interaction
    - more powerful computer
- aplicações de cloud precisam de mais níveis de segurança
    - além da necessidade de gerenciamento de memória
        - não mais pra evitar overhead, mas pra gastar menos
- Service Level Agreement (SLA) need to be guaranteed by the provider -> this can make a difference between selling or dying
- a grande parada disso aqui é poder ter uma alteração no uso (e na capacidade)

DATA: 18/Agosto/2025
# Clouds and data centers, Data center topology, Novel topologies, Network expansion, Types of traffic, Routing and Addressing
- not all DBs/datacenters are cloud
    - but they're still the ones that hold Cloud
- 1 cloud can be composed of several datacenters
- bigger cloud providers have warehouse-scale datacenters knowledgment
    - this is a concept that got more popular recently.
- the topology begins at the servers, passes through Access (ToR) switches, than the aggregator switches, and then the core (core switches), connect several aggregators and admin the payouts
    - DCN - Data Center Network
    - several paths available between physical servers
- as the data goes up (to the root - source switches), the bandwidth diminishes
- oversubscription is a concept that the racks need to have 1:240 bandwidth when compared to the core
    - this might break systems
    - resources eventually get fragmented and spread to different regions
    - this makes process and access slower
- servers are easier to customize than switches
- we should aim to minimize inter-datacenter comms (East-West)
- Cloud is too powerfull for current statistical multiplexing codes we have today
    - many servers share the same hardware (logically separated)
    - this can impact security and performance
- there are multiple physical paths in the network
    - Equal-Cost Multi-Path (ECMP) - spread traffic among paths with the same costs - layer 3 (OSI)
    - Valiant Load Balancing (VLB) - randomly selects the next router - layer 3 (OSI)
- the logic of net in data centers is LAN
    - VLANs can isolate and create more addresses for the VMs (each one needs one IP), but are restricted to 4096 VLANs (not a lot, really)
- Ossification - it gets pretty difficult to change protocols in Network layer
    - Internet is old already, it's hard to make config changes effectively

DATA: 25/Agosto/2025
# Developing applications for cloud computing – Part 1
- No upfront investment in infraestructure
- Potential of software dev cost reduction
    - hardware no longer necessary
    - everything is pay-per-use / pay-per-view
- 