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

DATA: 10/Setembro/2024
# Sistema de coordenadas
• Coordenadas locais (local space)
• Coodenadas de Universo (world space) – Sistema de Referência do Universo
(SRU)
• Coordenadas de camera (view space)
• Espaço de Recorte (clip space)
• Coordenadas de Tela (screen space) – Sistema de Referência de Tela (SRT)

A diferença mais básica entre uma **window** e uma **viewport** é que a *window* determina a porção/área da cena que será mostrada; enquanto que a *viewport* determina a *forma* dessa porção - além de montar a escala e o mapeamento de rederização.

- Sistemas de projeções e de janelas
- sempre exite o cálculo da transposição da câmera para o recalculo
- no momento q largar o objeto define a posição dele em relação ao sistema de coordenadas
- as coordenadas "originais" são de -1 a 1 (pelo menos no OpenGL) e se não ouver definição do objeto no espaço ele vai estar dentro desse espaço
- o primeiro mapeamento entre o *world space* ou o espaço de mundo/universo. -> relacionado á câmera, claro (que também é um objeto)
- no Blender, por exemplo, se coloca a câmera na cena para ter uma noção de composição de cena
  - colocar no ponto de vista
  - *view point* -> ponto de vista da câmera (de render)
  - as ferramentas de processamento gráfico (Blender, Unity, etc) todas permitem alterações das configurações base das pipelines gráficas
  - dá pra mexer sem medo, as ferramentas só dão uma facilitada
- o objeto central começa na origem do plano cartesiano (origem do mundo)
- ainda precisa definir duas matrizes (transformações) - rotações, translaçoes e escalas
- a matriz passa para o *view space* e a matriz de projeção passa para o *clip space* para aí escalar no *screen space*
  - Tudo é montado no processo de *vertex shader*
- a aplicação pode ter mais de uma viewport
  - elas podem ter visões completamente diferentes
- *viewpoint* se refere a tela
  - porções que serão exibidas pelo CG
- *Window* é um resultado das operações de view e projection - ainda não foi normalizado para os pixeis
  - podem existir viewports diferentes para a mesma window
- *aspect ratio* - razão de aspecto - definição de largura e altura
  - valor 1 entrega um quadrado - valores maiores que um mostram cenas achatadas e menores alongadas
- a projeção é montada do pbservador até o plano de projeção
  - se a distância do observador for infinita a projeção é paralela
  - caso não sempre vai ter alguma *perspectiva*
    - projeção perpendicular

## Projeções
As projeções planares paralelas e perspectivas diferem com relação a distância do plano de projeção ao centro de projeção:
– se a distância é finita, a projeção é **perspectiva**, e
– se a distância é infinita, a projeção é **paralela**
  • Projeção ortogonal (ou ortográfica): as linhas
  projetadas são perpendiculares ao plano da
  projeção.
  – Isso mantém a escala uniforme em todas as
  direções.
  • Projeção oblíqua: As linhas projetadas podem
  estar em um ângulo, mas ainda permanecem
  paralelas.

-> tenha em mente que *perspectivas* demonstram pontos de fuga

- cônicas
  - todos os pontos de fuga se reúnem
  - mais naturalidade à cena
  - objetos aumentam conforme proximidade do observador
- paralelas
  - exclui a característica de distância
  - perserva tamanhos e projeções dos objetos
  - desconsidera o observador
  - pode ser útil na composição de cena (evita enganos de perspectiva)
  - gera perda de informação de profundidade
- a modelagem gera as imagens com multiplicações de matrizes (facilita pra GPU)
  - 4x4 - mat4 -> operações matriciais de 4x4 facilitam pela representação das coordenadas
  - uma das bibliotecas mais simples é GLM - só os cabeçalhos pra colocar no OpenGL  

## GLM
Essa é a biblioteca para trabalhar com matemática dentro do OpenGL

## Matriz de view
Define a matriz do viewport - posicionamento da Câmera
Isso aqui vai multiplicar duas matrizes com os vetores de posicionamento e vai formar a orientação da câmera

