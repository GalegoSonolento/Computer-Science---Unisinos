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
- 