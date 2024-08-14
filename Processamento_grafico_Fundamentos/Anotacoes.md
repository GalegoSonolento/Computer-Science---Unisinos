-> anotações da cadeira

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
## Pipeline gráfico
- 
