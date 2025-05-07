DATA: 25/Fevereiro/2025
# Introdução à computação Gráfica
O principal trabalho com computação gráfica é o de geometria e construção de modelos (tanto 3D quanto 2D).
Existem algoritmos de transformadas e alguns usos mais específicos que podem ajudar em diversos casos - interfaceamento, por exemplo.
<img src="imgs\Fundamentos_de_imagem_e_cor.png">

A base matemática de computação gráfica é toda em cima de vetorização e cálculo matricial. Espero que ainda lembre das bases de álgebra linear.

- padrao CIE é o mais usado
- HSL
    - um sistema diferente convertido pro RGB normal
    - valores associados à cores específicas
    - edita saturarção e luminosidade
- existe uma matriz pronta já pra multiplicar pelo vetor de cor e representar no plano (vetor planificado)
    - proejções diferentes podem usar calibrações de cor diferentes
- imagens são matrizes e pontos (em RGB) tem 3 valores sempre
- sinalização de cor é sempre discreta
    - amostragem
    - amostragens menores pegam menos memória

# Sistemas de cor e imagem
Computadores interpretam as imagens como funções puras.
<img src="imgs\Funcao_imagem.png">

Monitores utilizam os 3 canais principais de cor (RGB - Red, Green, Blue) - essas cores em específico porque os bastonetes dentro do olho humano conseguem compreender essas cores - e (quase) todas podem ser formadas a partir dessas 3 - pelo menos as do expectro visível.
<img src="imgs\Captura_de_imagem.png">

Vale lembrar que os sinais de cor ainda são ondas e, por serem de computador, são ondas digitais. Imagens monocromáticas emitem apenas um pulso, outras emitem um intervalo.
Sistemas de cores tem um formato em específico - RGB forma um cubo à partir de uma fórmula com valores pré-estabelecidos (ou uma onda, uma expressão no formato 2D). Nesse sentido, qualquer outro sistema de cores é traduzido pra RGB a fim de espelhá-lo na tela.
<img src="imgs\Sistemas_de_cores.png">
Todos os valores são pré-estabelecidos

Como vimos, imagens são matrizes e matrizes, nesse caso, são quebras dessa imagem (por algum valor pré-definido) que possuem pelo menos uma informação (escala de cinza) ou 3 (RGB).
Pelo fato de serem matrizes (e digitais), as ondas de cores são amostragens (números finitos). Isso interfere na qualidade de imagem e cor. Quanto mais pontos, melhor a imagem seria.

## Imagens
Parte integrante da computação gráfica e sempre surge de uma forma ou de outra.
IMagens são funções e podem ser representadas matematicamente.
Temos um conjunto de cores que pertence a f e é um subconjunto de C, que por sua vez é a definição da quantidade de cores de uma imagem.
Imagens são matriciais.
Definição da imagem começa no canto superior esquerdo e desce até o canto inferior direito.
- Histograma = número de ocorrêcias de uma cor
- Quantização
    - discretização de uma cor
    - monta a imagem como um valor contínuo e a torna discreta (sequência de valores - amostragem)
- Resoluções tem o tamanho que o monitor de vídeo vai suportar
    - é uma matriz de pixels algoxalgo
    - Full HD por exemplo é 1920x1080
- Dimensão não é resolução - dimensõ é tamanho, que pode ter uma frequência de pontos maior. Uma tela de 5 polegadas pode ser 1920x1080.
0
- canal alfa de cores aparece apenas com 32bits
- Imagens vetoriais são muito usadas na computação e são convertidas em alguns contextos.
    - Vetorial → Matricial: rasterização
    - Matricial → Vetorial: área de reconhecimento de padrões
- imagens baseadas em pixels tem uma qualidade menor de impressão
o Uma imagem é um sinal no domínio do espaço
o Áudio é um sinal no domínio do tempo
- 

### Formato JPEG
Bastante antigo e ainda muito utilizado.
Para evitar redundância aqui, veja: https://en.wikipedia.org/wiki/JPEG
Mas ela basicamente funciona como no abaixo:

- 94
- Compressão de qualidade
- quebra a imagem em funções menores (onda) e joga as ondas uma por cima da outra
- regiões com frequências maiores são arestas, contornos - diferenças maiores entre pixels
- se faz uma reta de frequências das mais baixas pras mais altas (espaço de frequências)
- quantização pega alguns valores redundates de dentro da matriz de onda dos blocos e elimina eles
    - compressão agressiva tira muitas dessas ondas e pixaliza a imagem
    - fator de quantização faz isso
- Códigos em Java de FDCT e IDCT estão nesse documento
- Uma imagem fica em foco quando existem altas frequências

