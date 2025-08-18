DATA: 07/Agosto/2025
# Caracterização e introdução
- Ips privados
    - 10 -> rede inteira
    - 172
    - 192.68 ou derivados
    - 169.alguma coisa
        - enderço da máquina
        - auodesignação quando o DHCP ou n existe config na rede
        - vale pra IPv4 e IPv6
- conexões sempre se baseiam no IP de destino
- IP indicado de origem não é público
- ARP é um auxiliar pra puxar o mac address da máquina e estabelecer connection
- sistêma autônomo (intranet)
    - sai por 1 ou mais provedores
    - organização própria
    - BGP
- HUBs usam barramento
    - CSNA/CD
- Switch faz full duplex
    - várias portas
- VLANS são consideradas redes (interfaces diferentes)
    - num Switch dá pra fazer um backbone e passar todas no mesmo lugar
- Datagrama é o sistema TCP/IP
- cada segmentação (pacote) é um datagrama diferente
    - IP origem/destino
    - default - roteamento baseado em IP de destino
- tratamento de dado e voz é bastante diferente
    - voz precisa de QoS
    - algumas tem circuitos dedicados
- OSI é a o modelo mais simples e didático (não é utilizado)
    - feito pra estudo, internet hoje usa TCP/IP
- as camadas se comunicam apenas entre si
- em uma tradução

| TCP/IP              | OSI Model          
| --------------------|-------------------
| Application Layer   | Application Layer
|                     | Presentation Layer
|                     | Session Layer
| TransportLayer      | Transport Layer
| Internet Layer      | Network Layer
| Network Access Layer| Data Link Layer
|                     | Physical Layer

- os headers dos protocolos todos tem todas as camadas embeddadas
- usualmente todo mundo tem uma intranet (rede privada) se tem um modem dentro de casa - praticamente a intranet existe até chegar na concessionária e ir pra internet
- roteadores primeiro roteiam o caminho (dnâmico - datagramas) e depois encaminham (stream de dados/pacotes)
- Datagramas apenas mandam os dados e esperam que eles cheguem no destino (pra UDP)
    - TCP/IP ainda tenta mandar um ACK pra saber que o destino existe
        - mas não é uma conexão virtual direta
- 


DATA: 14/Agosto/2025
# Topologia IPv4
- Na camada de rede (IP) temos a seleção de melhor caminho pelo sistem
- rede da unisinos é um sistema autômo
    - não recebe IP do exterior - dona dos IPs
    - Pode até vender
- IP não trata de perda de pacotes - camadas superiores resolvem (TCP)
- Ethernet normalmente consome 1500bytes
    - padrão
    - Existe o Jumbo frame - 9000 bytes
- os pacotes precisam ser todos unidos no destino antes de mandar pra camada de transporte
    - caso contrário é td descartado
- subredes usam as máscaras de rede
    - subredes tem o endereço de host (.0 -> tds os bits em zero) e endereço de broadcast (.255 -> todos os bits em 1)
    - o barra significa quantos bits tem o valor 1 na máscara
    - 

por que /30 considera 2 IPs?
os roteadores veêm apenas os vizinhos imediatos ou as redes deles também
por que com uma rota é /24?
