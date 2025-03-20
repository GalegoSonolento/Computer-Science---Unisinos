DATA: 24/Fevereiro/2025
# Interação Humano-Computador (IHC)
A interação humano-computador entra em todas as áreas que de fato gerem computadores ou operam máquinas (e.g. desenvolvedores de hardware, administradores, operários, etc).
Nesse interim, o usuário é o componente físico que recebe a informação e a manipula.
<img src="imgs\Screenshot from 2025-03-01 13-09-09.png">

Muitos dos conceitos de interface gráfica vem do boom digital do ocidente. Um exemplo clássico é a forma de montar um toggle de sim ou não - apresenta diversos exemplos, alguns melhores que outros.
<img src="imgs/Screenshot from 2025-03-01 13-12-24.png">

A experiência do usuário quando se fala de UX é mais do que apenas o produto. Podemos pensar que quanto mencionamos ou o avaliamos, estamos aplicando um juízo de valor ao produto e, dessa forma, utilizando sua UX (não necessariamente sua UI). Fatores externos influenciam na percepção do público perante o produto, outros fatores que entram em jogo são qualidade, usuário (o físico), interação, o app e a interface.


- maior parte das abordagens é interface gráfica
- alguns abordam interações mecânicas (com máquinas por exemplo)
- Iso vai desde projeto até contexto de uso
    - ambientes de uso do sistema
- A intereção hoje também é do desenvolvedor perante o processo de desenvolvimento
- grande parte dos problemas são gerados por interpretação da info com o humano
- como desenvolver uma aplicação pensando em interação e como manipular a interpretação do user
- maioria dos sistemas serve a uma função (a n ser q seja entretenimento)

DATA: 10/Março/2025
Slides 14 a 53
# Experiência de Usuário (UX)
- início de processo de desenvolvimento
    - ficava limitado a funcinalidades do sistema
    - requisitos ficam esparsos
- tudo q o usuário faz e fala em relação ao produto
    - desde encontrar até usar e falar sobre
- toda UX é diferente pra cada user
    - mas a UX precisa ser minimamente bem montada
    - subjetivo
    - também fala de serviços
- experiência geral
    - com brindes externos, bugs em um game podem não ficar tão visiveis
- modelo circumplexo de Russel
- "Aspectos afetivos são viscerais, percepção instintiva de cores e relação entre formas"
    - aspectos psicológicos entram nessa ceara
    - aspectos afetivos
- algo pode não parecer funcional
    - mas ele passa uma mensagem e pode ser essa mesmo
    - o usuário muitas vezes pode não saber
    - o primeiro passo é definir o que se quer comunicar
- requisitos funcionais estão mais relacionados com a característica do produto mesmo
    - outros qualitativos estão mais relacionados com a pessoa usando o produto
        - mais complexos de atingir
    - uma coisa é o projeto (**utilizável**) outra é a experiência (**conveniência**)
- Muito da comunicação de design se baseia na ideia do designer e na mensagem que ele pretende passar para quem for utilizar o que foi feito por ele
    - o designer tem livre escolha do que ele quer fazer, não necessariamente um produto por ele desenhado precisa ser de fato funcional
    - se algo é inutilizável de propósito e quer passar uma mensagem, o designer teve absoluto sucesso em sua criação
        - o problema é se o resultado é diferente do que ele esperava, como algo inútil ter utilidade e algo preteciosamente útil não o ser.
- UI/UX precárias podem causar risco à usabilidade do produto, segurança operacional e até para a saúde do usuário

# Interface de Usuário (UI)
- camada audiovisual
    - antes tinha bem mais áudio
    - principalmente no começo da internet
- formas de acesso
    - conveniência do sistema
    - central na comunicação de uso do sistema
- uma UI ruim prejudica a UX
- em sistemas de platereira os testes de funcionalidade tem mais presença
    - em jogos normalmente o user fica na frente de outras funcionalidades
        - a ênfase é o user *achar* que tudo funciona bem

