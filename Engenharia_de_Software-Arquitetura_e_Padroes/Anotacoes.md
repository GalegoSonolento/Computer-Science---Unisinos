DATA: 26/Fevereiro/2025
# Engenharia de Software
- termo antigo e um termo guarda-chuva
- maioria dos conceitos é da OTAN e baseado em aplicações militares
- Margaret Hamilton montou o software da Apolo 11
    - com tolerância a falhas e absurdamente gigantesco
    - uma das primeiras a cunhar engenharia de software
- segurança da informação é parte integral da engenharia atualmente
    - SQL injection
- SWEBOK é o livro de guidance da eng de software e entrega algumas guias
    - não entrega processos completos
- segundo o CHAOS report de projetos de software, apeas 30% são completamente bem sucedidos
    - alguns requerimentos mudam pelo caminho
    - esquemas mais recentes normalmente estão abordando diversas entregas e projetos quebrados e integrados posteriormente
- ainda existem problemas apesar de todos os frameworks montados
    - pessoal errado nos times errados
    - fatores humanos
    - alterações de ambiente
    - usuário fora do ciclo de desenvolvimento

## Arquitetura de software
- entrega uma estrutura para o software
- o planejamento da construção do código fica aqui dentro
- projetos mal feitos entregam soluções não escaláveis, difíceis de dar manutenção e funciona mal
- muito da arquitetura se coloca em modularizar o código e dividí-lo entre os serviços necessários
- pensamento macro de componentes
- onde está e o que está no que são serviços completamente diferentes dentro da arquitetura
- se todas as aplicações conversam com todas a arquitetura está mal feita
    - sobrecargas e carregamentos de apenas um componente (sem hierarquia) formam arquiteturas malfeitas
- arquitetos normalmente são pessoas sênior
    - pessoal de desenvolvimento q sabe mais ou menos como implementar
    - ajuda na hora de entregar os prazos
    - custa CARO
- 

### O que é estrutural em uma casa?
- fundação
- coluna
- viga
- pilar
- parede
- chão
- estrutura do teto
- aberturas
- fusível

### Desenhando uma arquitetura
- precisam ter vários compoenentes
- sempre vemos todos quando montamos o software
- tds tem papéis específicos

DATA: 08/Março/2025
# Dimensões da Arquitetura
● Características arquiteturais
– Esta dimensão descreve quais aspectos do sistema a arquitetura precisa suportar:
escalabilidade, testabilidade, disponibilidade, etc.
● Decisões arquiteturais
– Esta dimensão inclui decisões importantes que têm implicações significativas ou de
longo prazo para o sistema. Por exemplo, o tipo de banco de dados que ele usa, o
número de serviços que ele tem e como esses serviços se comunicam entre si.
● Componentes lógicos
– Esta dimensão descreve os blocos de construção da funcionalidade do sistema e
como eles interagem entre si. Por exemplo, um sistema de comércio eletrônico pode
ter componentes para gerenciamento de estoque, processamento de pagamentos, etc.
● Estilo arquitetural
– Esta dimensão define a forma física geral e a estrutura de um sistema de software da
mesma forma que uma planta de construção define a forma geral e a estrutura da sua
casa.

Tenha em mente que uma escolha de arquitetura depende de vários fatores para que ela tenha algum sucesso.
Ter qualquer um dos aspectos como garantido pode gerar um gargalo ou até impedir completamente o funcionamento do sistema.
Entenda seu ambiente e trate como tal.

DATA: 12/Março/2025
### Continuação Dimensões de Arquitetura
- atualmente os estilos arquiteturais já estão mais ou menos estabelecidos
- visão de domínio sempre precisa do contexto bem definido
- monolitos são mais simples de entender, desenvolver e fazer onboard
    - infraestrutura é mais simples
    - comunicação é toda interna
    - a confiabilidade é maior por ser uma comunicação totalmente interna
        - ao mesmo tempo que ela pode ser baixa - se o sistema cai ele cai completamente
    - alterações, escalabilidade e evolução desse tipo de sistema é muito mais complexa