DATA: 11/Março/2025
# Introdução à VAO e VBO - Shaders
- OpenGL não para por debug de estado
    - é importante gerar algum tipo de log de erro
- informação é sempre estruturada no sentido horário
- sempre visualiza o front-face
    - normalmente se usa essa ideia com 3D
    - processamento de visão angulada
    - não precisa processar tudo de uma vez
        - não precisa processar o que a câmera não vê
- shader é basicamente um programinha que forma o pipeline gráfico do OpenGL
- cada programa é vinculado à um vértice por vez (shader)
- sistemas mais modernos já tem mais utilidades ligadas com o OpenGL e já o tem de forma nativa
- saiba o que está desenhando e como está desenhando
    - tenha um mapeamento do que vai ser posto em tela antes de qualquer outro passo
- pode existir mais de um fragment shader por pixel a nível que eles se sobrepõem
- os shaders serão programinhas pra cada um dos vértices da GPU (os quais serão expostos em tela)
- sempre muito importante verificar o versionamento do shader utilizado antes de começar a programar
- Buffers são vetores de memória para armazenar dados temporariamente
    - quando se muda uma cena ou se faz alguma atualizalção de fato, os buffers precisam ser limpos e preenchidos novamente para a nova composição de cena
- A GPU precisa manter a maior quantidade possível de dados
    - em VBO's, precisamos mandar a maior quantidade possível de vértices para evitar retrabalho
    - mandamos um vértice a cada 3 valores (composição de vértice em espaço, sem cor)
    - ou a cada 6 (composição de vértice em 3D com valores RGB)
- Como um exemplo, uma cor por vértice de um triângulo
    - faz com q os shaders façam um degradê entre as cores
- manter o programa organizado com as VBOs é importante quando se tem aplicações maiores
- 

## Programa gráfico em 5 passos:
1. Inicialização do sistema (já vimos nos slides iniciais… glfwInit,
createWindow, …)
2. Passagem de dados CPU ➔ GPU (VBO e VAO)
3. Definição de shaders (vertex shader e fragment shader)
4. Compilação de shader e link do programa que será
executado no pipeline da OpenGL/GPU.
5. Loop de desenho e execução do pipeline.
‣ Passagem de variáveis globais
‣ Execução do pipeline (glDrawArrays) para cada objeto
(VAO).

DATA: 18/Março/2025
## Conceitos de programação GPU
- 46 programinhas rodando em paralelo nos slots da GPU
- Rasterização preenche as informações dos vértices associados
- o pipeline programável são gerados para cada placa gráfica
- existem ações da pipeline já definidas que não podem ser alteradas
    - preenchimento de buffer
        - não se altera o comportamento desse tipo de função
- as composições do pipeline gráfico todos tem shaders e sua composição é usada para gerar a imagem
- glDrawArrays() -> não é programável
- é possível computar vários vértices em paralelo

## Shader Language OpenGLSL
- GLSL (quando se usa OpneGL)
- bastante parecida com C
- vinculado um vértice atual pra processar o mesmo vértice

- Modo de desenho muda diretamente a maneira que o dado é interpretado pelo openGL
- todas as operações em Comp_Graf é tudo matriz
    - tudo multiplicação de matrizes

DATA: 25/Março/2025
# Transformações
- usamos transformações lineares
    - concatenação de multiplicação de matrizes
    - menos oneroso do computador
- matricial
- cálculos de matrizes quadradas apenas (3x3 ou 4x4)
    - homogêneas
- matrizes identidade facilitam cálculos
    - base pra saber a orientação de um objeto
- deslocamentos são distorções de objetos
- incluem vetorização
- translada o cara na origem
    - gira
    - volta pra posição anterior
    - cada uma das operações é uma isolada
    - ordem das operações importa
        - origem, translado, move pro local
- operações são sempre feitas em coordenadas polares
- multiplicação é de um vetor com uma matriz (não é tão demandante assim)
- não precisa passar pra VBO's ou VAO's
    - passa só vetores pros shaders
    - passa as operações com as palavras reservadas pro shader
- glm passa algumas operações prontas
    - passa alguns métodos feitos pra nós
    - dá pra trabalhar com sobrecarga
- operações precisam sempre ser feitas da direira pra esquerda

## Coordenadas homogêneas
- manutenção de padrão de geração de objetos
- jogar pra ser 3x3
    - preenche com 1 (não afeta multiplicações)
        - essa normalização pode ser alterada para criar a impressão de perspectiva
    - 2D 3x3 e 3D 4x4
    - adiciona uma dimensão na matriz só
- transalação acontece em quase qualquer programa
- pensamos sempre nas linhas para os fatores de transalação, escala e rotação

