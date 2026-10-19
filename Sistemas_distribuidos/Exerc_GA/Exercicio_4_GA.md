Em duplas, entrega até a prova do GA
1) Descreva vantagens e desvantagens dos três mecanismos de resolução de nomes estudado.
   Dentre os 3 que estudamos, temos:
   - Navegação iterativa - controle central do cliente, mas temos um número limite de consultas e maior geração de tráfego;
   - Navegação recursiva - cliente precisa conhecer apenas um servidor, mas todos os servidores devem implementar a recursão de chamada para os seguintes.
   - Navegação Não-Recursiva - cliente precisa apenas conhecer um servidor e combina o melhor dos dois mundos mas gera implementações mais complexas.
1) Explique um cenário onde o sistema DynDNS pode ser útil.
   O DNS dinâmico pode ser útil para os provedores de internet que utilizam atribuição dinâmica de nomes (DHCP), dado à escassez de recursos IPv4, dentro dos sistemas internos.
2) Na parte de sistema de arquivos, qual a importância do VFS.
   O Virtual File System, geralmente implementado em Unix, tem importância sendo uma interface de abstração e leitura de vários tipos diferentes de sistemas de arquivos em *mounts* diferentes  dentro do mesmo sistema, oferencendo chamadas padronizadas de sistema.
3) Ao analisar a ACL (Access Control List), qual o problema em termos um arquivo com permissão 777.
4) Você vê o sistema NFS como um RCP (Remote Procedure Call)? Explique.