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

## Formato JPEG
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
- 