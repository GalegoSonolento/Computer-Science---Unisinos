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
- 