## Projeção ortográfica
– *𝑙* (left): coordenada da borda esquerda do plano de corte.
– *𝑟* (right): coordenada da borda direita do plano de corte.
– *𝑏* (bottom): coordenada da borda inferior do plano de corte.
– t (top): coordenada da borda superior do plano de corte.
– n (near): distância ao plano de corte mais próximo (em Z).
– f (far): distância ao plano de corte mais distante (em Z)
– 𝑟 − 𝑙 e 𝑡 − 𝑏: controlam a escala horizontal e vertical do volume de visualização.
– 𝑓 − 𝑛: controla a escala no eixo Z
– − 𝑜+𝑙
𝑜−𝑙 e − 𝑜+𝑏
𝑜−𝑏 : deslocam a posição da câmera, permitindo que o centro do volume
de visualização não esteja na origem

Essa ortogonalidade vai modificar toda a representação ortográfica da cena e alterar o tamanho e composição de cena.

## Scrolling
Aqui a câmera é settada para seguir o personagem e as dimensões de mundo são maiores que a viewport.
Logicamente precisa setar um objeto como o personagem e lockar a câmera nele
Em 2D e uma câmera sem perspectiva


DATA:17/Setembro/24
# Transformações
Todas as transformações e rotações utilizam matrizes para os cálculos.
Além disso, precisam ainda transferir o objeto para a origem e depois ainda colocar na posição necessária.

▪ vec2: ponto 2D (x,y) ou coordenada de textura (s,t)
▪ vec3: ponto ou direção 3D (x,y,z)
▪ vec4: ponto 4D (x,y,z,1.0) ou direção 4D (x,y,z,0.0)
▪ Lembre-se que uma matriz 4x4 só pode ser transformada
por um vetor 4D e uma matriz 3x3 por um vetor 3D

- nos objetos
- precisar usar trigonometria pra fazer os giros (claramente já que é o espaço)

Uma vez que a trigonometria é bastante utilizada, sinta-se encorajado para dar uma olhada neste projeto iterativo sobre o mesmo: https://phet.colorado.edu/en/simulations/trig-tour -> prometo que o site é seguro

Outro recurso muitíssimo utilizado são as matrizes, uma vez que as imagens se dão em uma matriz (a tela do computador), nada mais justo que os cálculos serem matriciais.
Todas as operações com matrizes são utilizadas aqui, sinta-se a vontade para revisar operações com matrizes em https://pt.khanacademy.org/math/algebra-home/alg-matrices

Tenha em mente que as transformações ocorrem por meio dos cálculos angulares trigonométricos e matriciais, mas não se preocupe, o OpenGL (e outras bibliotecas gráficas) o fazem por você (o trabalho pesado pelo menos).

## Translação
É a movimentação de um objeto pelos eixos - todos os pontos do polígono são movidos
xt = x + Tx
yt = y + Ty

## Escala
Altera-se o "tamanho" do objeto, ou a sua escala. Pontos podem ficar maiores, arestas aumentam de tamanho, a área/volume do polígono se altera, etc
Existem escalas uniformes e não uniformes, conforme Ex = Ey e Ex != Ey
Para realizar esse cálculo multiplica-se um fator de escala:
xe = x * Ex
ye = y * Ey

## Rotação
A rotação é interessante uma vez que ela necessita trazer o objeto novamente para a origem, rotacioná-lo e aí sim devolvê-lo para a região de onde foi retirado - isso porquê, caso contrário, ele mudaria de posição ao invés de ângulo (já que é uma soma simples e as posições dos pontos também mudam).
É basicamente uma soma de ãngulos, de forma que os pontos formam um ângulo α em relação à origem. Quando aplicamos uma rotação, adicionamos um ângulo θ à α, e com isso precisamos recalcular a posição dos pontos conforme esse novo ângulo α+θ
xr = x.cos(θ) - y.sen(θ)
yr = y.cos(θ) + x.sen(θ)

