# Análise Estratégica e Técnica: Ecossistema Google Cloud Pub/Sub

## 1. Introdução

Nos anos recentes o uso de mensageria e necessidade de infraestruturas robustas à fim de manter aplicações funcionando de modo *seamless* tornou-se mais importante e imprescindível para a vida moderna. Nesse sentido, arquiteturas orientadas à eventos ganharam espaço, permitindo desacoplamento espacial e temporal entre os geradores de eventos e consumidores. Nesse cenário, o **Google Cloud Pub/Sub** aparece como a solução da gigante de tecnologia para uso interno de suas aplicações de entrega (Ads, YouTube, etc.) e, assim como no caso da Amazon, permite uso externo para outros clientes.

A escolha de um Middleware de mensageria adequado é imprescindível, assim como a escolha de um bom plano. À depender do uso do negócio, pode ser um facilitador ou um fardo/conta à ser paga pelo utilizador; Tornando a tradução da necessidade na utilização da aplicação.

O serviço é definido como uma solução de **mensageria assíncrona global**, projetada para alta confiabilidade e escalabilidade. Sua autoridade técnica é fundamentada em sua origem: o Pub/Sub foi construído sobre a infraestrutura interna do Google com base na arquitetura *Publicator - Subscriber*, a mesma que sustenta produtos de escala massiva como **Ads, Search e Gmail**. Essa herança garante que lições aprendidas em décadas de operação de tráfego em escala exabyte estejam incorporadas em uma solução serverless pronta para o uso corporativo.

Este relatório tem como objetivo demonstrar a arquitetura, resiliência, posicionamento competitivo e definição de cenários de uso na atualidade.
## 2. Google Cloud Pub/Sub: O Core Tecnológico

O design do Pub/Sub segue a **escalabilidade horizontal**, permitindo que o sistema lide com aumentos súbitos de carga com elasticidade suficiente para não se notar degradação na latência ou disponibilidade.

### Arquitetura

A arquitetura do GCP Pub/Sub foi desenvolvida para funcionar em camadas

A separação de responsabilidades é o que permite atualizações de sistema sem interrupção de serviço:

- **Control Plane (Routers):** Responsável por distribuir clientes entre os servidores do plano de dados. Utiliza uma variante de _consistent hashing with bounded loads_, desenvolvida pelo **Google Research**, para equilibrar a carga de forma uniforme e evitar sobrecarga em forwarders específicos, garantindo estabilidade mesmo em rebalanceamentos.
- **Data Plane (Forwarders):** Trata a movimentação real das mensagens. A comunicação ocorre através de uma **Proxy Layer** que criptografa e encaminha os dados para o _publishing forwarder_. O sistema garante o **Global Data Access**, direcionando o tráfego para o data center mais próximo com base na menor distância de rede, independentemente da localização física do tópico.

![[Arquitetura_GCP_pub-sub.png]]
Exemplo de implementação com GCP integrado aos serviços de API do Google.
![[arquitetura_com_GCP_integrado.png]]

### Persistência e Tolerância a Falhas

O ciclo de vida de uma mensagem (Life of a Message) garante a durabilidade total após a confirmação de recebimento. O processo se dá de forma que:

**Regra de Persistência Técnica:** Para garantir a durabilidade, o Pub/Sub escreve a mensagem em N clusters (onde N é um número ímpar). A mensagem é considerada persistida apenas quando escrita com sucesso em pelo menos N/2 clusters. Internamente, em cada cluster, a mensagem é replicada em M discos independentes, exigindo a confirmação em M/2 discos antes de ser considerada persistida localmente.

### Segurança e Controle de Acesso

A segurança é integrada via **IAM (Identity and Access Management)**, fornecendo controle granular para os papéis de _Publisher_ e _Subscriber_. A automação é viabilizada por **Service Accounts**, que gerenciam permissões de forma programática. Um diferencial de governança é o suporte nativo a **Schemas (Avro e Protobuf)**, que atuam como contratos de dados, permitindo a detecção precoce de dados malformados antes que causem falhas em serviços _downstream_.

### Tratamento de Erros e Resiliência

Desenvolvidos abaixo alguns dos conceitos que o GCP Pub/Sub utiliza:

- **Dead-letter topics:** Mensagens que não podem ser processadas após tentativas exaustivas são encaminhadas para um tópico de "letra morta" para análise e debugging offline.
- **Propriedades de Subscrição:** Inclui o **Maximum number of delivery attempts** (configurável de 5 a 100), _Ack Deadline_ e políticas de reprocessamento.
- **Trade-off de Ordenação:** Embora suporte _Ordering Keys_, o uso dessas chaves **reduz o paralelismo e o throughput**, um ponto de atenção crítico para arquitetos que buscam performance extrema.

## 3. Análise Comparativa de Middlewares

Como elaborado anteriormente, a escolha do middleware deve alinhar-se à expertise da equipe e à previsibilidade da carga de trabalho.

### Quadro Comparativo Estratégico

