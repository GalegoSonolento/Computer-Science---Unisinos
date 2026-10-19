1) Por que sistemas em rede são organizados em camadas?
   Dados sistemas de rede são organizados em camadas de forma à demonstrar o acoplamento de headers entre as ditas camadas e demonstrar interfaces claras entre as ditas camadas, à fim de facilitar a comunicação entre tecnologias. À cada camada que o pacote desce, é adicionado mais um header para identificar a determinada camada e suas configurações (e.g. de leitura). O mesmo pode ser dito quando o pacote faz o caminho contrário. Essa organização facilita manutenção, substituição de protocolos e interoperabilidade do sistema.
2) Quais as vantagens da arquitetura "Computador em Rede"?
   Com computadores em rede temos algumas vantagens adicionais; como recursos externos à nossa máquina (GPUs, repositórios de memória, etc), independência de estação (posso logar em qualquer máquina da rede que ainda tenho acesso aos meus dados), acesso à imagens do sistema para instalação, etc.
3) Por que a arquitetura cliente-servidor tem problemas de escalabilidade?
   Cliente-servidor é um arquitetura que demanda uma central, ou melhor, um servidor central, por onde todas as requisições passarão. Enquanto tivermos esse gargalo de computação, tanto na capacidade de processamento quanto na largura de banda, teremos problemas para escalar. Para além, alguns sistemas se baseiam em comunicação síncrona, que agravam esse gargalo.
4) Por que replicação funciona bem quando a maioria das operações forem de leitura?
   Replicação tende a funcionar bem com leitura devido ao fato de as informações não precisarem de alterações. A forma que a replicação funciona é como num cache e, quando alterações aparecem no arquivo original, preciso passar em todas as réplicas enviando a mesma alteração. Sistemas com replicação que fazem muitas escritas (razão _read-to-udpate_ alto) tendem a perder a vantagem dessa por causa desta, abusando a largura de banda.
5) O que você entende pelo processo de reflexão.
   Nesse contexto, reflexão é quando, em uma serialização de um objeto java, por exemplo, o programa é capaz de reconstruir objetos inteiros à partir de seus nomes, muitas vezes feito recursivamente.

**Implemente:**
1) Código RMI, execute e comente o código e a execução. Pode ser qualquer código.