- o modelo distribuído trabalha nos *pain-points* do sistema monolítico
    - testabilidade, tolerância, escalabilidade, modularidade e implação são todas ridicularmente mais rápidas
    - mantendo a mesma interface de comunicação entre os sistemas, o teste e alterações são absurdamente mais ligeiras
    - menos performance 
        - o fator rede (latência, disponibilidade, etc) atrasam o processamento
        - muito mais rápido usar recursos do mesmo servidor
    - depuração e manutenção é bem mais difícil
        - sistemas diferentes comunicam diferente e tem processos de *troubleshoot* diferente

# Estilos arquiteturais
- usar a mesma solução sem contexto não faz sentido
- Camadas
    - MVC
        - Model View Controler
        - padrão de projeto
        - não necessariamente precisa apresentar pro sistema inteiro
    - diferentes tipos de arquivos e processos
        - não necessariamente microsserviços
        - camadas diferentes simulam diferenças físicas
        - ainda pode ser monolítico
    - sistemas web normalmente utilizam 3 camadas
    - dispositivos móveis normalmente tem pequenos bancos de dados junto do celular
        - SQLite ou No-SQL
    - é bantante complexo manter um sistema em camadas puro
        - novos membros precisam entrar na arquitetura
        - sem bloqueios forçados é mais difícil ainda
- monolito modular
    - **não é** todos falando com todos
    - basicamente microsserviços mas tudo no mesmo servidor
    - dentro de cada módulo (negócio) dá pra fazer todas as camadas MVC (técnicas)
- microkernel
    - principal caso são OS'
    - alguns apps desktop usam
    - *core* é um software com o mínimo de funções vitais
        - o resto é plugin conectado no microkernel
        - integração à nível de código mesmo
    - o kernel passsa serviços
        - chamadas, conexões, etc
        - maioria é solicitação (kernel não pede muita coisa)
- serviço é toda e qualquer funcionalidade do meu software que outro pode pedir/usar
    - o microsserviço tem uma responsabilidade menor que o serviço e pode ser, por exemplo, um  parte de um serviço maior
- todo microsserviço é dono do próprio dado
- microsserviços
    - precisa ser coeso e responder direito
    - precisa conseguir cumprir com suas responsabilidades
    - monitoramento e identificação de trechos mais utilizados que outros é bastante importante
        - trechos maiores e mais utilizados podem facilitar a vida
    - funções críticas separadas permitem mais estratégias e padrões de projeto
        - redundâncias nesses serviços e tolerância a falhas
    - por mais de se quiser separar - para manter integridade - é necessário juntar serviços
    - dados dependentes faz valer a pena fazer um microsserviço maior
    - serviços que sempre usam outros sreviços ou que sejam usados juntos
        - é interessante juntar e manter a orquestração *in-house*
- decisões de negócio normalmente valem mais que as técnicas
- Orientada a eventos
    - EDA
        - Event Driven Architecture
    - serviços apresentam e lançam um evento - quem precisar fazer uma ação vai realizar uma ação
    - serviços lançam eventos e não esperam por nenhuma confirmação
    - comunicação paralela e assíncrona
        - existe a possibilidade das respostas não chegarem ao mesmo tempo
    - os serviços que recebem podem falhar outros serviços precisam escutar e fazer o necessário
    - tudo é publicado como evento - sem esperar resposta
- à depender de quem fala mais alto (implementação ou negócio) teremos diferentes montagens e esquematizações de produto
- normalmente dispositivos móveis precisam de soluções embarcadas
    - nunca se sabe quando aquele dispositivo vai ficar sem internet
- se vamos aumentar ou diminuir um microsserviço depende bastante da granularidade que queremos com aquele determinado serviço e se faz sentido mantê-lo quebrado ou não 
    - serviços que sempre funcionam juntos podem ser, bom, juntos em um único serviço para evitar complexidade
    - ao passo que um serviço grande que só tem uma parte do código utilizada em casa chamada, pode ser quebrado em 2, por exemplo

DATA: 19/Março/2025
### Continuação estilos arquiteturais
- Peer-to-peer
    - sistemas mais específicos
    - desenvolvidos
    - todos os clientes são servidores
    - descentralizado - completamente
- pipe N' filter
    - sistema tem várias fuções quebradas (filtros)
    - entram num pipe e passam por uma sequ~encia de funções
    - filtros são autocontidos
        - bastante claridade
    - processamento de texto usa arquitetura em filtros
    - com muitos passos encadeados compromete desempenho
    - fluxos complexos dificultam a manutenção
    - sistemas desktop são mais comuns
