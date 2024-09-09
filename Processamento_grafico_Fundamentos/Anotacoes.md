-> anotações da cadeira
-> **Repositório de exemplos:** https://github.com/fellowsheep/PG2024-2
Será extremamente importante e de boa venturança usar esse repositório

DATA: 13/Aug/24
-> Procure baixar o OpenGL 3.3 -> Blender

- A disciplina vai ser baseada em OpenGL para fins de aprendizado e resolução de pequenos problemas
  - mais para frente o correto seria usar o Vulkan
- OpenCV é um tanto mais amigável que o OpenGL
- Ambas as bibliotecas são baseadas em C/C++
  - A disciplina provavelmente vai levar à usar C/C++
- Ponteiros normalmente são trabalhados com algumas "ajudas"
  - Use C++ preferencialmente -> mais suporte da linguagem

# Referências práticas (link)
• https://learnopengl.com/
• http://www.opengl-tutorial.org/
• http://docs.gl/
• https://github.com/fellowsheep/PG2024-2 -> esse é um repositório ótimo com alguns tutoriais pra settar o ambiente de desenvolvimento

# Processamento gráfico
**"É o processamento de informações visuais, tanto para geração de imagens, quanto obtenção de dados.**
Processamento gráfico (ou PG) está presente em diversas áreas da computação moderna (e baseia a maior parte dos games e entretenimento modernos).
É bastante possível identificar duas grandes áreas:
- Processamento de imagens - tratamento e visão computacional
- Computação gráfica - síntese e *pipeline* (processo/cadeia de *renderização* tanto 2D quanto 3D).
Tenha em mente a diferença fundamental entre processamento e tratamento
- *Processamento* - extração de dados de uma imagem
  - passa por um processamento computacional de análise dos pontos da imagem a fim de (tentar) compor dados à partir dela - detecção facial, placas de veículos, etc.
  - esse processamento é chamado de visão computacional a partir do momento que as informações da imagem são "enxergadas" pelo computador
  - identificação de marcações também permitem tecnologias de realidade aumentada (AR) - sim, os filtros de instagram são AR
- *Tratamento* - alteração e composição da imagem, sem retirar dados (Photoshop)

- Processamento pra gerar ou extrair info de imagens (grande área)
- usado pra placas de carro por exemplo
- as áreas de processamento gráfico mudam conforme a expressão
  - imagens estáticas tendem a ser mais simples e fáceis de compreender -> filtro e edição (paint) facilitam a vida
  - modelos ainda não viraram imagens
    - guardam informações de iluminação, cor, geometria
    - normalmente as informações são somente numéricas
    - só vira pixel depois da renderização (sintetização) -> computação gráfica
  - em visão computacional o input é a imagem e o output são as informações para tratamento
    - aqui entra em parte na realidade aumentada
    - fica mais próximo de design de interação

# Computação gráfica
O processo de *computação gráfica* *(CG) é basicamente sintetizar todos os dados para geração de uma imagem. Se forçar um pouco a barra, dá para dizer que é o processo inverso do processamento gráfico.
Uma modelagem em CG tem algumas *primitivas* básicas. Sempre será uma coordenanda de 3 pontos. Tenha em mente que CG utiliza o espaço 3D para modelagem das figuras e, para tanto, tem 3 eixos (x, y, z), sempre nessa ordem. Seguindo nessa ideia, podemos montar polígonos com esses pontos de coordenada e montar malhas (*Mesh*) a fim de gerar as figuras.
Um fato interessante é que preferencialmente se gera figuras com triângulos, já que possui menos pontos para gerá-lo (ferramentas inclusive mostram opções de "trianguloficar" os modelos 3D).
- *Frame buffer*: É uma porção de memória usada para criar o
pixel map que será enviado para o monitor.
- *Double buffering*: técnica que utiliza um buffer auxiliar
para criar imagem enquanto um buffer é desenhado
(alternância). Usado para evitar o flicker (tremer a
imagem)
*Game loop* é um conceito de pipeline que sempre *atualiza*, *renderiza* e *sincroniza* dados e processamento de imagem para lançar ao I/O (normalmente o monitor) - mais sobre isso na sequência.

## Renderização
- Essa técnica utiliza cálculos (normalmente vetoriais) para transposição do que seria um ambiente 3D (se for uma renderização 3D) para um plano 2D (tela do monitor - matriz - e o processamenmto de uma GPU). Todo o cálculo de luz e como ela interage com o ambiente, além da tradução para a vizualização em matriz, é feita nessa fase.


