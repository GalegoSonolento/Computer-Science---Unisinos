DATA: 27/Fevereiro/2025
# Revisão de banco de dados
- modelo conceitual é o mais abstrato
    - lógico e físico falam de tables e entidades
- não-relacionais falam de documento
    - relacionais falam de colunas
- ralacionamentos
- concetual pro lógico cria tables
    - álgebra relacional é a implementação base do banco (comercialmente conhecido como SQL)
- SGBD (Sistemas de Gerência de Banco de Dados) - coleção de dados
    - File system bonita
    - ainda é uma coleção de arquivos (só é diferente)
    - SQLite é um arquivo só
    - HANA DB é distribuído por exempl
- um banco de dados pode ter diversos schemas para módulos diferente 
    - até na mesma aplicação!
- aplicações maiores tem diferentes versões
    - diferença de recursos
    - os melhores são pagos (e.g. Oracle Enterprise)
        - aplicaçoes mais cara permitem Clusters por exemplo
- DBs surgiram pq manter tudo na mão em arquivos é muito trabalhoso
    - Excel é um meio termo disso
    - Excel ainda é muito interessante como um export
- DB à nível de RAM é uma coisa mais recente
    - DBs tipo Redis auxiliam a manter cache em RAM pra consulta
    - buscas mais rápidas que acesso à DB
- dados não-estruturados são lidos como *streams*
    - pode ser transformado em dado estruturado posteriormente
    - pode ser usado em aprendizado de máquina
- semi-estruturados apresentam diversos tipos de schemas e tem uma relação mais ou menos relacional (muita vezes não-coerente)
- estruturas ANSI-SPARC dá preferência pra dados de disco distribuídos para evitar problemas
- VDL - criação de *views* - queries prontas
    - chamar uma view é muito mais rápido que um select
    - chace dentro do DB
- dá pra ter várias camadas dentro do banco
    - N camadas
        - hoje é normal Front-end e Back-end, uma com cada DB e um middleware
        - podem existir mais subcamadas
    - pode servir como questão de segurança
- no final das contas, um banco de dados é um grande arquivo (ou vários arquivos) que salvam dados e permitem um controle maior de quem os acesso e como informações são dele retiradas - ele evita problemas de integridade e outros básicos como a condição de corrida (*deadlock*).
- 

# Serviços de um SGBD
- a hora de um DBA é cara pq bancos relacionais corporativos oferecem muitos serviços (mas o trabalho principal é gerenciamento)
- redundância precisa tolerar falhas mas não pode afetar o processamento do DB
- bloqueio de recursos é importante (*lock*)
    - evitar *deadlock* é um dos pontos cruciais de OS também
- ou tudo acontece ou nada acontece em um script de DB
- backups **quentes** são com o banco funcionando comercialmente (maluco)
- controle de integridade é importante
    - não é por que não é relacional que é a casa da mãe Joana

# Introdução ao Processamento de Consultas
- Análise de custo dos queries e consegue mostrar onde a consulta está com dificuldade
- o banco de dados pode fazer uma otimização sozinho
- existe uma tradução interna no banco pra uma visão diferente
    - novas execuções rodam mais rápido
- queries no geral seguem padrões ANSI
    - poucos bancos tem estilos proprietários
- DB mostra a quantidade de tempo que o banco leva pra aplicar os filtros (e.g. where clauses)
    - planos de queries mostram gargalos

# Otimização e Estratégias no Processamento das Consultas
- indices são ótimos mas não são balas de prata
    - consultas se benficiam
    - podem tornar inserções mais pesadas
- em IOT, outras soluções mais bem montadas para INSERTS são melhores (REDIS cai por terra)
- Oracle ainda é a melhor em alterações de disco 
    - provavelmente pelo fato das paginações e gerenciamento de cache
    - com discos precisamos diminuir a utilização dos mesmos
- bancos de dados transforma o SQL (comercial) pra álgebra relacional interna
    - entrega a equivalência menos custosa
- muitas vezes quantidades de registros e número de tables variam a efetividade
    - particionamento interno dos dados pra acesso mais rápido é bastante raro nos DBs
