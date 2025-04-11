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

DATA: 13/Março/2025
# índice
- ordenação de registros
- identificação
- otimização de consultas
- a ideia é seguir o mesmo princípio de um sumário de livro
    - ou índice remissivo
    - livros grandes, assim como bases de dados, precisam de uma pesquisa sequencial
    - ter índices permite pesquisar por termos ou assuntos e chegar á informação de forma mais rápida (deveras)
- **cheaves primárias** levam diretamente ao registro
    - ou levam pra blocos de informação
- busca de arquivos tem a msm ideia de um *SGBD*
- buscam que se baseiam em chaves de pesquisa
    - where em campos indexados auxiliam na pesquisa dos dados
    - sem indexação o banco precisa fazer um ***full scan*** na table inteira pra encontrar o dado
- ***Primary key*** -> sim, sempre
    - nunca pode ser nula
- ***Unique Key*** -> não é PK mas é única pra cada *record*
    - pode ser uma combinação de campos
    - SGBD n deixa outro registro ter o mesmo *set-up*
    - pode ser nula - a não ser que declarado *not null*
- ***Foreign Key*** -> PK de outra table
- pq não colocar índice em todos os campos?
    - espaço gasto pra nada (não se usam todos os campos)
    - índice é uma estrutura a parte que serve de referência
        - se já existe um termo que leva pra informação não tem porque ter uma redundância nesse sentido
    - leva tempo pra atualizar a estrutura de índices
        - com muitos registros demora bem mais

## índices Denso e Esparsos
- aparecem em concursos e construção de bancos
- indices primários
    - problemas com inseções no bloco de índices 
    - fica em RAM
    - a busca é sequencial ali dentro
- secundário
    - campo não-ordenado
    - pode ser ou não UK
    - seria um segundo valor de filtro quando muito utilizado (em *where*)
    - pode ser implementado com denso ou esparso, assim como o primário
    - é possível ter uma chave primária sequencial que aponta para uma secundária esparsa que consegue acessar blocos de registros
        - em diferentes tables
- índices de múltiplos níveis
    - buscas complexas com índices muito grandes
    - índice do índice
    - quebra a estrutura em alguns níveis pra conseguir manter em memória
    - todas as altearções vão demorar mais 
        - SGBD precisa recriar os múltiplos níveis
    - entram as árvores balanceadas
        - conceito de organização de arquivos
    - quando se cria um descompasso de índices, o sistema quebra ele com o ***overflow***

### Denso
- colocado pra cada valor distinto
- existem um apontamento pra cada valor diferente
- Compos com muitas buscas

### Esparso
- criado apenas para alguns valores
- **clusterização** - blocos de registros - paginação
- acessa o bloco e dentro do bloco faz uma pesquisa sequencial
    - isso já deixa a pesquisa bastante mais rápida por quebrar tables grandes em páginas

## Estrutura de Indexação Árvores B (B-Trees)
- árvore "binária" balanceada
    - 2 filhos e repartição de pesquisa pelo meio
    - o número de filhos é a quantidade de registros na página +1
- evitar desperdício em blocos de nó
- usado em casos com muitas inserções e remoções
- caso da rede social e IoT
    - normalmente são muitas inserções e não tem muita mudança ou pesquisa
    - preocupação com espaço também não existe
    - privilégio de inserção e consulta
    - *Wide Column*
    - tem DML, select, etc - estrutura, mas privilegia inserções
    - isso mesmo, IoT coleta dados (seus inclusive) - ´ra quem ele manda, depende
- árvore é rebalanceada a cada alteração
    - ocupação mínima de 50%
- nós são páginas
    - busca paginada
- poucas páginas pra poucos registros
    - todas as folhas no mesmo nível
- sempre constrói pra cima e deixa espaço para novos registros
- sempre 50% de uso
    - manter poucos acessos pra chegar no resultado
    - no pior dos cados é uma busca logaritmica (na base do tamanho da página)
