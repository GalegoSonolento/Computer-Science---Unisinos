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
- a internet é descentralizada
    - caso não o fosse poderia ser problemática
    - não seria tão escalável quanto é atualmente
    - era possível, mas o departamento de defesa queria algo desse tipo
    - programação *best-effort* -> não é confiável (IP)
        - quem resolve esses problemas são as camdas superiores
- os fragmentos possuem identificação dentro da rede e sempre precisam avisar o receptor se mais estão à caminho
- para comunicação, todos os dispositivos precisam de um endereço IP
    - é possível a comunicação com o endereço MAC ou um IP designado para pedir um IP ao roteador (quem controla e limita os IPs)
    - nesse *range* de IPs, o primeiro e o último são reservados
        - 223.1.1.0 -> endereço de rede
        - 223.1.1.255 -> endereço de broadcast
        - não necessariamente esses endereços serão com o final .0 ou .255
            - redes mescladas (somadas) podem ter esses endereços como HOST tranquilamente
        - uma máscara 223.1.1.0/24 significa que 24 bits mais a esquerda definem o endereço de rede e o resto o endereço de host
            2-4-8-16-32-64-128-**256** endereços de host.
- DHCP *Dynamic Host Configuration Protocol*
    - protocolo de internet
    - cliente-servido
- timestamp sempre tem 32bits
- 

DATA: 21/Aug/2025
# Roteamento - Conceitos iniciais
- forma da informação chegar no ponto A até o ponto B
- menor distância não é necessariamente o caminho mais curto (número de saltos)
    - o número de banda pode variar bastante
- nem sempre as entidades de backbone são operadoras
    - existem inter-operadoras
        - VIVO chegar até a AT&T
- ISP - Tier 3
    - próximo do user
    - normalmente empresas
- ISP - Tier 2
    - só conecta grandes usuários e operadoras
- ISP - Tier 3
    - vazão de banda
    - conexões grandes
- IXP
    - Internet Exchange Point - PTT - Ponto de Troca de Tráfego
    - links contratados de conexão entre operadoras
    - quando operadores contratam tiers mais altos elas precisam pagar
- roteamento
    - direto
        - tier 1 e 2
        - host destino na mesma rede
        - pega o endereço IP e máscara pra ver se está na mesma rede
            - IP binário
            - máscara binária
            - operação AND
            - se o resultado do IP host AND máscara for igual destinatário AND máscara -> é a mesma rede
    - indireto
        - fora do mesmo segmento de rede
        - vai pra um gateway
    - intra-domínio
        - dentro da operadora
        - datagramas passam por dentro da operadora
    - inter-domínio
        - levando pra outro sistema autônomo (e.g. outra operadora)
- quanto mais próximo da ponta, menos dinâmico e menos dependências de protocolos
    - inverta quando estiver entrando
- usa-se o endereço MAC do default Gateway
    - Layer 2
- equipamentos físicos reais com tables de roteamento
    - se o roteador vê que não é pra ele, ele precisa escoar pra alguém
        - decisão feita com base na table de roteamento
- operadores normalmente escondem os IPs mais específicos por segurança 
    - começaram a colocar IPs privados pra gerência do roteador
- table de roteamento != table de encaminhamento
    - seleção de melhor caminho
    - tables têm endereços de rede não de hosts
    - quanto mais pra dentro, mais genérica é a rota
- próximo passo é usar o IP destino
    - varia de algoritmo - pode nao conhecer o caminho completo
- protocolos diferentes podem dar subsídios para outros
- diretamente conectado - rota estática - table de roteamento - métrica de roteamento (pesos - podem ser alterados para mudar comportamento)
- como essas tables são montadas
    - no mínimo reconhece as interfaces pra colocar o default
    - algoritmos de roteamento
    - host final tem rota por ThCP
        - o problema é a rota entre roteadores
    - tabela de roteamento é montada igual q qql forma
    - roteamento estático fica extremamente complexo pra redes médias já
    - dinâmicos pode aumentar as redes e manter o funcionamento
        - vetor distância
            - grande problema é como a informação se propaga para todos os equipamentos
                - tempo de adaptação -> protocolo bastante lento
            - os vizinhos pegam as tabelas dos vizinhos e trocam figurinhas
                - espalhamento de tabelas -> flooding
                - o problema é se alguma coisa cair
        - estado de enlace
            - monta um mapa topológico em estado de link
            - peso
            - banda
            - etc
            - OSPF - Open Shortest Path First
            - troca informações somente entre roteadores imediatamente ligados a eles
            - SPF - Shortest Path First
                - Dijkstra e anúncios pra criar a topologia
        - vetor de caminhos
            - labels -> determinação do sistema autônomo
            - caminhos pré-montados por sistemas autônomos
            - prfixo de rede
            - BGP - Border Gateway Protocol
            