Para evitar movimentações desnecessárias no plano:
x' = (x - xp).cos(θ) – (y – yp).sin(θ) + xp
y' = (x - xp).sin(θ) + (y – yp).cos(θ) + yp
-> esse é o chamado pivot da rotação.

## Outras transformações
Ainda existem algumas outras mais situacionais, como:

### Reflexão
Eixo X
x’ = x
y’ = -y

Origem
x’ = -x
y’ = -y

Eixo Y
x’ = -x
y’ = y

### Shearing (deslizamento)
xs = x + Sx
ys = y + Sy

Isso é uma manipulação de um dos lados de um polígono

## Homogeneização de matrizes e vetores
Isso vale tanto para objetos 2D quanto 3D.
Se rezume a completar o vetor um um 3° elemento para homogeneizá-lo. Já que os cálculos matriciais e vetoriais necessitam de operações *completas*, ou seja, uma matriz precisa *necessariamente* ser quadrática, essa homogeinização adiciona o valor **1** para completar.
Esse multiplicação e usabilidade é possível a partir do momento que o OpenGL ainda guarda as informações de matrizes vetorizadas e precisa calcular para matriciá-las e jogá-las na placa de vídeo.

DATA 24/Setembro - 1°/Outubro/2024
# Texturas
As texturas surgiram para fazer uma "imitação" do que seria tal elemento com todos os polígonos presentes. Subtitui a necessidade de utilizar diversos polígonos enquanto ainda causa a ilusão de uma superfície.
Tudo que precisamos fazer é informar ao OpenGL os "cantos" do polígono, ou melhor, a região que tal textura precisa ficar que o **fragment shader** cuida da **interpolação** (preenche o resto).
Utilizando como coordenadas básicas de 0 a 1, um possível código para "placement" de uma textura poderia ser:

```C++
GLfloat texCoords[] = {
0.0f, 0.0f, // Inferior esquerdo
1.0f, 0.0f, // Inferior direito
1.0f, 1.0f, // Superior direito
0.0f, 1,0f // Superior esquerdo
};
```
## Texture Wrapping
Entre os pontos, o OpenGL pode fazer algumas coisas:
– GL_REPEAT: comportamento padrão, que repete a imagem de textura
– GL_MIRRORED_REPEAT: mesmo que GL_REPEAT mas espelha a imagem a cada repetição.
– GL_CLAMP_TO_EDGE: “prende”as coordenadas entre 0 e 1. Os valores mais altos ficam presos às arestas.
– GL_CLAMP_TO_BORDER: coordenadas for a do intervado recebem uma cor de borda.

Existem algumas maneiras de settar, mas as coordenadas s e t são necessárias; trate como x e y:
```C++
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_MIRRORED_REPEAT);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_MIRRORED_REPEAT);
```

## Texture Filtering
Ou **Texture smoothing**. Esse processo serve para consertar problemas causados por compressão ou aumento muito grande de imagem (as texturas). Algumas técnicas podem ser usadas:

### Neares Neighbor Filtering
Se falta pixel pega a cor do vizinho mais próximo
```C++
glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
```
A imagem tem tendência de ficar pixelada e bastante forte.

### Linear Filtering
Faz uma média de todos os vizinhos; os pixels faltantes tem uma cor mediana.
Normalmente geram imagens mais *fuzzy* ou pouco nítidas.
```C++
glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
```

## Minimaps
O OpenGL pode gerar imagens menores de uma textura automaticamente.
A biblioteca faz divisões lineares (divisões por 2) diversas vezes e armazena versões *miniaturizadas* das mesmas imagens.
Existe um método padrão, mas é possível especificá-lo com:
– GL_NEAREST_MIPMAP_NEAREST: usa o mipmap mais próximo do tamanho do pixel e usa o método de interpolação do vizinho mais próximo para amostrar a textura
– GL_LINEAR_MIPMAP_NEAREST: usa o mipmap mais próximo do tamanho do pixel e usa o método de interpolação linear para amostrar a textura
– GL_NEAREST_MIPMAP_LINEAR: faz a interpolação linear dos dois mipmaps mais próximos ao tamanho do pixel e usa o método de interpolação do vizinho mais próximo para amostrar a textura
– GL_LINEAR_MIPMAP_LINEAR: faz a interpolação linear dos dois mipmaps mais próximos ao tamanho do pixel e usa o método de interpolação linear para amostrar a textura
 
