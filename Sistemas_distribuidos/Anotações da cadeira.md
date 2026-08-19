Primeira aula tivemos um panorama geral - ainda sem especificidades.
Uma das coisas mais importante em sis dist é ter controle de clock
	- ordem de operações importa nesse caso

Escalabilidade: oferecer a mesma qualidade de serviço com maior carga imposta

Alto desempenho é encurtar o tempo de execução de sistemas

Replicação é ruim quando a maioria das operações é de escrita

Distribuição vira um problema com segurança e com dependência de desempenho de rede
![[Pasted image 20260811200650.png]]
https://en.wikipedia.org/wiki/Myrinet
https://en.wikipedia.org/wiki/Network_security

![[Pasted image 20260811201604.png]]
Melhor portabilidade existe hj é WebServices
**Toda** comunicação por rede necessariamente usa sockets - SYSCALL
	mas é psaaível de erro

![[Pasted image 20260811203646.png]]
![[Pasted image 20260811203815.png]]
Apesar de fácil de implementar tem pouca tolerância a falhas e pouco escalável - o P2P é o contrário
![[Pasted image 20260811204306.png]]
Blockchain salvou o P2P.

![[Pasted image 20260811210542.png]]
![[Pasted image 20260811210948.png]]
Uso de ferramenta central - mesma relaão de tolerância a falhas e escalabilidade

![[Pasted image 20260811211507.png]]

![[Pasted image 20260811212024.png]]
Software independente separado da máquina - precisa se instalar na máquina pra rodar (security) - pode ser mal intencionado - vírus

![[Pasted image 20260811212852.png]]

![[Pasted image 20260811213418.png]]

![[Pasted image 20260811213602.png]]
Esse tipo de tecnologia estabeleceu abertura de internet das coisas RFID
![[Pasted image 20260811213724.png]]
https://www.totvs.com/blog/gestao-industrial/rfid/

![[Pasted image 20260811214056.png]]
Latência é o tempo pra chegar do sender pro receiver - mensagem de 0 bytes (oficialmente) - header das camadas impedem o 0 bytes oficial
802.3 - rede de ethernet - CSMA/CD -> protocolo pra passar informação pra dentro da rede
Ethernet com Hub dá mta colisão (com muitos sinais)
medição de latência? é só estimável (ping-pong) - ida e volta é roundtrip (lat6encia é só ida - /2)
Lat = tempo mínimo pra abrir o canal de coms (impossível pagar menos que isso) e a soma dos processos de software (header), serialização pra rede e navegação na rede

NFS = Network File System - entra alguns outros conceitos aqui como RPC (Remote Procedure Calls) e segurança e acesso de rede, mas é essencialmente o mounting do esquema de arquivos de uma máquina (qualquer). Nesse sentido, pode ser um linux local ou um servidor de verdade - pra isso existem URLs NFS `nfs://servidor/caminho/arquivo` - bastante utilizado na internet

Utilização de sistemas se dá pela fórmula: **U=λ/μ​** dado que quanto maior a minha capacidade de processamento μ perante um uso (requisições) computacional λ tente à valores baixos de U e vice-versa. Valores muito parecidos (ou iguais) podem levar a sistemas lentos ou até paralização completa de um sistema.

Largura de banda:
B = dados/tempo -> relacionado à vazão
Overhead do UDP - 90-95%
Overhead de TCP - 80-90%

Jitter é redes pura - existe controle de Jitter (tempo entre pacotes)
![[Pasted image 20260818200939.png]]
Controle de jitter esse q é uma fila FIFO

Comunicação síncrona
![[Pasted image 20260818201716.png]]
Tudo dentro da API de sockets
Síncrona bloqueante - 1st espera sempre

Comunicação Assíncrona
![[Pasted image 20260818202325.png]]
Gurizada normalmente bloqueia receiver pq já vai usar na sequência
![[Pasted image 20260818202917.png]]
S {h=Isend(); wait()} e R {recv()} -> é basicamente uma comunicação síncrona
Ideia mais sofisticada:
POO - Objeto Futuro e Espera pela Necessidade
![[Pasted image 20260818204437.png]]
Se o objeto real n chegar à tempo, o programa vai esperar o objeto chegar mesmo
Esconde latência de comunicação
Por cod.:
```java
class Primo 

Integer getPrimo(Integer x);
//receptor necessariamente precisa ser um objeto dado que ele recebe um objeto futuro da aplicação

```

TCP
{
- Dentro de SO
- Bufferização
- Controle de Fluxo 
	- com S e R de velocidades diferentes
	- Transmissores mto rápidos podem gerar mtos pacotes perdidos
	- Receptores mais ligeiros de Senders ñ precisam de controle
- Temporizadores
	- Envio e recepção de ACKs
- CRC
	- Check Redundance Cyclic
	- Corrupção de mensagens
	- garantir dados ñ corrompidos na recepção de mensagem
- Multiplexação
	- Canal de coms compartilhado 
	- temporal {redes}
		- uso da banda por tempo
		- tokenização (round-robin)
	- frequência {AM, FM}
		- ATL - 94.3 Mh -> largura de banda reduzida mas pode transferir continuamente na faixa
- Send/Rec
	- Síncrono
	- Unicast
- Confiabilidade
- Qualquer TAM de mensagem
	- Fragmenta a mensagem automático
- Ordenação (de mensagens)
- TCP tá nas pontas apenas
}

UDP
{
- SW - dentro do SO
- Multicast
	- C/ 1 Send chega em vários Recept - Broadcast
- mensagens pequenas
	- < 64KB -> do contrário pode retornar um erro
- Send/Rec
- Pode perder dados
- mensagem pode chegar fora de ordem
- Desemp. e Experiência
}

Sockets TCP possui coms. sincronia send/receive (fato)
Tem que ter comunic. assíncrona com Sockets TCP? Sim
![[Pasted image 20260818213625.png]]

![[Pasted image 20260818213805.png]]
RDMA - Remote Direct Memory Access

![[Pasted image 20260818213917.png]]

![[Pasted image 20260818214650.png]]

![[Pasted image 20260818215035.png]]
![[Pasted image 20260818215126.png]]
![[Pasted image 20260818215318.png]]
![[Pasted image 20260818215452.png]]
![[Pasted image 20260818215542.png]]
![[Pasted image 20260818215827.png]]
![[Pasted image 20260818220252.png]]