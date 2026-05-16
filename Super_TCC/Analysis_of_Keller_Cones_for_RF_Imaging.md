## Abstract
A ideia desse artigo é justamente entender como os Cones de Keller podem auxiliar na visão computacional via ondas de wi-fi.
Também compara essa ideia, de identificação por bordas, com outros métodos já usados

# Introduction
- quando a crista da onda bate em uma quina, isso resulta em diversos ráios divergentes daquele ponto, ditados pela Teoria de Difração de Keller (GTD)
    -  *when a wave is incident on an edge, it results in a cone of outgoing rays, dictated by the Keller’s Geometrical Theory of Diffraction (GTD) [5].*
- uma das questões era identificar uma borda não aguda, mas que fosse curva o suficiente para causar uma difração na onda
    - em tese isso ainda geraria uma borda para o sistema, o que causaria a identificação da imagem
    - se a borda tiver a mesma curvatura da onda, ela não aparecerá
- o artigo gera uma base e define outros parâmetros, como distância do grid RX, localização do TX, tamanho do grid RX, etc.

# Problem Formulation
- O sistema q consegue receber o sinal é uma antena comum
- uma das dificuldades é, tradicionalmente, o tamanho da onda.
    - enquanto ondas de frequência maior (mmWave) veêm as bordas com maior facilidade, ondas maiores (e.g. Wi-Fi), mesmo que as mesmas perturbações ainda existam, elas são consideravelmente menores
- usando a mesma técnica só com wi-fi, a performance será bem pobre, dado que várias superfícies agem como espelhos para essas ondas
    - Mas usando justamente a difração com Cones de Keller, ainda é possível a utilização do mesmo

# Keller Cones: The Interaction of Wireless Signals with Edges
- *when a ray is incident on an edge point, the outgoing rays form a cone, known as the Keller cone, with the edge as its axis and the cone angle equal to the angle made by the incident ray with the unit vector along the edge.*
    - o Keller Cone é da origem da emissão da onda até o dado objeto (ou imagem)
    - a grande moral é entender o ângulo que a difração faz
        - se passar um ser *threshold*, temos nossa quina
- parece que com um ponto de reflexão a matriz de imagem precisa ser bem menor

# Experimental Setup
- Mais simples reler o artigo. Essa sesção detalha bastante o processo de setup para o test
- os resultados não são necessariamente sobre o wi-fi ver através da parede, mas sim que isso é possível, a partir dos resultados obtidos aqui

# What constitutes an edge to a wave?
- *Correção*: os Cones de Keller são gerados à partir do ponto de incidência da borda/quina
- *"[...] an area that does not visually look like a sharp edge can still appear as one to the incoming wave if the radius of its curvature is less than half of the wavelength."*
    - ou seja, se a curvatura não for muito grande, tudo certo

# Edge Visibility Analysis
- *Several parameters can affect the exiting Keller cone of an edge. Sample important ones include location and orientation of an edge, distance of the edge to the RX grid, location of the transmitter, and size of the RX grid.*
- Esse trecho discorre bastante sobre variação desses parâmetros, bem como o número de antenas RX afeta na captação
- tem um teste bastante interessante feito aqui com uma folha de papel e mostrando a resposta do sinal da captação
    - 2.4GHz é consideravelmente mais borrado, mas se o objetivo for um produto super barato, ainda é possível usar
- existem bordas cegas
    - olhando nas imagens de captação, norlmente é bastante óbvio no meio, mas as partes superiores e inferiores da borda se perdem (não tem informação/imagem não fica verdinha)
    - o nome disso é região *blind*
        - o sinal do Cone de Keller não chega nos receptores RX (matriz)
- em alguns testes é sugerido que pelo menos 2 transmissores sem ângulo (Θ = 0°) entre sí e o plano
    - junto de outro à 90°
- em alguns testes, a borda de baixo ter uma alteração de profundidade é menos prejudicial