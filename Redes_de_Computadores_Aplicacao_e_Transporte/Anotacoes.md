Anotações da cadeira

# Conceitos universais
- rede n funcional n é mais uma rede
- internet - núcleo de liga~çao de borda - rede q liga redes
- usar como infraestrutura n é trabalhar com ela
- cabo de par trançado n pd ter mais de 100 metros
    - ou dobrar > 45°
- sinal 5G é fraco, corpo humano barra
    - dentro dela n dá pra ver a 2,5G
    - são duas redes diferentes dentro do transmissor
- servidor em rede é um prestador de serviço
    - um celular mandando uma msg é um servidor tbm
- onda de rádio é um meio físico
    - preciso de controle do meio físico pra transmissão
- transmissões
    - simplex
        - só um lado faz a transmissão
    - half-duplex
        - só um pode falar por vez
        - walkie-talkie
            - controle de meio
    - duplex
        - coms duplas
        - telefone
- maioria dos pacotes n criptografam
- dois sinais na mesma rede é a física básica de ondas
    - se amplificar pode queimar alguma coisa
- o roteador de casa é um roteador de borda, mas essecialmente ele é só um switch
    - primeiro roteador, na borda da Net
    - trabalha como switch na camada de enlace
    - o roteamento é só com outro roteador
- enlace é uma ligação física entre as máquinas
- rede cabeada e wi-fi são diferentes (n tem rota)
    - alguns fazem um bridge entre as duas redes
    - com bridge vai ser sempre a 5G por ser mais rápida e n derrubar a latência do resto da rede
        - velocidade baseada no mais lento
- preocupação atual de rede é streaming 
- Aplicação de internet é uma aplicação distribuída
- tempo de carregamento online é troca de server
- normalmente velocidade é o parametro de desempate
    - ás vezes precisa de aplicação com mais espaço
- não dá pra transmitir dois sinai na mesma frequências no mesmo canal
- nunca use uma informação de regra de negócio pra arquitetar nenhum sistema
- o controle das informações da rede é feito completamente pela rede - os OS n tem nada a ver com isso
- Um 'ack' é uma confirmação de resposta do par de dados enviados
- checksum tá em basicamente todas as camadas


DATA: 29/02/24
# Introdução a redes de computadores
- ideia básica de redes surgiu por causa dos mainframes
    - um mainframe gigante e vários terminais burro
    - isso e uma arquitetura pai de redes
    - esse troço ficou mto lerdo e resolveram quebrar o processamento
- necessidade de rede era pra compartilhar recurso
- comuniação de rede é toda por pulso de luz
    - a voltagem tem espaços de volts pra análise
Redes hoje em dia não necessariamente são compostas apenas por computadores. Ficou bastante comum o uso de microcontroladores e outras peças de hardware que não são exatamente computadores. Vide os sensores coectados na rede.
Já meio batido mas para deixar claro, as redes funcionam com trocas de bits entre os computadores e a rede. Precisa-se converter o sinal na entrada e na saída.
## Evolução de rede
- depois de montagem de rede ela teve uma fase alta e continuou desenvolvendo
- trocar info cada vez mais rápido - menor custo facilita
- internet era uma segunda linha de coms pra manter os EUA em pé em caso de invasão de quebra das comunicações telefônicas
    - caminhão de dinheiro federal pra montagem da arpanet
A necessidade de uma rede alternativa à telefônica era por motivos bélicos, mas se tornou uma ferramenta indispensável na mão dos civis. 
A troca de informações barata e rápida com compartilhamento de informação e recurosos supera bastante a da rede telefônica.
### preocupações de rede
- transmissão precisa ser com luz, piscando, e o receptor precisa ser bom o suficiente pra pegar e o envio precisa ser sinconizado o suficiente pra n atrasar
- inicialmente todas as redes eram corporativas
    - transmissão de pulso era em cima de rede telefônica
    - já existiam alguns tipos de rede pessoal
