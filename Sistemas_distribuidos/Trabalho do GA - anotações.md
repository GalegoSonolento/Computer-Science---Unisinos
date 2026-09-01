https://www.dre.vanderbilt.edu/~schmidt/PDF/FOME-HCDS-paper.pdf -> ler esse artigo pra ter uma ideia

**Diário de Missão: A Lenda do Kafka** 📜

_Missão principal: Middleware Master — GA de Sistemas Distribuídos_

☐ **Objetivo 1 — Erguer o Overleaf** Criar o projeto no Overleaf com o template clonado da SBC. 

☐ **Objetivo 2 — Escrever a Introdução** Contextualizar o problema (comunicação em sistemas distribuídos), apresentar o Kafka e os objetivos do trabalho. _Dica do NPC: não gaste todas as flechas aqui, guarde profundidade pra seção 2._

☐ **Objetivo 3 — Dominar o Middleware Kafka** Detalhar arquitetura: brokers, topics, partitions, producers/consumers, KRaft/ZooKeeper, garantias de entrega. _Sub-quest: entender exactly-once semantics (chefão opcional, dá bastante XP)._

☐ **Objetivo 4 — Invocar os Conceitos de Sistemas Distribuídos** Conectar replicação, consistência, particionamento, tolerância a falhas e CAP theorem ao que foi visto na disciplina. _Item necessário: diferenciar Kafka de sockets crus (prova de que não é só "TCP com roupa nova")._

☐ **Objetivo 5 — Duelo de Comparações** Colocar Kafka em arena contra RabbitMQ/ActiveMQ/gRPC. Montar tabela comparativa (throughput, modelo, persistência).

☐ **Objetivo 6 — Explorar os Reinos Vendor (AWS/GCP/Azure)** Investigar Amazon MSK, Confluent Cloud, GCP Pub/Sub. Registrar trade-offs de gerenciado vs. self-hosted.

☐ **Objetivo 7 — Coletar Relíquias de Aplicações Modernas** Reunir casos reais: event streaming, microsserviços orientados a eventos, CDC, real-time analytics. Citar quem usa (LinkedIn, Netflix, Uber).

☐ **Objetivo 8 — Selar a Conclusão** Fechar com síntese: por que Kafka, quando usar, limitações.

☐ **Objetivo 9 — Forjar o Pitch (8 slides de poder)** Resumir cada seção em 1 slide-chave. Treinar os 8 minutos + preparar respostas pra 2 perguntas do mestre da masmorra (professor).

☐ **Objetivo 10 — Entrega Final** Exportar PDF do LaTeX + PDF/PPT da apresentação. Entregar antes da nona aula (dia da prova do GA).

---

🏆 **Conquista desbloqueada ao concluir tudo:** _"Sobrevivente do GA"_

Quer que eu ajude a "farmar XP" começando pelo Objetivo 2 (Introdução) já em texto corrido?

Fontes:
- https://www.datacamp.com/pt/tutorial/apache-kafka-for-beginners-a-comprehensive-guide -> tem inclusive um totorial pra montar uma aplicação de teste como o Kafka

---
Anotação de trechos

Parte 2 - contextualização do Kafka
O Apache Kafka, originalmente desenvolvido pelo LinkedIn em 2011 e posteriormente doado à Apache Software Foundation, consolidou-se como uma das principais plataformas de streaming de eventos distribuídos. Diferente de uma comunicação ponto a ponto via sockets, o Kafka introduz um modelo de publicação e assinatura (publish-subscribe) apoiado em um log distribuído, o que possibilita escalabilidade horizontal, e persistência de eventos, paralelismo no consumo de dados e a diminuição da carga nos produtores ao gerar desacoplamento, de forma que o produtor não precisa coordenar a comunicação com cada consumidor.

De maneira geral, o Kakfa funciona como um cluster de diversos brokers, os quais por sua vez hospedarão as réplicas das partitions (uma unidade de armazenamento e ordenação dentro de um tópico) definindo uma como a líder; que armazenam as mensagens passadas pelo Producer e às entrega aos consumers dada a demanda/consulta dos mesmos (subscription). Dessa forma ele reduz a responsabilidade do produtor sobre a coordenação da entrega aos consumidores (no handling das requisições de mensagens) e mantém os eventos de acordo com uma política de retenção configurada.

