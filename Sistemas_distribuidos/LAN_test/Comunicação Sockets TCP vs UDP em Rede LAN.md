Nesse teste foram dois computadores conectados por um cabo RJ45 (Ethernet), com um cliente em máquina Windows 11 e um servidor Linux CachyOS.
## 1. Comportamento do Tempo de Comunicação (Latência / RTT)

O gráfico de tempo de comunicação ilustra o tempo total de ida e volta (Round Trip Time - RTT) necessário para que o cliente envie um payload e receba o eco exato do servidor.

* **Cargas Menores (100 a 500 bytes):** Os tempos de resposta para ambos os protocolos são na ordem dos milissegundos. O TCP apresenta uma latência ligeiramente superior ao UDP. Este comportamento é esperado devido ao *overhead* inerente ao TCP, que exige o estabelecimento de conexão (*Three-way Handshake*) e a troca constante de pacotes de confirmação (ACKs) para garantir a entrega, enquanto o UDP envia os datagramas sem verificações prévias.
* **Cargas Maiores (100 KB a 10 MB):** O tempo de comunicação cresce de forma acentuada. O aumento no tempo reflete não apenas o limite de transmissão física do cabo de rede, mas também o tempo de processamento gasto pelo sistema operacional para fragmentar os dados em pacotes menores que caibam no MTU (Maximum Transmission Unit) da rede, enviá-los e remontá-los na máquina de destino adicionado ao fato que de tive que quebrar os pacotes UDP manualmente, uma vez que o protocolo pussui limite no tamanho do quadro.

## 2. Comportamento do Uso de Largura de Banda (Throughput)

A largura de banda foi calculada relacionando o volume total de dados trafegados (ida e volta) com o tempo total da operação.

* **Baixa Eficiência em Pacotes Pequenos:** Para mensagens de 100 e 500 bytes, a largura de banda registrada é extremamente baixa (geralmente inferior a 10 Mbps). Isso ocorre porque a proporção entre os dados úteis (payload) e os cabeçalhos de rede (IP, TCP/UDP, Ethernet) é desfavorável. O sistema gasta mais tempo processando chamadas de sistema (syscalls) e cabeçalhos do que efetivamente transmitindo o conteúdo.
* **Platô de Saturação:** Conforme o tamanho da mensagem aumenta para a casa dos Megabytes (1 MB a 10 MB), a eficiência da transmissão sobe drasticamente. O gráfico forma uma curva ascendente que estabiliza em um platô elevado. Este teto representa o limite físico real da interface de rede e do cabo utilizado (aproximando-se da capacidade máxima do link Ethernet, como 100 Mbps ou 1000 Mbps Gigabit).

## 3. Limitações e Desafios Arquiteturais do UDP

Durante os testes práticos, o protocolo UDP apresentou falhas críticas de entrega a partir da carga de 512 KB, exigindo uma adaptação na arquitetura do código cliente para a conclusão do experimento.

O UDP é um protocolo orientado a datagramas sem controle de fluxo (*fire-and-forget*). Na primeira iteração do teste, o cliente Windows despachou os fragmentos do arquivo de 10 MB na velocidade máxima da CPU. Como o servidor CachyOS ecoava os pacotes de volta imediatamente, o buffer de recepção interno do sistema operacional (Windows) transbordou rapidamente. Isso resultou no descarte massivo de pacotes (*packet loss*) e no travamento da aplicação, que aguardava dados que nunca chegariam.

O protocolo TCP não sofreu deste problema devido à sua "Janela Deslizante", um mecanismo nativo de controle de congestionamento que ajusta automaticamente a taxa de envio com base na capacidade de recepção do destino.

Para viabilizar a medição de mensagens grandes no UDP sem recriar os mecanismos do TCP, foi necessário implementar um envio intercalado (Ping-pong síncrono por fragmento de 65 KB). Isso demonstrou, na prática, que o UDP é altamente eficiente para transmissões rápidas e pequenas (como streaming ou jogos), mas inadequado para a transferência massiva e íntegra de arquivos sem a implementação de uma camada de controle adicional.