## Tipos de redes

dist. entre proces | proces. no mesmo 
:-----------------:|:-----------------:
       0.1 m       | Placa-msm pc      
         1 m       | Sistema-multicomp 
        10 m       | Sala-rede local   
       100 m       | Prédio-rede local 
         1 km      | Campus-rede local 
        10 km      | Cidade-MAN        
       100 km      | Estado/País-WAN   
      1000 km      | Continente-WAN    
     10000 km      | Planeta-Internet  

## Visão geral de rede
- transmissor (origem)
    - geralmente é dinâmico (pode enviar e receber)
- receptor (destino)
    - mesmo caso do transmissor
- dado enviado/recebido
    - em binário
- canal de coms (link)
    - transporta o dado
- interface - conexão da máquina no meio físico
    - precisa de um meio físico - wifi tbm tem (onda)
    - pega o pulso e transforma em binário
## Rede local
- LAN - Local Area Network
- são privadas por definição
- tamanhos definem LAN
    - se n precisa de roteamento ainda é uma LAN
- taxa de erro baixa por n ter roteamento - broadcast - transmite pra todos
### Topologia
- maneiras de ligar uma rede
- estrela
    - 90% da conexão
    - um switch centralizando a coms da rede
    - se derrubar o centro mata a rede
- barra
    - velha
    - barramento com td mundo ligado lá dentro
    - conector vampiro
    - todo mundo recebe a msg
    - n podia ter duas transmissões ao msm tempo
- anel
    - msg em único sentido
    - token
        - quem tem podia transmitir
## Redes metropolitanas
- transmissão de sinal de wi-fi é um barramento
- td mundo recebe a informação
- MAN - Metropolitan Area Network
- o próximo passo da rede é conectar a rede com outra rede
- necessita de criação e rotas
- rotas diferentes pra chegar em algum lugar
### Topologia
- DQBD (Dristributed Queue Dual Bus)
Aqui dois cabos interligam os computadores, um para cada direção, não existe um barramento único ou um anel entre eles.
## Redes geograficas distribuidas
- internet foi feita com infra de telefonia
- WAN - Wide Area Network
- qql coisa gera interferência
    - redes grandes podem usar rádio em alguns momentos
- logicamente tem roteamento
- internet é um modelo de WAN
    - ou pode ser um miolo da porrada de rede
    - sem acesso de borda a internet n funciona
Esse tipo de rede não tem necessariamente um único tipo de topologia, ela pode usar múltiplas inclusive.
O roteamento de dados aqui é imprescindível, uma vez que roteamento mal feito pode atrasar muitas partes do sistema.
## Redes sem fio
- cresce absurdamente
- custo de infra é bem menor
- segurança ainda é problemática
    - barramento mto simples - sinal compartilhado
O maior investimento na área de rede sem fio é em segurança, já que é um barrameto bastante simples. Ha não muito tempo era possível escutar (colocar o computador em modo promíscuo) diversos emails e compartilhamento de dados caso estivesse em um ambiente muito movimentado (aeroportos por exemplo).
A maioria das soluções nesse sentido estão na área mais high level, de software e aplicações com criptografia de ponta a ponta.
## Internet
- se levar em conta qql sensor ou IoT tem bilhões de disp dentro dela
- equipamentos são sistemas terminais/hosts
- aplicaçções de internet são programas de aplicação de rede 
Existe uma grande discussão se a internet é ou não uma rede ou um hub de várias redes. A resposta provavelmente está no que ela seria sem um monte de redes de borda para alimentá-la, nada, porque ela não "existe" de verdade.
### Componentes da internet
- Cabos coaxais/fibra óptica/cabos normais de rede
- TCP/IP - são dois protocolos diferentes
- protocolos tão tds prontos
- redes em 4 camadas
- links são enlaces -> tempo do disp até o access point
    - eles formam a rede basicamente
    - uso de meio físico
