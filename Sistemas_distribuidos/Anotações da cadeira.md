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
RPC é uma abstração de Sckets basicamente

Paradigmas e Computações
![[Pasted image 20260825203158.png]]
**Comunicação indireta** -> aplicações no meio do caminho salvam ou administram requisições
Email é coms indireta, por exemplo (tem um server no meio)
![[Pasted image 20260825204112.png]]

**Comunicação Pub/Sub**
![[Pasted image 20260825212023.png]]
Servidores centralizados sempre servirão para todas as tarefas e geralmente mostrarão outros problemas relacionados
![[Pasted image 20260825212309.png]]
Publish/subscribe distribuído
![[Pasted image 20260825212537.png]]
Um dos problemas do flooding é uma mensagem loopar e circular eternamente dentro da rede
	Solução normalmente é largar um ID nas mensagens - os nós verificam aquele ID e vêem se ele já passou por eles, se sim descartam
	Importante ter um líder dentro da arquitetura/rede - faz definições de IDs por exemplo
![[Pasted image 20260825213244.png]]

Message Queues
![[Pasted image 20260825213331.png]]
![[Pasted image 20260825213545.png]]

Presença de grana noramalmente mora na amazon ou na Google
![[Pasted image 20260825213809.png]]

![[Pasted image 20260825215053.png]]Configuro dentro do DSM (o software), mesmo com máquinas heterogêneas, pra ele administrar os endereços locais das máquinas e quais são os abstraídos do software dele.
![[Pasted image 20260825215310.png]]

![[Pasted image 20260901194210.png]]
**DNS** - nomes importantes dentro do contexto de computadores
Identificação de modos e métodos é toda feita aqui
![[Pasted image 20260901194751.png]]
![[Pasted image 20260901194809.png]]
![[Pasted image 20260901200405.png]]
![[Pasted image 20260901200531.png]]
![[Pasted image 20260901201107.png]]
![[Pasted image 20260901201408.png]]
![[Pasted image 20260901201625.png]]
Desses métodos o delineado é instituido na chamada pro primeiro server. Depende dessa chamada pra saber como que ele atua. O NS ou retorna tem/n~tem ou diz que tem/trabalho iterativo, toma outro server.
O cliente se vira dependendo da primeira reply do 1st server.
Mais usado é o recursivo mesmo (dominância)

cliente - iterativo
servidor - recursivo
servidor - não recursivo

![[Pasted image 20260901202954.png]]
Aqui ele pode faezr um DNS reverso - o resolver tenta resolver o IP do nome que chega pra ele - pra email ele pega a credencial do server que mandou a req e vê se ele existe de fato.
![[Pasted image 20260901203606.png]]
![[Pasted image 20260901203805.png]]
![[Pasted image 20260901204127.png]]
![[Pasted image 20260901204704.png]]

ACL - Access Control List:
O número **740** assume significados completamente diferentes dependendo de onde está sendo aplicado: em um sistema operacional (como o Linux) ou em um equipamento de rede (como um switch ou roteador Cisco).

**1. Em Sistemas Operacionais (Permissões Linux/Unix)**

No Linux, o controle de acesso a arquivos e diretórios usa um sistema numérico baseado em somas. O número 740 é lido da esquerda para a direita, dividindo os acessos em três grupos de usuários:
 
- **7 (Dono do arquivo):** Tem permissão total. O número 7 é a soma matemática de **Ler (4) + Escrever (2) + Executar (1)**.
- **4 (Grupo do arquivo):** Tem permissão restrita. O número **4** significa apenas **Ler**. O grupo não pode alterar nem executar o arquivo.
- **0 (Outros usuários):** Não tem permissão nenhuma. O **0** bloqueia qualquer tipo de acesso.
**Como o sistema lê:** _"O dono do arquivo pode fazer qualquer coisa com ele, o grupo de usuários atrelado ao arquivo só pode visualizá-lo, e qualquer pessoa de fora do grupo está totalmente bloqueada."_

**2. Em Roteadores e Switches (Padrão Cisco)**

Nos equipamentos de rede, os números das ACLs não representam permissões matemáticas, mas funcionam como **etiquetas de identificação** que dizem ao roteador qual cabeçalho ele deve inspecionar. O sistema operacional da rede (Cisco IOS) reserva faixas de números para cada tipo de protocolo:
- 1 a 99: ACLs para IPv4 Padrão.
- 100 a 199: ACLs para IPv4 Estendida (IPs e Portas).
- **700 a 799: ACLs para Endereços MAC (Camada 2).**

**Como o roteador lê:** Quando você digita a criação de uma `access-list 740`, o roteador automaticamente entende: _"O número 740 está na faixa de 700 a 799. Portanto, eu vou ignorar os endereços IP (Camada 3) e as portas TCP/UDP (Camada 4). Vou filtrar esse tráfego olhando exclusivamente para os endereços físicos (MAC Address) das placas de rede."_
![[Pasted image 20260901212330.png]]
![[Pasted image 20260901213010.png]]
![[Pasted image 20260901213257.png]]
![[Pasted image 20260901213601.png]]
![[Pasted image 20260901213809.png]]
Problemas dessas caras são os problemas de computação pela rede - ainda tem server centralizado (problema de escalabilidade e segurança).
NFS funciona bem quando 90+ operations são de read - se forem mtos writes o NFS é pouco performático.
	Pra resolver esse problema: 
	![[Pasted image 20260901214249.png]]
	Computadores velhos tem HDs pequenos, dá pra transformar isso tudo num Storage Area Network (SAN) e ofereço como um HD gigante único (software - HD grande lógico) oferecido pro cliente. 
		Salvo mtos computadores assim
		Tem semelhanças com Distributed Shared Memory - oferece a semântica de HD grande, mas particionado
		Permite leituras simultâneas se diferentes HDs do lógico estejam em uso.

---
**Criptografia e Segurança**
![[Pasted image 20260908195514.png]]
![[Pasted image 20260908195604.png]]
RSA ainda é a melhor arquitetura de chave, mas elas precisaram crescer substancialmente pra segurar o padrão
![[Pasted image 20260908200432.png]]
![[Pasted image 20260908201053.png]]
![[Pasted image 20260908201736.png]]
Gurizada ainda usa pela simplicidade de entregar as chaves e pela rapidez pra montar e desmontar a criptografia (hoje ainda é rápido computar essas chaves)
(não abordado em sist. dist.) segurança em engenharia social
![[Pasted image 20260908202406.png]]
![[Pasted image 20260908203316.png]]
OpenSSL é camada de aplicação
![[Pasted image 20260908204910.png]]
Problema de assinatura ainda persiste (remetente não identificado)
Atualmente a gurizada pega as chaves assimétricas pra settar o canal seguro pra mandar a chave simétrica e espabelecer uma comunicação

![[Pasted image 20260908211201.png]]
![[Pasted image 20260908211701.png]]
Sempre se assina Hash - Assinatura Digital é bastante complexa - Hash é mais ligeiro de assinar pra mensageria

Apesar de Assinatura Digital com criptografia, ainda não dá atestar quem um usuário diz ser
Dentro de certificados tem chaves públicas - precisa ir nas entidades certificadoras pra certificar chaves públicas
Nos certificados tem chaves públicas e a validade -> root de segurança