- Blackboard
    - repositório de dados compartihados
        - entre os programas todos
    - pedaços de aplicação que colaboram para determinado resultado
    - manpulam os mesmos dados
        - é uma *pool*
    - coordenar todas as funções é complexo
    - troubleshoot de origem é complicado
- Pub/Sub
    - publish / Subscribe
    - subscribers ficam observando quando algum publisher larga uma e responde
    - mais liberdade que o orientado a eventos
- MapReduce
    - mapeia dados de entrada
    - jogam num Hash e consulta em uma lista menor
    - esse mesmo esquema é utilizado pra compressão de aruivos
- Broker
    - mediador de comunicação
    - sair do problema do pub/sub que não sabe quem recebeu de verdade
    - armazenamento temporário

# Notação e Documentação
- as pessoas não lembram o que elas fazem
- decisões impactam o desenvolvimento do sistema    
    - informações importantes e porquês precisam ser anotados para o bem do projeto e evitar esquecimento

## Trade-off
- decisões que precisam de análise de todo o contexto
- facilita um lado e dificulta o outro
- uma troca entre positivos e negativos
    - ganhar em um lugar e perder em outro
- é uma gangorra
- os mais significativos são de arquitetura

## Como documentar?
- UML ainda é bastante utilizado
    - tem uma porrada de modelos
- deve ser uma referência pra equipe toda
- dá pra mostrar o funcionamento completo de um serviço usando um diagrama de sequência

## Architectural Decision Records (ADR)
- descrição de uma arquitetura específica
- decisões arquiteturais
    - baseadas nos requisitos 
    - guarda descartes
    - pode ser alterado dependendo de mudanças de contexto
    - precisa descrever mudanças, por quês e padrões e decisões
- documentar o motivo de algo ter sido abandonado é importante pra evitar voltar pro mesmo lugar

DATA: 2/Abril/2025
# Padrões de Projeto
- padrões espalhados por diversas aplicações
- existem diversos padrões de projeto prontos
- não tem pq reinventar a roda toda vez que implementar algum software
- padrões de projeto são cobrados em entrevistas técnicas bastante
    - alguns softwares precisam manter esses padões para evitarem um código macarrônico
- padrões de projeto são absolutamete práticos
    - uma ideia de uma solução
    - não existem códigos prontos
    - a implementação varia
- algoritmo não é um padrão de projeto
- aprender os padrões é importante para entender a fluidez e manter uma linguagem comum entre os desenvolvedores
    - o desenvolvimento de uma linguagem comum, **jargões** são comuns em diversas profissões
- esses padrões são catalogados em linguagem padrão nas linguagens
- o foco deve ser em problemas novos - padrões já descobertos estão para usarmos
- ter uma variável global com mudanças dentro do código é complicado
    - mas variáveis globais ainda são úteis se temos algum valor constante
    - tipo a gravidade (9,8 m/s)
- ideias e implementações precisam nascer com a ideia de padrões 
    - é como se fosse um reflexo de exercícios
    - na loucura do dia a dia é necessário ter pensamento rápido com os padrões para a implementação

# Anti-partterns
- *balas de prata* comuns em códigos que não são exatamente as formas mais eficientes de resolver um problema
- são implementações legado que vão ficar infinitamente 

DATA: 09/Abril/2025
# Padrões para Aplicações Corporativas
- Soluções arquiteturais para empresas
- mesmo pique dos padrões normais
- é complixo desenvolver hoje em dia
- alguns problemas clássicos vêm de bancos relacionais colocados em codigos OOO
- DTO - Data Transfer Object
- em aplicações web é importante ser eficiente
    - dá pra carregar objetos nã completamente

# Frameworks e bibliotecas
- o objetivo dos frameworks é trazer uma implementação pra atacar problemas semelhantes
- pedaços prontos de aplicação
- sempre flexíveis e extensíveis
- precisa ser fácil de usar
- frameworks controlam aplicações
    - ele te permite só preencher os espaços
    - desenvolvimento mais rápido 
- bibliotecas são soltas e trazem diversas classes
    - não tem modelos, só as funções prontas
    - catálogo de uso
    - 