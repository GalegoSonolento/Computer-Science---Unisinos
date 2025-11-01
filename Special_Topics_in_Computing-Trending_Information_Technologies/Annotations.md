AWS course: https://awsacademy.instructure.com/courses
Main bucket name for Development course: haaghenrique
API invoke URL: https://nclcd1mbii.execute-api.us-east-1.amazonaws.com/prod

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

DATA: 8/Setembro/2025

c169845a4385584l11609860t1w7303351928-samplebucket-ktfas1heh5f2
aws s3 cp list-buckets.py s3://c169845a4385584l11609860t1w7303351928-samplebucket-ktfas1heh5f2

DATA: 15/Setembro/2025
# C4 model
- diagrama de engenharia de software
- esquematização do software pra construí-lo posteriormente
- nessa altura do campeonato mapear os serviços utilizados e interações é o importante
- tem um bom exemplo na página relacionada nas notas da aula
- describe business problem
- specify architecture or deplyment
- diagram must have cloud services utilized
    - how the service interact with one another
 
DATA: 06/Outubro/2025
# Cloud Security Fundamentals
- Infomration security is often times mislead or misinterpreted
- According to ISO 27002, information security is the protection of information against various types of threats to ensure business continuity, minimize risks, and maximize return on investments and business opportunities
- confidentiality, integrity and availability are the main concerns of information security
    - as this is a triangle, you can see that this might be an issue to have them 3 at high, at the same time
- computer, storage and networking assets - they need availability and are all proon to fail
- Man-in-the-Middle attacks are very easy to do and useul
    - problem is to know where the information is passing through
- security is the protection against external attackers and information integrity
- privacy is the end user's right to control their personal information

DATA: 15/Outubro/2025
# Accesss Control and Identity Access Management
- every system should be using the minimal access approach
    - only assign the accessess a user really needs
    - asssigning extras is a ssecuriy risk - even if the authentication method is good

DATA: 20/October/2025
# Data Security
- Data must be encrypted while navigating on the Internet, sending plain text is problematic
- AWS and other cloud services can generate this for teh users (always best to have your own)
- Data accountability on cloud is important
- There's a difference between data in transit and data at rest
    - it's usually easier to catch data in transit if there's no effective encrypting.
- one of the solutions recently found was the AWS KMS - for key management
- client made keys tend to be safer in general
    - server application does not has both key pairs
- 