# Engenharia cognitiva
- conhecimento do user sobre o mundo
- práticas de realização de determinadas tarefas
- dialoga com a maneira de produzir tarefas dos usuários

# Engenharia semi-ótica
- signos e modelos mentais
- relacionamento do signo com seu conceito e inserção
- a maioria dos signos são adquiridos por cultura
    - disquete como símbolo de salvar é presente na cultura da computação
    - outras tecnologias são complexas e demoram mais tempo
    - uma vez que algo é aceito e espalhado culturalmente é difícil quebrar
        - quase como um vício
- contextualização muda a interface
    - potência e simplicidade dependem de acesso à recursos (principalmente, espaço, processamento e memória)

# Usabilidade
- usabilidade é qualidade
    - sobre facilidade e aprendizado de uso
- se um usuário erra, foi erro dele ou do produto?
- signos que não fazem sentido, perguntas inadequadas, muita informação
    - só precisa entregar o passo e a informação necessária pro user continuar utilizando o sistema
    - pouca informação e inferir que o usuário sabe o que está fazendo também é problemático
- UIs ruins geram riscos operacionais e dificuldades de manutenção à sistemas já existentes
    - um esquema monocromático com muito texto já é horrível quando descansado, imagina mexer nisso depois de dormir 3 horas?
- mapeamentos, consistência
- Um *affordance* é um *trade off*, um detrimento de um ponto em favor de outro

DATA: 17/Março/2024
*Slides 53-101*
# Princípios de Design
- produtos e elementos precisam de devido cuidado

## Visibilidade
- as funções principais devem ser as mais óbvias
- consistência é importante
    - escrita de nomes e definição fica por cima ou dentro
- não deixar visívle o que n tem sentido em determinada situação

## *Affordances*
- Grau de compreensão das pessoas sobre a finalidade do objeto
- entendimento e reconhecimento
    - sem explicação
    - bastante semiótica
    - padrões culturais
- aqui entram os processos de localização
    - de linguagem, espaçamento, etc
- produto pode ter várias funções
    - mas precisa mostrar a principal de forma absurdamente óbvia
- podem existir conflitos
    - algo escrito não é aquilo mesmo
    - LOWER CASE escrito em upper case
- entra em anomalias de visão pra composição de imagem
    - ilusões de ótica
    - olho humano é terrível
- se precisa de rótulo, o design é ruim
    - ele pode ser bom em uma região e não em outra (localização)
- affordances explícitas ajudam usuários que não são muito familiarizados a entenderem a funcionalidade e utilizarem o produto de maneira mais eficiente
    - formatos de botões podem ser explícitas também
- o convencional é o padrão
    - ***hyperlink*** padrão de link desde os primórdios da internet
- affordances ocultas só aparecem com algum tipo de alteração no ambiente pra funcionarem
    - *mouse hover* por exemplo
    - interfaces mais agradáveis
    - o risco aqui é o usuário não saber que aquilo existe
- a metafórica traz um ícone que trás uma semelhança, metáfora mesmo
- interações não-permitidas
    - *affordance* de cor que indica possível problema e impedimento de função
- quando a pessoa vai montar um design novo ela não necessariamente pensa no que as outras pessoas vão pensar sobre ele.
    - aplicações de design são meros reflexos das aplicações que o designer já viu
    - normalmente reflexos de designs reais, analógicos

## Restrição
- evitar erros do usuário

## Bom modelo conceitual
- evita problemas quando as coisas dão errado
- forma intuitiva de utilização do produto
- tem coisas semelhantes 
- um modelo conceitual ruim faz o usuário aprender por tentativa e erro
- funções e controles não relacionados
    - sem precisar de um manual

## Mapeamento
- interface condiz com a espacialidade da realidade
- interface corresponde com a função de alguma maneira
    - formato
    - disposição

## Feedbacks
- mostrar ao user o que está acontecendo
- saber a etapa atual e as próximas diminui a ansiedade do usuário
- como o processo está se desenrolando
- barra de carregamento é um exemplo clássico
- cores, formatos, ícones
    - consistência de feedback
    - informações do sistema pro usuário