DATA: 01/Abril/2025
## Primitivas gráficas 2D
- representação analítica trabalha com início e final
    - mais fácil de renderizar
    - *rasterização* discreta essa amostra e mostra uma linha que *parece* natural
    - só acontece em renderização
- em OpenGL tudo é renderizado com triângulo
    - se um objeto ficou mto triangular faltou objeto

### anti-aliasing
- **aliasing** é um cerrilhado
- **anti-aliasing** é um borrador pra evitar cerrilhado
    - suaviza a borda só
    - pixels vizinhos tem a mesma cor em diferentes intencidades
- algoritmos de *anti-aliasing* precisam borrar a borda de maneiras diferentes
    - esses códigos não são open source 

# Câmera virtual
- movimentação de FOV dentro de um cenário
- projeções cônicas precisam de interação de pontos de fuga
- existe um espaço chamado de **frustum** que define o que vai ser processado pela GPU
- o *fator h* agora é o fator de perspectiva que define o FOV
    - ângulo de abertura da câmera
- Z sempre cresce pra fora da tela
- teste de profundidade cria um ambiente 3D e descarta objetos que estão atrás de outros
- **z-buffer** - guarda informação de produndidade da tela inteira
    - pra definir o que aparece na frente
    - precisa habilitar o tsete e limpar em todos os passos de renderização
- a câmera olha em um vetor direção normalizado
    - esse é o target da câmera
    - lado de cima da câmera é definido no começo do projeto
        - descrição de lateral e à cima
- criação da câmera é uma matriz criada em openGL
    - precisa passar as posições de target só
- FOV se calcula em radianos
- objetos precisam ser desenhados face-a-face
- matriz model e comportamento do objeto no mundo
    - model ainda pode transladar
    - matriz view refere à câmera e pega os translados

DATA: 08/Abril/2025
# Computação gráfica 3D
- normalmente se trabalha em um sistema de coordenadas pela mão direita
    - a matriz de view é invertida (a câmera vê as coordenadas x invertidas)
- da direita pra esquerda
    - M = Rz * Ry * Rx
- todas as projeções são em 2D
    - fragment shader - pizelização da imagem
    - elementos de textura são aplicados aqui
- câmeras (views) funcionam mais ou menos como câmeras de verdade
    - elas tem áreas de fooc
    - N = eye - center(lente)
    - apesar que aqui o foco é infinito
        - pra aplicar algum tipo de efeito de câmera precia aplicar no shader mais tarde
- a definição do vetor *right* é a multiplicação do vetor up e o LookAt
- coordenadas da câmera ficam na última coluna da matriz de view
- projeções ortográfica matém as formas
    - ignora um dos planos
- a perspectiva deforma formas
    - precisa de pelo menos um **ponto de fuga**
- na computação planos de projeção são volumes (espaço entre o Near e o Far) -> o Frustum
    - o ***curling*** tira objetos que não precisam ser renderizados (atrás de outros, muito longe, fora do frustum)
    - isso precisa do z-buffer
        - buffer de armazenamento de profundidade
        - isso aqui usa pro *curling* e decidir quais descarta
- Centro da *view* fica dentro da câmera
- distância pro plano é normalizada pra manter proporções
- interpolação de cor é calculada por posição de aresta
    - é tudo vetorizado mais tarde

## Renderização 3D
- EBOs são tables de vértices (estrutura da dados) pra armazenamento
    - isso facilita cálculos de simplificação de vértices por distância
- pra construir uma esfera, pro exemplo, a quantidade de *steps* colocada dita a resolução da esfera, ou do objeto dado
- uma curva de bezier é uma curva baseada entre 3 pontos
- a varredura por ***sweep*** curva uma, bom, curva, e a repete em um círculo
    - usado pra criar molas
- Octree
    - ***voxalização*** - cubicalização de um espaço
    - ressonância magnáticas usam isso pra imprimir cor no espaço dentro do corpo
    - imagem estruturada por Octree
    - dá pra descer mais níveis e ver mais voxels
    - árvore voxel é bastante pesada
        - a menor unidade é um voxel
- CSG
    - dá pra criar qql objeto através de primitivas
    - cria uma árvore de criação pra um objeto
    - usa o z-buffer pra operações de interseção, substração, etc
    - estrutura em árvore de cálculos
    - as folhas tem primitivas
    - autoCAD e SolidWorks usam bastante
    - interceção é com ***ray casting*** (rajada de raio) em relação à câmera

## Texturas
- imagem colada em superfície
    - coordenada de textura **UV**
- a textura "substitui" a coordenada de cor dos vértices
- o dado da imagem é carregado em um buffer (data) pra GPU
- Mipmap gera versões diferentes pré-renderizadas
    - gera níveis pré-definidos pra acelerar o processamento
- a textura é posta em uma variável q vai direto pro *fragment shader*
    - dentro dele dá pra aplicar o *texture*
