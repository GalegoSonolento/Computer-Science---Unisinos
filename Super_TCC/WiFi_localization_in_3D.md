## Abstract
O trabalho se refere essencialmente á localização de máquinas utilizando a força do sinal de Wi-Fi para gerar um meio 3D

# Introduction
We adopt one branch of WiFi localization methods based
on mapping of the WiFi radio signal that uses Gaussian processes and we combine it with a 6-DOF gyro-odometry allowing a mobile robot to continuously localize
itself in a complex 3D indoor environment or outdoor, if
there is sufficient Wi-Fi coverage. The additional degrees of
freedom of the gyro-odometry (compared to a classical 3-
DOF problem) allow continuous localization, which is not
limited to a single floor and can capture movement in full
3D

<Girômetro ou girómetro ou giroscópio de medição é um instrumento destinado a medir movimentos de rotação, ou, melhor definindo, taxas de variação de ângulo, ou ainda velocidade angular. Um giroscópio ou um sensor de rotações a laser são exemplos de girômetros>

# Mothodology
• Wi-Fi signal strength mapping, section II-A,
• Gaussian process learning, section II-B,
• Wi-Fi localization, section II-C.
- no processo de identificação de força do wi-fi, um primeiro robô faz o preliminar para o segundo, menos equipado
- Os resultados da primeira parte são impressionantes, o robô de mapeamento é capaz de gerar um espaço 3D bastante razoável do ambiente baseado na força sinal do wifi

# Experimental Evaluation
- Em locais mais remotos, menos access points e, principalmente, mais densos em material (concreto) a qualidade da análise e dos dados coletados dmimnuía significativamente
- Efetividade e precisão foi de 3 a 4 metros no geral
    - interessante para cobrir uma área tão grande

# Conclusions
- média de 2.2m dentro do dataset deles
    - *state-of-the-art* consegue 0.7m
- em áreas muito extensas com a cobertura de um access point apenas geram falhas (não consegue analizar as bordas direito)