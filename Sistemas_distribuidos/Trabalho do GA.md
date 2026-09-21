-> Trabalho do GA
Parte apresentação
	Na oitava aula, teremos as **apresentações**, no estilo **Pitch**: 8min apres. + 2 perguntas
	Entrega: PDF ou PP  + da apresentação até o dia da prova do GA. (nona aula)

Parte teórica:
	Fazer um documento em **LATEX** (Ooverleaf), **clone da SBC**, cerca de 10 páginas. Escolher um middleware e escrever as seções Introdução, Middleware X, Comparações, ..., Conclusão. Entregar até o dia da prova do GA.

Entrega é um PDF (doc).
Modernos - Azure, GCP, AWS
S.D. - Rede, Middleware != sockets, protodados, sistemas

### **Estrutura Proposta para o Trabalho**

#### **1. Introdução**

- **Contextualização**: O papel da mensageria assíncrona na comunicação desacoplada entre microsserviços e em pipelines de processamento de dados de alto desempenho.
- **Apresentação do GCP Pub/Sub**: Definição do Google Cloud Pub/Sub como um middleware _serverless_ orientado a eventos com garantia de baixa latência (aprox. 100ms).
- **Objetivo do Trabalho**: Analisar os aspectos arquiteturais, de segurança, resiliência e governança do Pub/Sub, comparando-o com alternativas do mercado (como Apache Kafka e AWS Kinesis).

---

#### **2. Google Cloud Pub/Sub**

- **2.1. Arquitetura e Infraestrutura Global**
    
    - **Separação de Planos**:
        - **Plano de Controle (_Control Plane_)**: Roteadores que utilizam variações de _consistent hashing_ para atribuir clientes aos servidores de dados com base na menor distância de rede.
        - **Plano de Dados (_Data Plane_)**: Servidores chamados _forwarders_ (publicadores e assinantes) responsáveis por persistir e transportar as mensagens.
    - **Persistência e Tolerância a Falhas**: Escrita síncrona de mensagens em múltiplos discos independentes e replicação em diferentes _clusters_ e regiões antes de confirmar a entrega (_ack_) ao publicador.
- **2.2. Funcionamento e Modelos de Consumo**
    
    - **Conceitos Fundamentais**: Tópicos, Assinaturas e Mensagens (constituídas por _payload_ em bytes e atributos de chave-valor).
    - **Modelos de Entrega (_Delivery Methods_)**:
        - **Push Subscriptions**: Entrega automática de mensagens para _endpoints_ HTTP/HTTPS (webhooks), ideal para integração sem bibliotecas de cliente e escalonamento automático no Cloud Run.
        - **Pull Subscriptions**: Consumo em lote controlado ativamente pelos clientes assinantes.
        - **Streaming Pull**: Conexão bidirecional persistente (gRPC) otimizada para alta vazão e baixíssima latência.
    - **Garantias de Entrega e Ordenação**: Entrega _at-least-once_ (pelo menos uma vez) por padrão, com suporte opcional a chaves de ordenação (_ordering keys_) e entrega exatamente-uma-vez (_exactly-once delivery_).
- **2.3. Segurança e Controle de Acesso**
    
    - **Autenticação e Autorização (IAM)**:
        - Aplicação do princípio do menor privilégio através de _Service Accounts_.
        - Papéis específicos por recurso e projeto, tais como `roles/pubsub.publisher` e `roles/pubsub.subscriber`.
    - **Proteção de Dados**: Criptografia de mensagens em trânsito e em repouso.
- **2.4. Tratamento de Erros e Resiliência**
    
    - **Tópicos de Mensagens Inativas (_Dead-Letter Topics_ / DLQ)**: Encaminhamento automático de mensagens não processadas após um número configurável de tentativas de entrega (_max delivery attempts_, entre 5 e 100).
    - **Metadados de Falha**: Injeção automática de atributos de diagnóstico na DLQ (ex: `CloudPubSubDeadLetterSourceDeliveryCount`, `CloudPubSubDeadLetterSourceSubscription`).
    - **Monitoramento e Alertas**: Métricas via Cloud Monitoring para acompanhamento de falhas de envio e atraso de consumidores (_consumer lag_).
- **2.5. Validação de Dados e Governança (Schemas)**
    
    - **Contratos de Dados**: Uso de esquemas vinculados aos tópicos para validação das mensagens na camada de publicação.
    - **Formatos Suportados**: Suporte a **Apache Avro** e **Protocol Buffers (Protobuf)** com codificação em JSON ou BINARY.
    - **Evolução de Esquemas**: Regras de compatibilidade (reversa e direta) para atualização de esquemas sem quebrar produtores ou consumidores.

---

#### **3. Comparação com Outros Middlewares de Mensageria**

- **3.1. Pub/Sub vs. Apache Kafka vs. Amazon Kinesis**
    
    - **Modelo de Paralelismo**: Kafka e Kinesis utilizam partição/shard (paralelismo atrelado ao número de partições), enquanto o Pub/Sub utiliza **paralelismo por mensagem**, permitindo escalonamento individualizado e independente dos assinantes.
    - **Modelo Operacional e Implantação**: Kafka exige gerenciamento de infraestrutura/brokers (ZooKeeper/KRaft) ou serviços gerenciados específicos; Kinesis exige provisionamento/dimensionamento de _shards_; o Pub/Sub é **100% _serverless_** sem necessidade de gerenciamento de capacidade.
    - **Tabela Comparativa**:
        - _Critérios_: Modelo de implantação, garantias de ordenação, retenção de dados, limites de mensagem, vazão e sobrecarga operacional.
- **3.2. Estudo de Caso de Migração Real: Spotify**
    
    - **Motivação**: Transição do ecossistema Kafka/Hadoop _on-premises_ para o GCP.
    - **Resultados**: Testes de carga com mais de 2 milhões de mensagens/segundo e redução substancial da complexidade operacional ao adotar o Pub/Sub integrado ao Cloud Dataflow.

---

#### **4. Conclusão**

- **Síntese dos Achados**: Vantagens do Pub/Sub na construção de arquiteturas orientadas a eventos modernas sem atrito operacional.
- **Indicação de Uso**: Quando optar pelo Pub/Sub (integrações _cloud-native_, microsserviços serverless, distribuição global) em relação ao Kafka ou Kinesis.
- **Trabalhos Futuros**: Considerações sobre otimização de custos e integração com ferramentas de _analytics_ em tempo real (BigQuery, Dataflow).

---

💡 **Sugestão para o próximo passo**: Se quiser, posso gerar um código LaTeX completo configurado no modelo da SBC para você colar no Overleaf, já com esses tópicos estruturados e formatados.