- durante a renderização precisa passar o bind de textura e jogar dentro do VAO

DATA: 15/Abril/2025
# Modelagem 3D
- precisamos saber como tratar as estruturas de dados para gerar objetos 3D
    - isso precisa ser traduzido pros buffers do OpenGL
- objetos 3D são conjuntos de vértices alinhados a fim de gerar conjuntos de faces
    - normalmente forma malhas de triângulos (malhas triangulares)
    - menor forma de representação de uma face é um triângulo
        - primitiva convexa
            - 2 pontos quaisquer
            - qql reta entre eles  contida dentro da figura
        - importantes em cálculos físicos e representação de volumes
        - características mais simples de calcular
        - blocos de construção
            - o mais usado é o triângulo mesmo
- faces dos polígonos possuem **normais** em relação ao vértice ou ao plano
    - cálculo de volumes e cálculo de luz
    - **mapa de normais** - cada pixel representa um vetor normal
        - ajuda a dar aspectos de realismo aos objetos
            - relevo, rugozidade, ranhura, etc
    - malhas normalizadas
        - normais médias de acordo com os vizinhos
    - normais por face geram objetos mais duros (*flat*) que normais por v;ertices e médias (*smooth*)
- ***Wireferame***
    - gera apenas linhas para geração dos objetos
    - gera dificuldades na hora de calcular volume, luz e etc
- ***Boundary Representation (B-Rep)***
    - representação mais simnples de limites de um objeto
    - é o casco do obhjeto 
    - serve pro armazenamento de composição de uma superfície
    - topologia do objeto
    - mto usado em CAD (conjunto de softwares)
- ***Quadtrees***
    - dados espaciais em duas dimensões
    - pode ser usada pra representar LOD de terreno
    - pode ter até 4 quadrantes q se subdividem recursivamente
        - depende do refinamento e da necessidade
    - pode ter usos em compressão de imagem
    - é uma árvore grandona
    - cada quadrante pode gerar até quatro filhos
        - subdivisões só terminam quando temos ou quadrados cheios ou quadrados vazios (para representação do objeto)
        - atinge e *folha* - informação final - definição dos critérios de capacidade
- ***Octree***
    - basicamente a mesma coisa q a *quadrtrees*
    - mas em cubos
    - minecraft é um dos grandes exemplos
- quanto mais polígonos, menos facetada (quadradona) - mais tempo de processamento
    - existe um equilíbrio aí nesse meio
    - nem sempre precisa renderizar o objeto com o máximo de informação
- ***LOD - Level Of Detail***
    - dependendo da distância da cena, o modelo perde alguns polígonos
        - isso aumenta ou diminui conforme o quão perto o objeto está da cena
    - isso pode gerar o efeito de *poping* - modelos dos objetos mudando muito bruscamente
        - uma solução é gerar vários modelos de andar entre eles
            - pode usar mais memória (significativo)
    - ***LOD* Contínuo**
        - redução gradativa em tempo real de polígonos
        - união de pontos e contração de algumas faces
    - ***LOD* de terrenos**
        - uma matriz com perturbações em y
        - dá pra definir manualmente, mas tem como usar uma imagem em preto e branco que puxa um mapa de altura
            - não é muito efetivo em terrenos extensos e com muito detalhe
        - terrenos não são totalmente descartados se estão fora do *frustrum*
        - evite **T vértices** - regiãoes de transição de nível de detalhe - fica muito discrepante
            - isso gera buracos na malha

22/Abril/2025
### Continuação da aula anterior
- o terreno deve ser calculado por *bathces* - quadrados
- precisa existir uma costura entre as diferentes regiôes pra evitar falhas na inserção da textura
- LODS defínem níveis
    - serão baseados na quantidade de quadrados (*batches*) - no exemplo são 16*16, poderia ser mais ou menos
- o método de *skirt* é o utilizado aqui - técnica de criar uma "saia" de triângulos emabixo das bordas dos *batches* pra fazer a costura
    - pra evitar se gera um vértice extra na borda maior (jeito mais simples) - ou ainda gera triângulos menores entre as bordas

# Formato OBJ - Computação gráfica
- arquivo pra carregamento de arquivos
    - representação de malhas de arquivos
- representa modelos 3D
- é basicamente um arquivo de texto (open source)
- cada linha é um objeto
    - é uma abstração da declaração dentro da main.cpp
- **g** agrupa faces sobre um mesmo dado nome
- as linhas compõe os vértices pra criação dos volumes
- isso aqui é basicamente um tipo fixo de arquivo com anotações de vétices e definições dos objetos
    - ele não preenche nada, na verdade isso depende da renderização

DATA: 06/Maio/2025
