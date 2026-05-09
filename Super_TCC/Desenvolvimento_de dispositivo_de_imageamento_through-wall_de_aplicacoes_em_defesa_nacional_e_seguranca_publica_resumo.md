# Resumo/objetivo geral
Utilização de ondas de rádio e radar para identificação de objetos através de anteparos (e.g. paredes).

# Introdução
Nesse artigo a intenção era o uso justamente em missões de busca e salvamento, assim como de inverstigação, para uso da polícia e bombeiros por exemplo. Algo importante de se dizer é que o dispositivo montado foi leve e desenhado justamente para ser portátil.

# Desenvolvimento do Dispositivo
- Princípio semelhante ao dos radares biestáticos
    - Par de antenas - receptora e emissora
- Potência e força de onda foram parametrizados conforme a média encontrada em operação no Brasil
- A unidade utilizada para identificação é justamente o RCS (*Radar Cross Section*) que varia de material para material
    - o da pele humana é 1 mˆ2
    - ou 0 dBm

# Simulação Numérica Computacional
- Antenas receptores (TX) e transmissoras (RX)
- O sinal captado pelas antenas é aumentado por LNA - *Low Noise Amplifier*
- Propagação de OEM no ambiente virtual é coordenada pelo algoritmo de Yee
- Implementação em tempo discreto com método FDTD (Finite Diference Time Domain)
    - 420x420 células
    - condições de fronteira medidas com PML - Perfectly Mached Layer
- com ondas muito grandes, pode-se usar antenas pequenas, mas a refração é menor e mais próximo a antena fica da zona de Fraunhofer
- Inicialmente 3 GHz -> a resolução 680 da Anatel restringe 2,9 GHz a 3,6 GHz como frequências de uso
    - frequência de operação de 3 GHz é de 10cm
- as fases de todos os elementos são somadas

# Resultados obtidos
- Essencialmente passa o sinal da antena como uma varredura do ambiente e identifica algum objeto/pessoa na cena.
- a onda conta a intencidade de refração, dessa forma é possível plottar um gráfico em base de acúmulo de sinal

# Conclusoes
- O eco do corpo humano e das paredes permite criar um contraste na imagem