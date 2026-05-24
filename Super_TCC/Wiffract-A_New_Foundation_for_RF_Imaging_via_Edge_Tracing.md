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
- *We thus propose a completely different way of thinking about this imaging problem: to image the edges of the object by utilizing the corresponding Keller cones and conic sections.*
- Measurement de wifi é bastante problemático

# Experimental Validation
- *5.3.2 Classification Results. We next discuss our classification results in Area 1 and 2. As mentioned earlier, we have run 30 imaging experiments over these two areas for imaging alphabet-shaped objects (pooled from a total of 18 letters). Our proposed Hough Transform-based classifier was able to correctly predict the letters in 26 out of 30 experiments, resulting in an accuracy of 86.7%. It is worth noting that for a classification problem with 26 categories (the English alphabet), a random guess would have yielded a classification accuracy of only 3.8%. This confirms that Wiffract’s edge images carry meaningful information for our classifier to read the alphabet-shaped objects*

# Discussion and future work
- *Extension to imaging other objects: So far, we have showcased Wiffract’s performance by imaging several alphabet-shaped objects that were detailed and complex. We had specifically chosen this application since passing the imaged results through an alphabet classifier gave us a clear quantitative metric of our imaging performance. Nevertheless, Wiffract can also be used in other scenarios, to image any other object. To motivate future work, Fig. 16 shows Wiffract’s performance when imaging sample daily-life objects, such as a garden fence and a microwave oven (in Area 2 of Fig. 7). It can be seen that Wiffract generated good representations of the objects by tracing their dominant edges. For instance, it could capture the fence’s parallel lines even though they are close to each other. Interestingly, for the microwave oven, it could image the inner rectangle, something that would not have been possible with other techniques. As part of future work, one can use Wiffract to image other objects and further pass the imaged results to a classifier for object classification, similar to what we have shown for the letters. Wiffract can, in particular, be useful for detecting cracks and other structural damages, among other applications*
- Backup para sistemas baseados em luz
- usar a IA pra reconstruir o objeto à partir da informação recebida