Universidade do Vale do Rio dos Sinos - Unisinos
2024/1 - Redes de Computadores: Aplicação e transporte
Henrique Vinicius Haag
|-------------------------------------------------------------------|

Redes sem fio e Telefonia IP
- Início das telecomunicações sem fio em 1890 - Nicola Tesla
- sec XX - meios militares (gurras basicamente)
- Redes AM/FM fazem parte constante disso
- IEEE 802.11 -> padrão de uso do wi-fi (2000)
    - WLANs - Lan sem fio
    - 2.4 - 5 (ou 6) GHz
    - padrões de seguranças mais antigos 
        - WPA e WPA2 - mais recentes
    - Padrões mais modernos de rede procuram evitar os conflitos de vários tipos de sinais no mesmo ambiente (densidade de sinal)
- Telefonia IP funciona por fora da telefonia padrão, usando a internet pra isso
- Qualidade de Serviço (QoS), e segurança são problemas constantes em telefonia
    - comunicações live são mais complexas de criptografar
    - Compliance e ISO variam de país para país
    - Integração com sistemas legado e comunicação com a estrutura de rede antiga
- 6G já está em fase de projeto

|-------------------------------------------------------------------|

Aplicações Multimídia e Protocolos RTSP, RTP e RTCP - Evelyn Tag e Pedro Fleck
- Real Time Protocolo (RTP)
    - transporte multimídia em tempo real
    - pode transportar dados de simulação
    - não garante qualidade de serviço
    - usado com RTCP
        - ambos enviados separadamente
    - sessões separadas de áudio e vídeo
        - utiliza um misturados
        - funciona como um euqlizador de sincronização para as diferentes qualidades de rede
    - tradutor 
        - para bypass em firewalls
        - tradução e retradução para entender no destino
    - padding
        - octetos de informação
        - funcionam para controlar tamanhos dos algoritmos de criptografia
- jitter
    - equalização do atraso dos pacotes recebidos
    - a rede não é perfeita e pode existir variações de envio
- RTCP
    - transmissão de grandes quantidades de dados para vários receptores
    - manda relatórios de qualidade de envio
    - tem um demon que fica apenas observando essas qualidades
    - manda informações para os transmissores equalizarem a transmissão
    - CNAME é um endereçamento pra sincronização de áudio e vídeo
- RTSP
    - camada de apicação
    - controle de compatibilidade
    - controle de sessão
    - Realnetworks e Netscape (firefox!)
    - DESCRIBE, OPTIONS, PLAY, PAUSE, RECORD, REDIRECT, SETUP, ANNOUNCE, TEARDOWN
    - reqisita TCP (pode ser UDP)
    - DESCRIBE
        - SDP
            - IP
            - porta
            - mídia
            - cod
            - protocolo de apliação (RTP)

|-------------------------------------------------------------------|

VPN: IPSEC - Patricia e Rodolfo
- VPN - Virtual Private Network
    - rede privada em cima de uma pública
    - tunelamento
        - tunel entre vários roteadores
        - mensagens com criptografia pelo tunel
    - enciptação 
    - se o ataque é identificado ele destrói o tunelamento e cria outro
- IPSEC
    - tunelamento na 3° camada de rede
    - framework da IETF
    - IKE, AH e ESP
    - topologias G2G e C2G
    - mode transporte
        - criptografia do pacote e cabeçalho original
        - conexão direta entre os hosts
    - túnel
        - criptografado
    - puxa pela confidencialidade
        - criptografia
    - integridade   
        - protocolo impede pacotes alterados de chegarem ao destinatário
    - atenticação
        - só manda se a origem e o destino forem autenticadas propriamente
    - Authentication Header (AH)
        - no transporte ele coloca um header novo por baixo do cabeçalho de IP original
        - no túnel ele fica por cima do IP e cria um novo por cima dele ainda
    - Encapsulating security payload (ESP)
        - encapsula os cabeçalhos e os embaralha para dificultar a vida de invasores
        - vai encriptar o AH
        - autentica tbm
    - Internet Key Exchange (IKE)
        - troca de ordem de pacotes e inversão de alguns sinais 

|-------------------------------------------------------------------|

Arquiteturas P2P - Vicenzo, Vicenzo e diogo
- cada nó coopera entre si
- sem necessidade de servidor principal
- similar à ARPANET
- Napster
    - rede própria
    - compartilhamento de músicas 
    - 8milhoes no auge
- BitTorent
    - Bram Cohen
    - quebra o arquivo em várias partes e pega partes do arquivo de vários lugares
    - depois o cliente vira servidor e semeia os files
- eles precisam reconhecer os vizinhos na rede
- rede sobreposta na internet
- redes estruturadas
    - existe algo conectando os pares
- não estruturada
    - os pares se viram para encontrar outros
    - todas as pesquisas são por flooding
- algumas estruturadas existem supernós
    - servidores de centralização e indexação pra organização dos files
- tipos de busca
    - servidores principais indexadores e conexão entre os dois computadores
    - Gnutella - sem centralização e chuta os pings e queries para encontrar os servidores

|-------------------------------------------------------------------|

Internet das Coisas - IoT
- trabalha com disponibilidade de recursos e adequação de recursos
- diversos protocolos podem ser implementados, mas variam quanto á forma e necessidade 
- AMQP - baseado em TCP
- MQTT - tbm baseado em TTCP
    - assinatura e propagação de informação
    - baixo consumo de banda
    - simples
- dá pra usar http no IoT
    - é esse mesmo
- CoAP - baseado em UDP
    - inspirado no http
    - a finalidade é pra ser leve e funcionar em conexões instáveis
    - ele mesmo implementa recursos de controle de rede
- Bluetooth
    - é IoT tbm
    - frequências de rádio
    - Bluetooth low energy
- 6LoWPAN
    - trabalha com IPv6
    - pode ter massas grandes de dados passando por ele mesmo em dispositivos fracos
- Zigbee
    - parece bluetooth e wi-fi
    - precisa de um hub para funcionar
    - evita sobrecarregar o roteador
    - alcance bem baixo
    - fácil de implementar

|-------------------------------------------------------------------|

TCP para Redes sem Fio
- 1970
    - ALOHANET
        - protocolo ALOHA
        - HAWAII
        - se tem dados é pra enviar
        - se receber um dado enquanto recebe ele tá quebrado
        - rapidez bem baixa
- assim como nas redes cabeadas, sem fio também sofrem de congestionamentos frequentes
- I-TCP
    - inderect TCP / split TCP
    - meio de campo entre a cabeada e a sem fio
    - tratamento é feito por um Access Point que evita problemas da rede sem fio baterem na rede cabeada
    - se ocorrer perda de pacotes ele retransmite o pacote sem precisar pedir pro servidor de novo
    - access point pode segurar melhor o gerenciamento de usuários
        - distruibuição de handover entre os access points
- TCP Snoop
    - fica no meio da rede "bisbilhotando" os pacotes entre o host e o equipamento móvel
    - se tomar 2 ACKs considera perda de pacote
        - pega um do buffer e manda dnv
    - pode ser ineficiente se os pacotes estão encriptados
    - Notificação de Perda Explícita (ELN)
        - tentar avisar o remetente da causa de perda de pacote
        - não ignora sugestoes de rede
        - evita subutilizar a rede
- TCP Hybla - alta latência e banda variável

|-------------------------------------------------------------------|