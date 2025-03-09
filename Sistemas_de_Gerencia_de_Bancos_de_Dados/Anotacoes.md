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

DATA: 05/Março/2025
# Transações
- inserção e alteração de dados
- conjunto deoperações feitas no modo **tudo ou nada**
    - ou faz todas de uma vez só
    - ou reverte tudo pro estado original
- acontece com duas ou mais alterações
- fita magnética é muito boa, mas tem um acesso sequencial que diminui a velocidade de informação
    - isso é importante pra guardar informação a longo prazo
    - disco também é importante e mais seguro atualmente, mas ainda não ganha da fita pra longo prazo
    - a memória RAM é ainda mais rápida e o Redis é bastante utilizado aqui
        - nuvem, local, etc
        - mensageria e cache (consultas rápidas)
        - evita sobrecarregar os HDs
- backups são sempre feitos em disco por segurança
- RAID - distruibuição de arquivos entre vários discos
    - se um falhar os dados nos outros discos podem reconstruir a parte que falhou
    - precisa de um OS específico para construção de servers
- consistência é o vai ou racha
- transação pode ficar inconsistente
    - quando algum fator externo acontece (e.g. falta de luz) a inconsistência aparece
- COMMIT; server para confirmar uma operação a nível de DB (transação) - permite ***rollback***
- DBs mais famosos são relacionais justamente pela confiabilidade nos dados
    - muitos sistemas corporativos usam DB's e precisam de mais garantia de integralidade que rapidez
    - não necessariamente o mais usado é o melhor
- é mais complexo montar Clouds com bancos de dados relacionais
    - eles são mais lentos
    - não necessariamente compatíveis com as expectativas cloud
- **execuções simultâneas** melhora bastante o tempo de execução
    - vários cores e bastante *output*
- **ACID** é usado em bancos relacionais
    - em hipótese alguma uma transação deve interferir na outra
        - mesmo com paralelismo
    - se desligar e consultar depois o dado precisa estar lá ainda
- O ***failover*** usa a gravação de disco automática e permite dar *rollbacks* pra estados anteriores daquele banco
- ***ghosts*** causam consulta e geração de dados errados
    - acontecem com transações simultâneas
- schdules não podem estar cascateadas (uma dependendo da outra)
    - gera *aborts* em sequência
- leituras nunca geram interferência
    - o cuidado é necessário com leituras e escritas
    - escritas sempre devem ser postas antes e commitadas
- serialização pode ser testado pelo grafo de precedência
    - se quando passar pra T2, voltar imediatamente pra T1, tem risco de confiabilidade de dados
    - isso é um grafo cíclico
        - arriscado pra execução
        - isso é visto dentro do execution plan
    - em grafos acíclicos a ordem de execução é montada em outro lugar e o execution plan toma conta

# Concorrência
- evitar *deadlocks*
- controles de *timestamp* para replicação de dados 
- isolamento é fundamental - é possível com a serialização
    - *serializable* em Java
    - objetos compartilhados na rede como um string gigante
    - mesmo princípio mas com transação
- em DB se faz isso com locks
    - ao final da operação o objeto deve ser desbloquado
    - assegurar serialização e evitar *deadlocks*
- *deadlock* - impasse eterno
    - predições em grafos podem auxiliar no encontro de deadlocks - *loops* no grafo
- serialização tira performance
- árvores B+ -> árvores balanceadas
- existem alguns tipos de isolamento, que permitem performances diferentes
    - da mesma forma que antes, aqui algumas vezes pode ser que o dado não seja 100% coerente
- *starvation* é deixar a transação morrer de fome por falta de acesso (assim como em OS)
    - resolver isso é colocar uma fila de prioridade nas operações
- acessos em árvore caminham entre os nodos com alguma intenção, até chegar no nodo necessário, faz o que precisa fazer e volta
    - dá uma concorrência maior mas reduz o tempo de resposta
    - apenas módulos folha de fato são afetados
- 2PL - two phase locking
    - impede qualquer outro bloqueio de afetar os locks-X
    - consegue desbloquar uma leitura mesmo após dar lock-S em uma outra
- 2PL - Rigoroso
    - sempre libera apenas ao final de tudo
- *Timestamps*
    - permite ordenação e controle de dados pelo tempo
- versialização também pode controlar pelo acesso e tipagem
-  a prevenção de *deadlock* utiliza várias ferramentas normais de administração e evita 

## Leitura suja
- *Dirty read*
- não acontecem erros e permitimos uma leitura em um momento que uma transação não foi completada
    - pode ser o caso de o valor ter sido atualizado, lemos, e a operação de alteração se desfaz
- pra evitar esse tipo de problema, só com serialização

# Recuperação de falhas
- várias alternativas
    - principal são sistemas baseados em *log*
        - *clusters* e **réplicas são todos baseados em ***logs***
- diversos outros sistemas de recuperação são ainda baseados em logs
- vale tudo, o que não pode acontecer é perder informação ou consistência
- **falhas de disco** são mais complexas mas ocorriam bastante em eras anteriores da computação
- **Logs** precisam ter todas as marcações de aplicação e das fazes da operação
    - ***traces*** de bancos de dados tem dezenas de informações
- o mais comum é desfazer e refazer a operação
    - aqui tem valor anterior e posterior
    - dá pra rodar 50x q o log ainda é o mesmo
- se uma operação fica pela metade é melhor dar um rollback e rodar depois
    - não sabemos se existia alguma operação em memória que ainda n tinha descido pro log
- ***Dump*** -> manda o banco exportar os dados e larga em um zip ou em um arquivo específico (criação de tables, etc) - restauração à frio
- **sempre teste seu backup**


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