- ao fazer qql query mais complexa, analise o banco de query para ter mais informações sobre como o DB está rodando aquela query em específico
- views guardam as consultas mais utilizadas para retorno mais rápido dos dados
- backups frios são normalmente feitos em fita magnética (incrivelmente mais segura)
- A estrutura de armazenamento 
- HASH e HEAPS são usados aqui também
    - HASH muito usado em Blockchain
        - um bloco aponta pro outro com HASHES - segurança
- 




### Perguntas
- SAP HANA tem plano de avalização proprietário?
Sim, em geral os bancos de dados possuem pelo menos o que se chama de “execution plan”, para mostrar os custos de cada parte da query.

- Redis é uma boa engine de DB ainda
Sim, Redis é muito utilizado, diria até que a grande maioria das empresas que utilizam soluços de cache atualmente usam o Redis.

- O que é o Cloud BigTable?
É o banco de dados do Google, que funciona em cloud, e é muito utilizado como motor de busca.

- a equivalência menos custosa é necessariamente a mais rápida?
Sim, pois o caminho para se chegar ao dado é menor, além de evitar problemas de concorrência como  deadlock.

- view substituem a lógica de partições internas da table?
São conceitos independentes, views são consultas prontas, enquanto o particionamento interno de tabelas serve para buscar os dados mais utilizados mais rapidamente.

- gravação em fita magnética ainda é a mais segura?
Sim, é uma das formas mais seguros para armazenamento de dados offline e de longo prazo, além do custo-benefício, mas é possível também gravar em HDs e na nuvem, todavia, por exemplo, um cartucho de fita magnética moderna consegue armazenar muitos terabytes por um preço muito baixo em relação a um HD ou nuvem.

- como funciona um banco de dados inconsistente? porquê vale a pena?
Vamos falar mais sobre isso nas próximas aulas, mas adiantando o assunto, em geral os banco nosql privilegiam e priorizam mais o armazenamento em memória do que tanto em disco, por isso se chama eventualmente consistente, pois o dado pode estar na memória e não foi pro disco ainda, então existe o risco (pequeno mas existe, principalmente em cluster), por outro lado a performance é muito maior.

- Referente ao trabalho do semestre, serão 15 de apresentação + 5 para perguntas (totalizando 20min) ou teremos 15 e, desses, 5 serão para perguntas (então teríamos 10min para apresentar o trabalho)?
Total de 20 min (15 min de apresentação + 5 min de perguntas).

- JDBC ou ODBC são drivers de conexão que utilizam determinadas arquiteturas, certo? Por exemplo, uma aplicação Java rodando um banco Oracle utiliza ODBC e outra em Java rodando HANA utilizaria JDBC, certo? Ou esses drivers podem se comunicar e funcionar indiferente do banco e da aplicação?
Sim, são drivers, utilizados nativamente (ODBC) ou por máquina virtual (JDBC) para habilitar a aplicação “conversar” com o banco de dados, de acordo com a versão do banco e até do sistema operacional.

- Como a rede se comporta nos casos de acesso ao servidor e como a aplicação (BD) deveria se comportar? Ela pausa todas as operações para poder concluir a viajando pela rede?
Não sei se entendi bem a pergunta, mas nós vamos ver nas próximas aulas como é percorrida a comunicação até encontrado o dado e retornar.

- Caso tenhamos uma rede muito longa e muitos acessos à um determinado banco, mesmo que tenhamos o Redis para cache, isso significaria lentidão do sistema como um todo?
É preciso analisar cada caso, mas em resumo o Redis evita o acesso ao(s) disco(s) onde estão armazenados os dados, então ele encurta o caminho digamos assim.

- A ordenação de execução de operações é sempre a mesma? No sentido da álgebra relacional. Ou ainda temos alterações com outros tipos de banco (i.e. não-relacionais)
A ordenação pode ser diferente sim, há vários algoritmos e cada banco de dados pode implementar diferente, nós vamos ver esses algoritmos nas próximas aulas.
 
- Qual a diferença da fita magnética para o disco magnético?
Na fita magnética os dados são armazenados sequencialmente ao longo da fita, em faixas paralelas. Já o disco magnético funciona como um HD, com os dados armazenados em trilhas, divididas em setores, assim o acesso pode ser aleatório, o que torna mais rápida a busca, por outro lado é mais caro que fita magnética. A fita magnética é mais barata por terabyte armazenado, normalmente é utilizada para armazenamento de longo prazo.