Nesse sentido, o Kafka não simplesmente trabalha com Publish/Subscribe, ele ainda pode versionar mensageria, abstração de consumers, separação deles em grupos e paralelização entre esses grupos e tolerância a falhas. 



Grosso modo, o Kafka funciona como um cluster de _brokers_, os quais hospedam réplicas das _partitions_, unidades de armazenamento e ordenação dentro de um tópico, definindo uma delas como líder. Nesse sentido, o broker com a partition líder é responsável por receber as mensagens enviadas pelo _producer_ e entregá-las aos _consumers_ de acordo com a demanda destes (_pull_, via _subscription_), enquanto os demais brokers mantêm réplicas, sendo consideradas _In-Sync Replicas_ (ISR) aquelas que permanecem suficientemente sincronizadas com o líder para estarem aptas a assumir a liferança caso este se torne indisponível (e.g. queda de conexão do Broker, lembre-se que eles estão clusterizados). Dessa forma, o produtor deixa de ser responsável por coordenar a entrega das mensagens a cada consumidor individualmente, e as mensagens são mantidas de acordo com uma política de retenção configurável.

A leitura das mensagens é controlada pelo próprio consumidor por meio do conceito de _offset_, um índice sequencial que indica sua posição de leitura dentro da partition, permitindo que múltiplos consumidores leiam o mesmo tópico em ritmos e momentos diferentes. Além disso, o Kafka organiza consumidores em _consumer groups_: cada partition de um tópico é atribuída a, no máximo, um consumidor dentro de um mesmo grupo, o que possibilita paralelismo no processamento sem duplicidade de mensagens, ao mesmo tempo em que múltiplos grupos podem consumir o mesmo tópico de forma independente.

A garantia de ordenação do Kafka é local à partition e não ao tópico como um todo — mensagens em partitions diferentes podem ser processadas fora de ordem entre si. A coordenação dos metadados do cluster e a eleição de líderes de partition, originalmente dependentes do Apache ZooKeeper, passaram a ser gerenciadas internamente pelo próprio Kafka a partir da introdução do protocolo KRaft, eliminando a dependência de um serviço externo de coordenação.

---
**Comparação do Kafka com o RabbitMQ**

É importante destacar que no universo de Middlewares para comunicação assíncrona (tanto de espaço quando de tempo), temos outras opções tão boas quanto (ou ainda mais indicadas para determinada situação que outras). Nessa ceara, teamos exemplos como IBM MQ, Apache ZooKeeper, Redis e Amazon SNS; todos funcionando com uma ou outra diferença, à depender da implementação dos desenvolvedores. Nesse momento; todavia, cabe uma comparação entre o Kafka e outra ferramenta bastante utilizada no mesmo meio, o Rabbit MQ.

Abaixo segue uma tabela comparativa entre as duas ferramentas:

|                                  |                                                                                                                                      |                                                                                                                                           |                                                                                                                                                                      |                                                                                                                                                                         |                               |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| Característica                   | Apache Kafka                                                                                                                         | RabbitMQ                                                                                                                                  | Vantagens                                                                                                                                                            | Desvantagens                                                                                                                                                            | Fonte                         |
| Arquitetura e Armazenamento      | Log de confirmação (commit log) distribuído, replicado e particionado. Armazena registros sequencialmente em disco (append-only) 1.  | Modelo de broker central que gerencia filas tradicionais (Store-and-forward). Suporta Streams (log append-only) em versões recentes 2, 3. | Kafka: Escalabilidade horizontal e alto rendimento constante. RabbitMQ: Flexibilidade com diferentes estruturas de dados e roteamento complexo 1-5.                  | Kafka: Maior complexidade de configuração e gerenciamento de offsets. RabbitMQ: Dificuldade em lidar com volumes massivos de dados e filas longas 1, 3, 4, 6.           | 1, 2, 3, 5, 6, 9, Inferred    |
| Políticas de Retenção de Dados   | Mensagens são retidas mesmo após o consumo, baseando-se em tempo ou tamanho configurável. Suporta compactação de log por chave 1, 2. | Geralmente, as mensagens são removidas após a confirmação do consumo (ACK). Streams podem reter por tamanho ou tempo Inferred, 2, 3.      | Kafka: Permite que novos consumidores leiam dados históricos (Unlimited Lookback) e reprocessamento (replay) 1, 2, 4, 7.                                             | Kafka: Risco de esgotamento de disco se a política de retenção não for bem dimensionada. RabbitMQ: Perda de dados se não houver consumidor ou persistência 1, 3, 4, 7.  | 1, 2, 3, 5, 7, 8, Inferred    |
| Escalabilidade e Particionamento | Nativo com suporte a partições distribuídas entre brokers. Permite paralelismo massivo entre consumidores de um mesmo grupo 1.       | Escalabilidade vertical/clusters; o agrupamento de filas (clustering) é mais complexo para escala massiva Inferred, 3, 7.                 | Kafka: Suporta centenas de milhares de mensagens por segundo com hardware modesto. RabbitMQ: Runtime BEAM isola falhas em processos leves 1-3.                       | Kafka: Alterar o número de partições em tópicos baseados em chaves pode quebrar a ordenação. RabbitMQ: Gargalos em sincronização de filas grandes 1, 3, 8.              | 1, 2, 3, 7, 8, Inferred       |
| Garantias de Ordenação           | Garantida estritamente dentro de uma partição (sequência por offset) 1, 9.                                                           | Garantida dentro de uma fila (FIFO) ou via streams particionados (super streams) 2, 3, 9.                                                 | Ambos oferecem paralelismo com preservação de ordem em partições ou fluxos específicos 2, 7, 8.                                                                      | Kafka: Não garante a ordenação global entre múltiplas partições. RabbitMQ: Ordenação pode ser perdida com múltiplos consumidores concorrentes na mesma fila 1, 3, 6, 9. | 1, 2, 3, 4, 6, 7, 8, Inferred |
| Entrega e Notificação            | Modelo de 'Pull': o consumidor busca mensagens no seu próprio ritmo e controla sua posição (offset) 1, 9.                            | Modelo de 'Push': o broker envia mensagens para os consumidores (Smart broker) Inferred, 4, 5.                                            | Pull (Kafka): Proteção contra sobrecarga (backpressure). Push (RabbitMQ): Baixa latência para notificações instantâneas 4, 7, 9.                                     | Pull: Pode introduzir latência se o polling for lento. <br>Push: Risco de sobrecarregar consumidores lentos se não houver controle de fluxo 4, 7, 9.                    | 1, 4, 5, 7, Inferred          |
| Publish/Subscribe e Consumidores | Desacoplamento total; múltiplos grupos de consumidores independentes podem assinar o mesmo tópico 1, 7.                              | Suporta Pub/Sub via Exchanges (Direct, Topic, Fanout) e Bindings que roteiam mensagens para filas 2-4.                                    | Kafka: Fan-out altamente eficiente e escalável para múltiplos sistemas. RabbitMQ: Roteamento granular e dinâmico com chaves específicas 2, 4, 5, 7.                  | Kafka: Menos flexível para lógicas de roteamento complexas. RabbitMQ: Inviável se muitas aplicações precisarem dos mesmos dados brutos sem duplicação 3-5.              | 1-5, 7                        |
| Mecanismo de Replicação          | Baseada em In-Sync Replicas (ISR) e KRaft. Replicação síncrona ou assíncrona entre líderes e seguidores 1, 2, 7.                     | Filas espelhadas (Mirrored Queues) ou Quorum Queues (baseadas em Raft) para alta disponibilidade Inferred, 2, 7.                          | Kafka: Alta durabilidade e tolerância a falhas nativa. RabbitMQ: Quorum Queues garantem durabilidade com fsync obrigatório 1, 2, 7.                                  | Kafka: Replicação entre datacenters distantes pode degradar o desempenho. RabbitMQ: Performance cai significativamente com filas espelhadas clássicas 1, 4, 7.          | 1, 2, 7, Inferred             |
| Protocolos Suportados            | Protocolo binário próprio sobre TCP 1, 2.                                                                                            | Multi-protocolo: AMQP (0-9-1, 1.0), MQTT, STOMP, HTTP e WebSockets 2-4.                                                                   | Kafka: Otimizado para lotes (batches), reduzindo sobrecarga de rede. RabbitMQ: Alta interoperabilidade entre diferentes linguagens e sistemas (IoT, Web) 1, 2, 4, 6. | Kafka: Requer proxies ou bibliotecas específicas para protocolos padrão. RabbitMQ: Overhead do protocolo AMQP pode reduzir o throughput comparado ao binário 2-4, 6.    | 1, 2, 3, 5, 6, Inferred       |