- CG
- representação de objetos e modelos usam vértices/pontos -> coordenadas no espaço
  - normalmente associados no modelo 3D, mas o 2D tbm usa obviamente
- a junção dessas coordenadas formam os polígonos
  - normalmente a primitiva é na forma de um triângulo
  - rotacionamento e planos são formados com esses elementos
  - álgebra linear é usada conceitualmente
- a origem do sistema cartesiano é 0,0,0 -> canto do sistema
- é interessante atrelar as unidades dos operadores 3D (como o Blender) pra unidades reais (e.g. metros) para coerência
- em geral para os cálculos, arestas não são tão utilizadas
  - em processamento gráfico em algumas situações as arestas podem ser úteis
- no contexto de CG, polígono e face é a mesma coisa
- o fato de triângulos serem o polígono com menor número de vértices, ele é bastante usado para implementações efetivas (mais estáveis e baratas computacionalmente)
  - algoritmos mais efetivos utilizam malhas triangularizadas de polígonos
- técnica de subdivisão de superfícies
  - aumenta a quantidade de polígonos e procura quadruplicar a quantidade de polígonos
  - fica cada vez mais *smooth*
  - só precisa cuidar pra não explodir a quantidade de polígonos no modelo
  - os pontos não podem ser colineares
### game loop
- desenho do processo gráfico
- processamento mais simples das entradas dos usuários - detecção de eventos
- render é a fase onde o processamento realmente acontece - faz parte do gameloop para computar as alterações realizadas no programa
### Renderização
- render
- ainda é informação visual sem a transposição pra pixel
- imagens são dados bidimensionais
- wireframe view - aramado - estrutura básica poligonal
- solid view - geometria sobre os polígonos com shadding (shaders - sombreamento)
- rendering - iluminação e pós-processamento - mais próximo da imagem final - ainda aparece debugs
- render usa vetores dos objetos para a tela e calcular o direcionamento dos raios de luz
  - inclusive, alguns tipos de material precisam guardar informações de outros objetos - a maioria dos cálculos são feitos na hora - dependendo da complexidade da imagem, uma renderização pode levar horas


DATA: 20/Agosto/24
## Pipeline gráfico
- sequência de etapas com entrada de dados - processamento por etapas
- idealmente os processos podem ser paralelizados (como em uma pipeline padrão de processador)
- o gargalo (bottleneck) da pipeline é o processo mais lento - uma peça de hardware mais fraca pode desacelerar o processo
- estágio de aplicação ainda está contido no código - a maioria das informações e bufferizações acontece aqui
- processamento geométrico monta os vértices e começa a geração de polígonos
- depois de todo o posicionamento correto na cena, entra a rasterização
  - tamanho da imagem
  - resolução
  - posicionamento à partir da posição da câmera
  - aplica algoritmos específicos para diferentes fases
  - os prépixels (fragmentos) são settados
  - input - vértice montados
  - output - fragmentos
- pixel processing pega os fragmentos e processa
  - variando com as informações passadas À ele, ele gera a imagem de verdade
  - dá pra ter mais de um frag pra mesma posição de pixel
    - aqui ele dá um blend e entende a cor final do pixel
- aí dá o resultado final - frame buffer 
  - dá pra meter uns efeito em cima ainda
  - isso aqui é o pós-processamento

DATA: 27/Agosto/24
- Pixel Shader == Fragment Shader

### Shaders
Versões mais atuais das ferramentas de processamento gráfico todas usam uma *Programmable pipeline*, existente desde do OpenGL 2.0. Processadores mais modernos todos utilizam pipelines programáveis.
Essas pipelines programáveis, ao invés de apenas lançar a *geometry data* dentro da GPU e largar na tela, ela pega os dados, lança *buffer*, *shader* e etc, e pode lançar e receber dados da tela ou de outros buffers.
GLEW/GLAD são bibliotecas alcançadas em tempo de execução do código e utilizam o padrão OpenGL (porque é isso que ele é apenas).
Temos 4 estágios dentro da pipeline programável da OpenGL:
• Estágio de Vertex shading
  – Processa cada vértice separadamente
  - antes de rasterizar (achatar) a geometria pra 2D
• Estágio de Tesselation shading -> opcional
  – Gera geometria dentro do pipeline (com código)
• Estágio de Geometry shading -> opcional
  – Processa cada primitiva separadamente
• Estágio de Fragment shading
  – Processa cada fragmento separadamente