```C++
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
```

## Mapeamento UV em modelos 3D
É um mapeamento do objeto 3D. Como se fosse uma planta baixa mesmo. Igual quando montávamos bonecos de papel os quais formavam cubos.
Tem algumas etapas, mas a principal delas é o **mapeamento de textura**. A mesma planta baixa, mas com as texturas aplicadas. É consideravelmente mais simples aplicar texturas em polígos simples que em poliedros.

## Inicialização de texturas
As texturas precisam ser obviamente inicializadas e colocadas dentro do projeto na hora do carregamento.
Cheque abaixo alguns dos métodos para inicializá-las.

- **Gere o ID da textura**
```C++
// Gera o identificador da textura na memória
glGenTextures(1, &texID);
glBindTexture(GL_TEXTURE_2D, texID);
```

- **Ajuste os parâmetros de *wrapping* e *filtering***
```C++
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);

glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
```

- **Faça o carregamento da imagem**
-> Com a biblioteca stb_image (https://github.com/nothings/stb), esse processo é mais facilitado; considere dar um check.
```C++
int width, height, nrChannels;

unsigned char *data = stbi_load(filename.c_str(), &width, &height,
&nrChannels, 0);
```

- **Agora é só mandar os dados para a memória do OpenGL e trabalho feito**
```C++
if (data)
{
  if (nrChannels == 3) //jpg, bmp
  {
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, data);
  }
  else //png
  {
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, data);
  }
  glGenerateMipmap(GL_TEXTURE_2D);
  }
else
{
  std::cout << "Failed to load texture" << std::endl;
}
```

- **Algumas boas práticas interessantes**
```C++
// Considere sempre liberar o buffer de memória depois de usar (isso aqui ainda é baseado em C, ou seja, não existem muitas ferramentas de unassign de memória)
stbi_image_free(data);

glBindTexture(GL_TEXTURE_2D, 0);

// Precisa ativar o buffer de textura do OpenGL
glActiveTexture(GL_TEXTURE0);

// Sempre faça o bind das unidades de textura (as imagens mesmo) com os buffers os quais elas precisam estar relacionadas
glActiveTexture(GL_TEXTURE0);
glBindTexture(GL_TEXTURE_2D, textID1);
glActiveTexture(GL_TEXTURE1);
glBindTexture(GL_TEXTURE_2D, textID2);
glBindVertexArray(VAO);
glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);
```

## Buffers
Agora os buffers do OpenGL possuem mais atributos e nossos leitores precisam espelhar tal fato.
Considere montar estruturas parecidas:
```C++
float vertices[] = {
// posicoes // cores // coordenadas de textura
0.5f, 0.5f, 0.0f, 1.0f, 0.0f, 0.0f, 1.0f, 1.0, // superior direito
0.5f, -0.5f, 0.0f, 0.0f, 1.0f, 0.0f, 1.0f, 0.0f, // inferior direito
-0.5f, -0.5f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 0.0f, // inferior esquerdo
-0.5f, 0.5f, 0.0f, 1.0f, 1.0f, 0.0f, 0.0f, 1.0 // superior esquerdo
};
unsigned int indices[] = {
0, 1, 3, // primeiro triangulo
1, 2, 3 // segundo triangulo
};

//-------------------------------------------------------------------------
glGenVertexArrays(1, &VAO); glGenBuffers(1, &VBO); glGenBuffers(1, &EBO);
glBindVertexArray(VAO);
glBindBuffer(GL_ARRAY_BUFFER, VBO);
glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);
// position attribute
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)0);
glEnableVertexAttribArray(0);
// color attribute
glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)(3 * sizeof(float)));
glEnableVertexAttribArray(1);
// texture coord attribute
glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)(6 * sizeof(float)));
glEnableVertexAttribArray(2);
```

**Não esqueça do vertex shader!**
```C++
#version 450 core
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 color;
layout (location = 2) in vec2 tex_coord;
out vec4 vertexColor;
out vec2 texCoord;
uniform mat4 model;
uniform mat4 projection;
void main()
{
gl_Position = projection * model * vec4(position, 1.0f);
vertexColor = vec4(color,1.0);
texCoord = vec2(tex_coord.x, tex_coord.y);
}

//---------------------------------------------------------
#version 450 core
in vec3 vertexColor;
in vec2 texCoord;
out vec4 color;
// pixels da textura
uniform sampler2D tex_buffer;
void main()
{
color = texture(tex_buffer, texCoord);
}
```

## Finalizando
Alguns lembretes na hora de finalizar seus métodos para completar o programa:
```C++
//Não esquecer de chamar o método para carregar a imagem ☺
GLuint texID = loadTexture("./textures/mario.png");

// Não esquecer de especificar a variável uniform que vai conter os dados da textura no fragment shader
glUniform1i(glGetUniformLocation(shader.ID, "tex_buffer"), 0);

//Antes da drawcall:
glActiveTexture(GL_TEXTURE0);
glBindTexture(GL_TEXTURE_2D, texID);
glBindVertexArray(VAO);
glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);
glBindVertexArray(0);
```

# Camads de sprites e cenários 2D
Cada ciclo do *Game Loop* vai gerar um sprite diferente. Lembre-se de que o game loop sempre passa pelo renderer um update e um sync.
Os sprites estão presentes dentro de uma **Spritesheet**, como uma contendo os estágios de animação de um personagem.
Tal personagem pode possuir uma SpriteSheet com o loop de caminhada que se repete toda vez que ele caminha, dessa forma, o game loop também "caminha" pela spritesheet mostrando as fases.
O posicionamento das imagens é baseado em x, y e z.
Para que o sprite exista, ele precisa estar associado a um quadrilátero qualquer, para que o sprite sirva como uma "textura".
Todas as imagens vem pelo *shader*. Veja uma implementação simples:
```C++
glEnable(GL_DEPTH_TEST);
glDepthFunc(GL_ALWAYS);

glClear(GL_COLOR_BUFFER_BIT |
GL_DEPTH_BUFFER_BIT);

// Para existir transparência, use:
glEnable(GL_BLEND);
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
```
## Recorte de imagens - Spritesheet
A spritesheet funciona basicamente como uma matriz mesmo.
Divide-se o "papel" onde ela está em diferentes segmentos os quais correspondem a estágios da animação. Assim sendo, tudo que o programa faz é navegar pelos diferentes estágios dessa matriz que é a spritesheet.
Uma implementação de uma spritesheet deve levar em conta, agora, os frames de animação presentes. Para isso, uma implementação necessária é:
```C++
iFrame = (iFrame+1) % nFrames
```

Os **Offsets** serão basicamente coordenadas para puxar determinado sprite.
Tenha como exemplo:
```C++
// Na inicialização do sprite
dx = 1.0 / (float)nFrames;
dy = 1.0 / (float)nAnimations;
float vertices[] = {
// positions // colors // texture coords
0.5f, 0.5f, 0.0f, 1.0f, 0.0f, 0.0f, dx, dy, // top right
0.5f, -0.5f, 0.0f, 0.0f, 1.0f, 0.0f, dx, 0.0f, // bottom right
-0.5f, -0.5f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f, 0.0f, // bottom left
-0.5f, 0.5f, 0.0f, 1.0f, 1.0f, 0.0f, 0.0f, dy // top left
};

// Na atualização do sprite
GLint offsetLoc = glGetUniformLocation(shader->Program, "offset");
glUniform2f(offsetLoc, iFrame * dx, iAnimation * dy);
iFrame = (iFrame + 1) % nFrames;

// No shader
#version 450 core
in vec2 TexCoord;
out vec4 color;
// pixels da textura
uniform sampler2D tex1;
//Texture coords offsets for animation
uniform vec2 offset;
void main()
{
color = texture(tex1, TexCoord+offset);
}

// Dentro do gameloop, ainda é necessário implementar algum tipo de timer para coordenar os sprites
//GAME LOOP
while (!glfwWindowShouldClose(window))
{
timer.start();
//faz as chamadas de update e desenho...

// E ainda uma classe timer
#include <chrono>
#include <thread>
#include <ctime>
class Timer
{
public:
Timer();
void start() { begin = std::chrono::system_clock::now(); }
void finish() { end = std::chrono::system_clock::now(); }
double getElapsedTimeMs()
{
std::chrono::duration<double> elapsed_seconds = end - begin;
return elapsed_seconds.count() * 1000;
}
double getElapsedTime()
{
std::chrono::duration<double> elapsed_seconds = end - begin;
return elapsed_seconds.count();
}
double calcWaitingTime(int fps, double elapsedTime) {
double wt = 1000 / (double)fps - elapsedTime;
return wt;
}
protected:
// Using time point and system_clock
std::chrono::time_point<std::chrono::system_clock> begin,
end;
};
```

Ainda é necessário implementar um **waiting time**. Caso ele não exista, a animação funciona, mas ela fica descompassada e não-natural.
É bastante interessante usar um waiting time a fim de, por exemplo, colocar uma velocidade diferente do personagem correndo e andando (de animação no caso).
```C++
double calcWaitingTime(int fps, double elapsedTime) {
  double wt = 1000 / (double)fps - elapsedTime;
  return wt;
}

//GAME LOOP
while (!glfwWindowShouldClose(window))
{
  timer.start();
  glfwPollEvents();
  //...Chama métodos de atualização e desenho dos objetos da cena....
  //Sincronizando o FPS
  timer.finish();
  double waitingTime = timer.calcWaitingTime(60, timer.getElapsedTimeMs());
  if (waitingTime)
  {
  std::this_thread::sleep_for(std::chrono::milliseconds((int)waitingTime));
  }
  glfwSwapBuffers(window);
}
```

## Camadas e Parallax
O efeito de parallaxe não é exatamente simples de ser executado.
Na realidade, é necessário quebrar quebrar a imagem em algumas camadas (como árvores mais adentro separado de uma casa ao fundo) para ser possível *simular* a realidade.
Como na invenção de animação do Walt Disney (dê uma olhada https://www.youtube.com/watch?v=YdHTlUGN1zw), as camadas se movem e tem comportamento um tanto diferentes. A magia está no movimento.
Essa implementação de camadas são os **layers**
A viewport sendo uma câmera, se comporta tal qual a invenção e um offset é necessário:
```C++
layers[i]->setOffsets(offsetx,offsety);
```
Considerando que ainda são "texturas", precisamos definir coordenadas x e y, assim como definição de qual layer é.

Uma forma de implementação seria:
```C++
for all layers [0..n]
layers[i]->computeScrollRateX(mainLayer->getWidth());
layers[i]->computeScrollRateY(mainLayer->getHeight());

for all layers [0..n]
layers[i]->scroll(forward);

for all layers [0..n]
layers[i]->plot(viewport); // será alterado para animação

for all layers [0..n]
layers[i]->computeScrollRateX(mainLayer->getWidth());
layers[i]->computeScrollRateY(mainLayer->getHeight());

for all layers [0..n]
layers[i]->scroll(forward);
```

DATA: 15/Outubro/2024
# Geração de colisão
Uma implementação de colisão simples é considerar os lados dos polígonos e identificar se eles estão sobrepostos.
Veja a implementação simples:
```C++
bool checkCollision(Sprite &one, Sprite &two)
{
  // collision x-axis?
  bool collisionX = one.getPMax().x >=
  two.getPMin().x &&
  two.getPMax().x >= one.getPMin().x;
  // collision y-axis?
  bool collisionY = one.getPMax().y >=
  two.getPMin().y &&
  two.getPMax().y >= one.getPMin().y;
  // collision only if on both axes
  return collisionX && collisionY;
}
```

DATA: 22/Outubro - 12/Novembro/2024
# Sistemas de cores e Introdução ao Processamento de Imagens
Processamento gráfico trabalha com imagens puras e o processamento de imagens ainda segue as normas previamente vistas.
Grosso modo  uma *imagem* é, "nas ciências exatas, como a matemática, o termo "imagem" é entendido como representação de um objeto especializado, que exige técnicas e ferramentas especiais." - wikipédia
Como trabalhamos com matrizes de valores, uma imagem é isso mesmo, uma matriz de **pixels** - *picture elements*.
Cor, sendo uma percepção visual de luz e a luz, sendo uma onda/partícula, telas podem transmitir perfeitamente ilusões de luz.
Se quiser mais informações sobre cores, luz e etc., acesse https://pt.wikipedia.org/wiki/Cor

Existe o Diagrama de Cromaticidade CIE que é basicamente uma forma (X+Y+Z)=1 planificada em x e y, nesse caso, é uma forma meio bizarra onde as cores puras estão nas pontas.

A geração de imagens pelo computador depende de hardware, o qual pode ser por:
CRT (Cathode Ray Tube) - método de TV's de tubo
LCD (Liquid Cristal Display) - tem vários componentes de luz ligados em uma central - vários feixed de luz.

As dimensões da tela ainda usam os dimensionamentos padrão (640x480, 1280x1024) - o produto dessas dimensões identifica os **megapixels** - produto de largura pela altura

A quantidade de bits pode alterar a quantidade de cores representadas na tela. Por isso usualmente imagens e processamentos em gray scale são mais leves
O básico é que o *truecolor* surge a partir de 24 bits e é aí que o canal alfa (luminosidade) aparece para uso.
Caso queira mais informações sobre luminosidade, acesse https://pt.wikipedia.org/wiki/Profundidade_de_cor

Dessa forma, uma imagem é basicamente um conjuto de pixels, cada um com uma coordenada específica

Os modelos mais comuns de uso de cores são o RGB, CMY(K), HSV.
Cheque mais detalhes em https://pt.wikipedia.org/wiki/RGB, https://pt.wikipedia.org/wiki/CMYK e https://pt.wikipedia.org/wiki/HSV.
Inclusive, HSV é um dos modelos mais utilizados para editores de imagem.

### Referências
- Real-time rendering - 4th ed. / 2018 - ( Livro eletrônico ) 
  - https://pdfroom.com/books/real-time-rendering/XDkgVjmNg9B -> aparentemente o leitor de PDF funciona
 wow
- LearnOpenGL - Anton's OpenGL 4 Tutorials
- Slides sobre CG dos professores: Christian Hofsetz, Cristiano Franco, Marcelo Walter, Soraia Musse, Leandro Tonietto e Rafael Hocevar
- Cohen, M., & Manssour, I. H. (2006). OpenGL: uma abordagem prática e objetiva. Novatec editora
- Notas de Aula do professor Leandro Tonietto
- Notas de aula do professor Marcelo Walter (UFRGS)
- Notas de aula do professor Bruno Carvalho (UFRN)
- FOLEY, J.D. et al. Computer graphics: principles and practice. Reading: Addison-Wesley, 1990.
- TONIETTO, Leandro; WALTER, Marcelo. Análise de Algoritmos para Chroma-key. Unisinos, 2000.
- https://learnopengl.com//#!Getting-started/Transformations
- https://learnopengl.com/Getting-started/Textures
- https://learnopengl.com/