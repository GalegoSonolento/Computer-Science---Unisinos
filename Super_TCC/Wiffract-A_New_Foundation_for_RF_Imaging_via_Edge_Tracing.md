## Abstract
- imagem da mais alta resolução possível com objetos parados
- Montagem de imagem com RF (Radio Frquency)

# Introduction
- de maneira geral, tirar imagens (i.e. identificação) de objetos em movimento é mais fácil que de objetos parados
- Treinamento de IA pra Imagem RF ainda é um problema dado os datasets pequenos
- Uso de **Keller Cones**
- Identificar bordas de um objeto com secção cônica
- a diferença de usar essas ôndas cônicas é justamente para montar um desenho mais detalhado do que seria a forma de verdade de um objeto

# Traditional Imaging
- A aquisição normal de imagens pode ser facilmente utilizada com uma quantidade de RX grande (large size)
- esse artigo trabalha, também, com o recebimento de onda, mas especificamente com as ondas maiores, a fim de evitar ruído

# Proposed idea: Imaging via edge
- as bordas interagem com a onda de uma maneira difente
- qualquer objeto no meio do caminho do cone de Keller vai se tornar um corte do cone.