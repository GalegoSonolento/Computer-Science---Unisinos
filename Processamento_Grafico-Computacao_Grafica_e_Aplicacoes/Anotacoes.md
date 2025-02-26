DATA: 25/Fevereiro/2025
# Introdução à computação Gráfica
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
## Formato JPEG
- 94
- Compressão de qualidade
- quebra a imagem em funções menores (onda) e joga as ondas uma por cima da outra
- regiões com frequências maiores são arestas, contornos - diferenças maiores entre pixels
- se faz uma reta de frequências das mais baixas pras mais altas (espaço de frequências)
- quantização pega alguns valores redundates de dentro da matriz de onda dos blocos e elimina eles
    - compressão agressiva tira muitas dessas ondas e pixaliza a imagem
    - fator de quantização faz isso
- 