A arquitetura modular que você sugeriu é uma excelente abordagem. Para um modelo cliente-servidor (Ping-pong), separar a lógica em arquivos baseados em suas responsabilidades facilita a manutenção e a geração dos relatórios.

Em vez de nomear por máquinas (`PC1.py` e `PC3.py`), estruturar por papéis de rede torna o código universal para rodar no Windows e no CachyOS.

## Estrutura de Arquivos Recomendada

* **`config.py`**: Armazena as variáveis globais (IP, portas, lista de tamanhos de mensagens em bytes: 100, 500, 102400, 512000, 1048576, 10485760).
* **`payload_generator.py`**: Função única que gera as strings ou arrays de bytes aleatórios nos tamanhos exigidos.
* **`servidor.py`**: O processo passivo. Fica em loop ouvindo conexões. Recebe a mensagem e a devolve imediatamente (Ping-pong). Deve suportar tanto TCP quanto UDP.
* **`cliente.py`**: O processo ativo. Gera o payload, inicia o cronômetro, envia, aguarda a resposta completa, para o cronômetro, calcula as métricas e salva em um arquivo CSV.
* **`plotter.py`**: Lê o CSV gerado pelo cliente e utiliza bibliotecas como `matplotlib` para gerar os gráficos de tempo e largura de banda.

## Considerações Críticas de Implementação

### 1. O Problema do UDP com Mensagens Grandes

Essa é uma "pegadinha" clássica nesse tipo de trabalho. O protocolo TCP é orientado a fluxo (stream); você pode dar um `.sendall()` de 10MB e o sistema operacional gerencia a quebra em pacotes.

O protocolo UDP é orientado a datagrama. O limite teórico de um datagrama UDP é 65.535 bytes (na prática, o limite seguro para evitar fragmentação de IP é próximo ao MTU, geralmente 1500 bytes). Se você tentar enviar 1MB ou 10MB de uma vez via socket UDP usando `sendto()`, o Python lançará um erro `OSError: Message too long`.

* **Solução para o projeto:** Para os tamanhos de 1MB e 10MB no UDP, você precisará implementar no código uma lógica de fragmentação (enviar em blocos de 64KB, por exemplo) no cliente, e um loop de remontagem no servidor.

### 2. Medição de Tempo e Banda

Para medir o tempo com a máxima precisão no Python, utilize `time.perf_counter()` em vez de `time.time()`.

A lógica do RTT (Round Trip Time) no `cliente.py` deve ser:

1. `inicio = time.perf_counter()`
2. Envia a mensagem (Ping).
3. Recebe a mensagem de volta (Pong).
4. `fim = time.perf_counter()`
5. `tempo_total = fim - inicio`

A **largura de banda** (Throughput) usa o tempo total. Como os dados vão e voltam, o total de dados trafegados na rede é o dobro do payload.

* Banda (bits por segundo) = `(Tamanho_Mensagem_Bytes * 8 * 2) / tempo_total`
* Para facilitar a visualização no gráfico, converta o resultado para Mbps (dividindo por 1.000.000).

### 3. A Infraestrutura de Teste (Wi-Fi vs Cabo RJ45)

Como você possui um cabo RJ45, **use-o para os testes oficiais**.
Conecte o computador Windows e o computador com CachyOS diretamente pelo cabo. Configure IPs estáticos manuais nas duas pontas (ex: Windows `192.168.10.1`, CachyOS `192.168.10.2`) e desative o Wi-Fi durante os testes.

* **Motivo para a Análise:** O Wi-Fi utiliza o meio compartilhado (ar) e está sujeito a colisões (CSMA/CA), interferências de outros roteadores e micro-quedas. Isso gera *jitter* (variação no tempo de comunicação), o que deixará seu gráfico de latência caótico, dificultando a análise do impacto real dos tamanhos de mensagem. O cabo direto fornecerá um ambiente isolado, onde a única variável será o comportamento do protocolo e o tamanho do pacote.

## Análise e Gráficos (O que esperar e explicar)

**Gráfico de Tempo de Comunicação:**

* Você deverá plotar o Tamanho da Mensagem no eixo X e o Tempo (ms) no eixo Y.
* **Comportamento:** O tempo de comunicação crescerá linearmente conforme o tamanho da mensagem aumenta. O TCP deve apresentar um tempo levemente maior que o UDP nos pacotes menores devido ao *Three-way Handshake* (se você contar o tempo de conexão) e aos pacotes de confirmação (ACKs).

**Gráfico de Largura de Banda:**

* Você plotará o Tamanho da Mensagem no eixo X e a Largura de Banda (Mbps) no eixo Y.
* **Comportamento:** Para os pacotes de 100 e 500 bytes, a largura de banda calculada será baixíssima. Isso ocorre porque o tempo de processamento das camadas de rede (cabeçalhos, syscalls do SO) é desproporcionalmente grande em relação aos dados úteis. Conforme o tamanho da mensagem chega a 1MB e 10MB, o gráfico de banda deve subir de forma acentuada e estabilizar em um platô. Esse platô é o limite físico da sua placa de rede (provavelmente próximo a 100 Mbps ou 1000 Mbps / Gigabit, dependendo do hardware dos dois PCs).
---
De maneira geral vou montar tudo no pc mesmo e largar um RJ45 entre os dois pcs