- equip de comutação
    - troca
    - infindável
    - serve pra trocar pacotes
    - quando o pacote chega lá a linha morre
    - roteadores (routers)
        - quem faz a comutação
A distribuição de rede é levemente hierárquica, o que significa que existem apenas alguns componentes e camadas de comunicação. A maioria delas é referente à componentes de borda.
### intranet
- intranet são redes isoladas de internet
- internet privada.

DATA: 07/Mar/2024
- Provedores de Serviços de Internet (ISP's)
    - é um provedor 
    - pdser um de borda ou ISP regional pra coectar regiões e ir pra fora
### tipos de Serviço
- orientado a conexão
    - garante envio correto
    - 
- nã-orientado a conexao
    - n necessariamente garante informação chegando certo do outro lado
    - streaming usa esse tipo de informação
        - velocidade é mais importante q confiabilidade
    - evita bastante latência

## Entidades básicas
Uma das premissas da rede é que qualquer comunicação entre as máquinas pode ser cliente-servidor para qualquer um dos lados.
Dessa forma, um dos pontos são os diferentes tipos de servidores:

Tipo           | Função
:-------------:|:--------
Arquivos       |  Serviços de armazenamento e acesso às informações
Banco de dados | BDs e processos de consulta
Impressão      | Serviços de impressão
Comunicação    | Procedimentos de acesso à rede e interface com os dispositivos dos usuários
Gerenciamento  | Tráfego da rede, desempenho, identificação de falhas
...            | ...

- sempre vai ser comuniação cliente e servidor
- dá pra saber claramente a rota e os domínios
- modelo de predomínio na internet
    - servidores dedicados
- hosts:
    - clientes
        - estações de trabalho normais
        - pedem determinado serviço
    - servidores
        - mais forte pra prover serviço pra tds
        - mais processamento
- aplicação distribuída só significa q a aplicação n tá salva no cliente 

## Meio de transmissão
O meio físico é indispensável dentro do esquema da rede, por isso existem algumas diferentes formas de transmissão de informação.
Usualmente essa comunicação é feita com pulsos elétricos ou raios de luz. 
- sempre tem um caminho físico
    - guiado
        cabo coaxal, fibra óptica
        - toda capacidade é distância e tipo da rede
            - cabos tem distância de garantia de conexão
            - a tensão pdser n chegar
        - transmissão bit/segundo
### cabo coaxial
- transmissor de entrana no meio e um outer conducter por fora
- tem um isolante no meio
- largura depende do tamanho do cabo
- cabos de 1km chega a 1 ou 2 Gbps - garantido
- bidirecional
- substituição por fibra óptica
### cabo de par trançado
Normalmente esse tipo de cabo é usado na última milha - muitas vezes entre o switch/modem de borda a as máquinas.
- UTP Unshielded Twisted Pair
- STP (Shielded Twisted Pair)
- categoria 3 a 7 (7 é Ethernet de 10Gb)
### cabo de fibra óptica
- fibra de vidro ultrafina
- pulso de luz (lazer)
- Ethernet de 100 Mbps
- transmissão de alta velocidade
- qualidade deve ser bem alta
- situações mto extremas estragam o cabo (ressecamento)
- tem um núcleo com uma capa reflexiva (casca) pra n perder sinal
- quase na velocidade da luz
- normalmente quebra fora da casca

### Não-guiados
- atmosfera ou espaço
- satélite, infravermelho, microondas
- precisa de um direcionamento das antenas
- direcionada
- bem menos seguro
- usa onde precisa
    - deserto, pântano, difícil acesso
#### satélites
- 50Mbps - único problema é a latência
#### microondas
- ondas de rádio
- interferência pacas
    - em frequências altas
- 155Mbps
#### infravermelho
É tão terrível que nem os controles com funcionalidades em infravermelho funcionam corretamente.
Para isso ser viável e necessário 
- desgraça

## Protocolos
Regras de comunicação entre os computadores/dispositivos.
As máquinas precisam de alguma maneira de entender o que aquele conjunto de bits significa, para tal, eles precisam ser organizados de uma certa maneira.
Essa é uma das premissas de os arquivos terem extensões e cabeçalhos.
- conjunto de regras de coms
- o q é o primeiro bit
- definem formato e ordem de mensagens 
- divide entre sinalização e informação
    - msg de conexão tem bem mais sinal q info 
- overhead - informações a mais de cabeçalho
    - protocolos diferentes tem cabeçalhos completamente diferentes
    - n considerada na velocidade efetiva da coms

### Camadas de protocolo
- programação de camadas
- separação de camadas facilita na hora de atualizar e montar diferentes tipos de camadas
- melhor maneira de montar sistemas complexos
- Modelo Ozi é o ideal (referência) de rede - mas a maioria é TCP/IP
- cada camada fala com ela mesma no outro lado
- camadas de baixo presta serviço pra td mundo
- o request vai descendo e conforme vai as informações das camadas acumulam, quando chega no destino ele sobe
#### Aplicação
- app
- ftp, smtp, http
#### Transporte
- TCP, UDP
- transportes entre terminais
- bota no processo correto
#### Rede
- IP
- rota
- comunicação com máquinas distantes
#### Enlace
- PPP, Ethernet
- lig de 2 pontos
#### Física (tá dentro do enlace)
- modulaão de bit no meio
#### Hierárquicos
- um monte de etapa vinculada uma com a outra 

DATA: 14/Mar/24
## MOdelo de camadas
- Modelo OSI (de referência)
- criado por universidades européias
    - modelagem acadêmica
    - mais pensado antes de executar
- funcionaria pra qql tipo de rede e protocolo
- na coms lógica só o receptor se preocupa em entender
    - só quem abre é a msm camada na outra máquina
- primeira boa versão veio depois q o TCP/IP tava bombando
    - http foi pensado pra funcionar em TCP/IP
    - internet era mais simples q o modelo OSI
- n necessariamente precisa usar todas as camadas
    - n tem roteamento em LAN
    - rede n deve exigir todas as camadas
### nível físico
- transmissão de bits pelo meio físico
- detém o controle de acesso ao meio 
### nível de enlace
- quadros (frames)
- detecta erros de transmissão e pode tentar corrigi-los
- parte em software outra em firmware - permanente dentro da placa de rede
### nivel de rede
- roteamento e localização
- sedex do processo
- entrega como o processo certo
### nível de transporte
- preocupação entre os dois pontos finais
- quem localiza e entrega a mensagem
- gerenciamento de processos
- cuida da ordem certa pra entrega na aplicação
### nível de sessão
- tempo máximo de interação
### nível de apresentação
- formatação dos dados pra aplicação
- compressão de dados e descompressão seria aqui
    - inclusive criptografica
    - aplicação n precisa entender nada
### nível de aplicação
- terminal
- jogo
- etc...
- criação dos programadores

### TCP/IP
- aplicação
    - FTP (arquivo), SMTP (email), HTTP (web)
- transporte
    - TCP (conexão), UDP (transferência não confiável - não existe no modelo OSI, n entra nos parâmetros, serve só pra transmissão de dados rápida)
    - garantir q a msg chega no nível de transporte pode gerar uma lentidão pq o protocolo precisa cuidar do reenvio do pacote
    - identifica as portas abertas das aplicação e entrega os pacotes (se a aplicação existir, caso contrário o pacote é descartado)
- rede
    - IP
- enlace (junto do físico)
    - arestas da rede
    - ligações entre os hosts
    - PPP, Ethernet
- físico
    - bit no cabo

### coms
- cada camada consegue ver o q a outra camada fez
    - comunicação horizontal
- Overhead é o cabeçalho da informaçao e vem de cima
    - comunicação vertical
- roteador só abre a rede pra saber onde precisa mandar

### camadas e protocolos de dados
- comunicação é sempre com socket
    - são as portas entre as camadas
- dados gerados são mensagens
- cada camada mete um cabeçalho em cima (uma porta)
    - aplicação envia dados pras camadas abaixo - mensagem
    - transporte tem a porta da aplicação e quem tá mandando - segmento
    - ordenação da mensagem
    - rede precisa saber o tempo de vida dele (pacote pode se perder) - datagrama
    - enlace precisa do sabeçalho dele pra fzr validação de erros - quadro 
- aplicação cuida da camada de sessão

## atrasos
- pra cada enlace
    - 5 tipos diferentes de atrasos
        - dproc - processamento nodal
            - precisa abrir todos os cabeçalhos e identificar pra onde precisa mandar
            - pequeno hoje em dia
        - dqueue - enfileiramento
            - filas podem ser grandes no buffer
            - pode ser 0 se n tiver ngm na fila
        - dtrans - transmissão
            - tempo pra colocar os bit no enlace
            - tempo pra colocar o fluxo de bits dentro da rede
            - Taxa R - largura de banda
                - Ethernet - 10Mbps, taxa de R=10 Mbps
            - aumenta com uma taxa de transmissão menor
            - L = taxa de bits
            - L/R -> tempo de transmissão (pacote completo)
        - dprop - propagação
            - tempo q o bit leva pra chegar da máquina té o access point
            - velocidade pelo espaço
            - sempre na mesma velocidade
            - D(distância)/S(velocidade) -> tempo de propagação
            - luz trafega a ~2.10^8m/s dentro da rede
        - dnodal - nodal total
            - soma de todos
### descarte de pacote
- pacote pode se perder
    - n chegar no destido ou ser descartado
- se a fila ficar cheia é morte

## Exercícios
1.) Considere dois hosts A e B, conectados por um Unico enlace com taxa de R bits por segundo (b/s). Suponha que
estes dois hosts estejam separados por d metros, e que a velocidade de propagação neste enlace seja de s metros
por segundo. O host A tem que enviar um pacote de L bits ao host B. Pede-se:

a) Escreva o atraso de propagação dprop em termos de d e s.
**A propação desse pacote terá o cálculo de dprop=d/s**
b) Determine o tempo de transmissão dtrans, em termos de L e R.
**dtrans=L/R**
c) Suponha que o host A comece a transmitir o pacote no instante t = O. Neste caso, no instante t = dtrans onde estarå
o último bit do pacote? Justifique.
**O último bit do pacote vai estar dentro do link de rede pronto pra percorrer todo o caminho**
d) Suponha que dprop é MAIOR que dtrans. Onde estará o primeiro bit do pacote no instante t = dtrans ?
**Dentro do link físico de rede**
e) Suponha dprop seja MENOR do que dtrans. Onde estará o primeiro bit do pacote no instante t = dtrans ?
**Ainda vai estar dentro do link de rede junto com o resto do pacote**
f) Suponha que s = 2,5x10^8 m/s, L= 100 bits e R = 28 Kbps. Para qual distância d temos dprop igual a dtrans?
```sql
dprop = dtrans
d/2,5x10^8 = L/R
d/2,5x10^8 = 100/28
d = 892 857,14285714285714285714285714 km
```
g) Considere dois hosts X e Y, conectados por um Unico enlace com taxa de 50 Mbps. Estes dois hosts estão separados
por 300 quilômetros, e a velocidade de propagação neste enlace é de 2,5x10^8 metros por segundo. Que tamanho de
pacote seria necessário para que o atraso de transmissão fosse igual ao atraso de propagação?
```sql
enlace = 50 Mbps
d = 300 km
dprop = 2.5x10^8 m/s

dtrans = dprop
L/R = d/s
L/50 = 300 000/2.5x10^8
L = 0.06 Mb
L = 61,44 kb
```