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
