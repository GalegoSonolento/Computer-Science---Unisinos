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