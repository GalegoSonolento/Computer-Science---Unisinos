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



Grosso modo, o Kafka funciona como um cluster de _brokers_, os quais hospedam réplicas das _partitions_, unidades de armazenamento e ordenação dentro de um tópico, definindo uma delas como líder. Nesse sentido, o broker com a partition líder é responsável por receber as mensagens enviadas pelo _producer_ e entregá-las aos _consumers_ de acordo com a demanda destes (_pull_, via _subscription_), enquanto os demais brokers mantêm réplicas, sendo consideradas _In-Sync Replicas_ (ISR) aquelas que permanecem suficientemente sincronizadas com o líder se torne indisponível (e.g. queda de conexão do Broker, lembre-se que eles estão clusterizados). Dessa forma, o produtor deixa de ser responsável por coordenar a entrega das mensagens a cada consumidor individualmente, e as mensagens são mantidas de acordo com uma política de retenção configurável.

A leitura das mensagens é controlada pelo próprio consumidor por meio do conceito de _offset_, um índice sequencial que indica sua posição de leitura dentro da partition, permitindo que múltiplos consumidores leiam o mesmo tópico em ritmos e momentos diferentes. Além disso, o Kafka organiza consumidores em _consumer groups_: cada partition de um tópico é atribuída a, no máximo, um consumidor dentro de um mesmo grupo, o que possibilita paralelismo no processamento sem duplicidade de mensagens, ao mesmo tempo em que múltiplos grupos podem consumir o mesmo tópico de forma independente.

A garantia de ordenação do Kafka é local à partition e não ao tópico como um todo — mensagens em partitions diferentes podem ser processadas fora de ordem entre si. A coordenação dos metadados do cluster e a eleição de líderes de partition, originalmente dependentes do Apache ZooKeeper, passaram a ser gerenciadas internamente pelo próprio Kafka a partir da introdução do protocolo KRaft, eliminando a dependência de um serviço externo de coordenação.