Pelo guia do OpenGL 4.3, a ordem do pipeline é a seguinte: *Vertex data* => *Vertex shader* => *Tessellation / Control / Shader* => *Tessellation / Evaluation / Shader* => *Geometry / Shader* => *Rasterization* => *Clipping* => *Primitive Setup* => *Fragment Shader* => Imagem representada na tela.

Shaders, nesse sentido, são simplesmente mini-programas que identificam **como** desenhar algo na tela. São *especificamente* montados pra rodar na **GPU**.
Existem 3 tipos/estágios de Shaders:
• Vertex Shaders: descrevem *como* tratar um *vértice*
  – Posição (3D -> 2D)
  – Coordenadas de Textura
  – Cor
• Fragment Shaders: descrevem *como* tratar uma *área* (pixel-size)
  – Cor
  – Z-depth
  – Alpha value
  - processamento de pixeis
  - em alguns momentos os fragmentos de sobrepõe e ocupam o mesmo pixel (normalmente ficam ocultos)
  - *Depth testing* evita reduência de fragmentos no mesmo pixel
  - todas as cores são em RGBA normalizadas
  - aqui existem alguns comandos úteis para usar
    - points (só os pontos)
    - lines (vértices)
    - line_strip (conecta linhas desconectadas)
    - line_loop (criação de triângulo)
    - triangles (gerar mais de um triângulo na tela)
    - triangle_strip (preencher espaços entre os triângulo - agrupar)
    - triangle_fan (faz um catavento de triângulos)
• Processados paralelamente
  – Um para cada vértice de um modelo
  – Um para cada fragmento

A pipeline toda vai rodar em paralelo usando diversos núcleos de processadores da GPU. O paralelismo nesse caso é real. Nesse sentido, dá pra escolher um shader que tenha nosso objetivo e faça uma diferença bastante clara no resultado final do resultado do processamento. Animação e diferenciação do objeto acontecem nessa área - todos esses processos na GPU são *pipeline do hardware*.
O paralelismo da execução dos shaders é montado especificamente pra execução em telas e rodagem em GPU's (ou melhor, GPU's foram montadas para processamento matricial, necessário em computação gráfica). Essa execução, principalmente de shaders, necessita de *shader cores*; se uma imagem necessita de 200 deles, 200 serão usados ao mesmo tempo.
Os shader cores processam um número fixo de primitivas por vez pelo *buffer VAO* - já que eles os fazem, por isso é interessante manter o número de malhas usadas *baixo* - já que todas essas execuções são feitas em paralelo.
  As primitivas desse buffer são chamadas pelas *drawcalls* - quanto mais delas, mais malhas e mais buffers - podendo sobrecarregar a GPU.
Tenha atenção para a programação dos shaders, já que eles dependem da versão utilizada do OpenGL. Dito isso, ele vai com certeza ter alguns tipos diferentes para realizar as chamadas.
Sempre separe os shaders em arquivos de texto separados - como uma boa prática
- programas (pequenos) que implementam/definem/processam info para serem desenhados (geometrias/fragmentos) para o desenho (render) junto com a API gráfica
  - são compilados especificamente pra rodar na placa gráfica (GPU)
- Shading != shaders (pero no mucho)
  - shading (fazer o sombreamento na solid view) utiliza shaders pra conseguir rodar, mas o *shading* serve como um processo maior conceitualmente
- o compilador do código de shader é a própria API gráfica do OpenGL (GLSL) - nessa caso, se estiver utilizando outra biblioteca gráfica ela vai dar conta do recado à sua maneira
  - GLSL é uma linguagem de Shader

### Buffer
A definição mais básica de *buffer* é que ele é uma unidade de memória separada para guardar informações. Esses dados são colocados em um dispositivo de saída, um *frame buffer*.



### Referências
- Real-time rendering - 4th ed. / 2018 - ( Livro eletrônico ) 
  - https://pdfroom.com/books/real-time-rendering/XDkgVjmNg9B -> aparentemente o leitor de PDF funciona
 wow
- LearnOpenGL - Anton's OpenGL 4 Tutorials
- Slides sobre CG dos professores: Christian Hofsetz,
Cristiano Franco, Marcelo Walter, Soraia Musse, Leandro
Tonietto e Rafael Hocevar

 ## Perguntas
 - o ray tracing é uma camada a mais no processo de rendering?
 - o pipeline é do rendering? cada vez que se renderiza se usa o pipeline grafico?