- mas é uma árvore que de fato precisa de uma manutenção maior e alterações demoram mais tempo
    - detrimento disso em rapidez de *select*
- mas em *betweens* ele precisa de vários acessos

### Árvores B+ (Bplus-tree)
- busca de valores encadeados
- **todos os ramos terão o mesmo comprimento**
- na raiz existem apontamentos para os próximos valores em sequência
    - na folha aparessem todos os valores da árvore (inclusive os da raíz)
    - também existem apontamentos entre os blocos
- isso permite busca sequencial
    - só precisa usar as folhas como uma lista normal

## Hashing
- *blockchain* usa encadeamento por funções de *hash*
- transforma uma chave em um endereço - busca rápida por chave
- mapa de chave-valor
- apontamentos de **blocos** (*buckets*)
- estaticidade
    - números de blocos pequeno faz com que ele cresca pros lados
        - **cadeias de *overflow***
    - hashing dinâmico permite aumentar o número de *buckets* - árvores B+
- ***Hashing* extensível** tem um logaritmo de 2 na pior das hipóteses - talvez de ~69%

## Bitmap
- mapa de bits
- array de bits
- ligar os valores das posições
- consultas de vários campos
    - AND, OR, ect
- bit-a-bit
    - Oracle utiliza bastante
- marca as linhas que tem determinado valor com um número binário (indexa) e aplica operações AND, OR, etc com esses números binários 
    - o resultado é a linha onde está no valor
- muito utilizado para colunas que repetem valores
- pode crescer bastante por lado, mas é um bit, então é menor que a maioria das estruturas  
    - operação muito leve (binária apenas)

# Indexação por função
- Oracle utiliza
- índice específico para determinado tipo de consulta
- utilizar índices pra consultas com *where* de campos não-indexados
    - *where* muito utilizado, claro

DATA: 20/Março/2025
# Banco de dados distribuído
- replicação de dados
- data centers distribuídos
    - ou o lugar que guarda os dados
- oposição à bancos de dados distribuídos
- cobrança é feita a partir do número de cores utilizados para o banco
    - bancos distribuídos tem o mesmo tipo de cobrança e são potencialmente ainda mais caros (dado a quantidade de nós a mais)
- ainda é tudo ou nada
    - vai precisar ainda de um esquema de replicação
- pra bancos centralizados, o máximo que dá pra fazer é melhorar a máquina 
    - em distribuídos podemos simplesmente adicionar mais uma máquina na mesma rede
- apresentado bastante em SaaS e PaaS
    - IaaS ainda é administrado pelo user, ele só compra as máquinas
- ***Cloud Services***
- banco + sistema de controle
- esses bancos não são necessariamente ligados na mesma *rede* (cabeada, por exemplo)
    - vai ser uma conezão P2P, ou por rede sem fio

## Replicação em bancos de dados
- replicação em vários nós
- segurança q se um dos nós cair o dado não se perde
- dessentralização
- poslíticas de backup
- em tese fica mais tempo no ar que um ambiente centralizado

# Bancos de Dados NoSQL
- tese do elevador
    - tu precisa conseguir explicar teu projeto no tempo de uma conversa de elevador
- schemas não -fixos
    - soft (relacional sendo *hard*)
- largar 400MB em um banco relacional é complicado
    - não é feito pra isso
- IOT tem papel nesse avanço
- processamento e velocidade são fatores predominantes para o uso de NoSQL
- baseado no JSON files
    - a estrutura do json mesmo é bastante simples
    - json já é um banco de dados chave-valor
    - bastante intuitivo inclusive
- consistência eventual
    - sistema distribuído nativamente
- metodos feitos como se fosse orientação a objetos
- escalabilidade horizontal
    - mais máquinas, mais nós
    - scale-out
    - usada pelo NoSQL
- escalabilidade vertical
    - mesma máquina com upgrades
    - scale-up
- NÃO É NEWSQL
    - esse newSQL é pra BigData
- maioria no mercado atualmente
- Map/Reduce está de volta
- código mais complexo

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