|   |   |   |   |
|---|---|---|---|
|Recurso|Apache Kafka|Amazon Kinesis|Google Pub/Sub|
|**Modelo de Implantação**|Gerenciado/Self-hosted|Totalmente Gerenciado|Serverless (NoOps)|
|**Garantia de Ordenação**|Por partição|Por shard|Opcional (impacta throughput)|
|**Tamanho Máximo da Mensagem**|1MB (padrão)|1MB|**10MB**|
|**Retenção de Mensagem**|Configurável (Ilimitada)|Até 365 dias|Até 7 dias|
|**Sobrecarga Operacional**|Alta (ZooKeeper/KRaft)|Baixa (Gestão de Shards)|Mínima|
|**Latência Típica**|5-10ms (tunado)|70-200ms|100-500ms|

### Diferenciadores e Análise Financeira

O Pub/Sub destaca-se pela **simplicidade serverless**. Enquanto o Kafka exige gestão de partições e o Kinesis demanda monitoramento de shards (1MB/s de escrita por shard), o Pub/Sub elimina o planejamento de capacidade. Financeiramente, o modelo **pay-per-GB** do Google (estimado em **US$ 40-80 por TB**) é ideal para cargas variáveis. Em comparação, o modo _on-demand_ do Kinesis pode custar **30-50% menos** que sua capacidade superprovisionada, mas ainda exige vínculos com o ecossistema AWS.

**Estudo de Caso de Custo estimado (100GB/dia, 3 dias de retenção):**

- **Kafka (Self-hosted na AWS):** ~US$ 550-950 (incluindo instâncias EC2, EBS e transferência).
- **Amazon Kinesis (On-demand):** ~US$ 900 (ingestão e recuperação).
- **Google Pub/Sub:** ~US 800 (US 400 publicação + US$ 400 entrega).

O Pub/Sub suporta mensagens de até **10MB**, um diferencial interessante contra o limite de 1MB dos concorrentes, permitindo integrações de dados complexos sem a necessidade de fragmentação lógica (_chunking_) e que serve de compensação para o período de retenção consideravelmente menor (apenas 7 dias).

## 4. Estudo de Caso de Alta Escala: A Infraestrutura Google

Analisar sistemas que operam em escala exabyte valida a robustez do Pub/Sub para o mercado corporativo.

### Análise de Escala Real

A tecnologia processa métricas críticas para o **Google Ads** e indexação em tempo real para o **Gmail** e **Search**, atingindo marcas de **500 milhões de mensagens por segundo** e um tráfego agregado de **1TB/s**.

### Rigor de Engenharia

A manutenção dessa escala é gerida por SREs através de três ambientes distintos:

1. **Test:** Onde novas funcionalidades são validadas sem tráfego de clientes.
2. **Staging:** Uma **réplica exata da produção** (versão, flags e configuração) para testes finais.
3. **Production:** Rollout progressivo via _Canary_ após dias de estabilidade em Staging.

O Google monitora o sistema com **Probers** (clientes que simulam tráfego real) e opera sob SLOs estritos, como a garantia de **criação de subscrições em menos de 5 segundos**. Nesse mesmo sentido, o Google ainda apresenta quantas respostas conseguiu adquirir em dado tempo, ferramenta que passa sobre o uso do GCP Pub/Sub.

![[Pesquisa_de_batata.png]]
![[Batata_menor.png]]

## 5. Conclusão

Tendo essa visão global da ferramenta, o Google Cloud Pub/Sub é uma solução definitiva para arquiteturas que priorizam escala global nativa e a eliminação de dívida técnica operacional.

### Pontos Fortes e Limitações

- **Pontos Fortes:** 
	- Limite de 10MB por mensagem; 
	- Integração nativa com Dataflow/BigQuery;
	- Escala global sem shards;
	- Governança via Schemas (Avro/Protobuf) como contratos entre microserviços.
- **Limitações:** 
	- Retenção limitada a 7 dias;
	- Latência superior (100-500ms) (inadequada para trading de alta frequência);
	- Custo superior ao Kafka (bem otimizado) em volumes massivos e constantes.

### Exemplo de Cenário Ótimo de Uso

O Pub/Sub é recomendado para **microsserviços orientados a eventos, ingestão de dados de IoT e distribuição global de mensagens** em equipes que buscam uma estratégia **NoOps**. Se a prioridade é governança de dados com baixo custo operacional e suporte a mensagens grandes, o Pub/Sub supera os concorrentes.

_O Google Cloud Pub/Sub oferece mensageria global serverless com suporte a mensagens de até 10MB e processamento de 500 milhões de eventos por segundo. Sua arquitetura de persistência em clusters e discos garante durabilidade extrema, enquanto o suporte a schemas consolida a governança de contratos em sistemas distribuídos. Embora possua latência superior ao Kafka, sua simplicidade operacional e integração nativa o tornam a escolha mais ágil para o ecossistema de nuvem moderno._



Ainda precisamos de mais alguns textos:
- elaboração sobre a arquitetura;
- explicar o conceito de publish-subscribe
- sistema de monitoramento do GCP pub/sub
- explicar como julgar o desempenho de um serviço de mensageria
- Adicionar a explicação do termo Canary

