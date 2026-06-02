mmID: High-Resolution mmWave Imaging for Human Identification

## Abstract
- *this paper proposes to improve imaging resolution by estimating the human figure as a whole using conditional generative adversarial networks (cGAN). In order to reduce training complexity, we use an estimated spatial spectrum using the MUltiple SIgnal Classification (MUSIC) algorithm as input to the cGAN.*
- chega bem perto do que um kinect consegue fazer (jogando até 5% de taxa de diferença entre as tecnologias)

# Introduction
- passa por testes de imagem e explica o motivo de não usar antenas 2.4/5GHz
- com mmWave foi possível montar um modelo tal que identifica atributos físicos da pessoa

# mmWave radar sign model
- *60GHz commodity WiFi device with Qualcomm 802.11ad chipset.*
- *Each transmitter (Tx) transmits radar pulses and the pulses are received sequentially by the receiver (Rx) antenna array after reflections from the static and dynamic objects. The received pulses are correlated at the Rx side to estimate the CIR.*

# mmID Design
- pra evitar problemas com o fundo das imagens, fica-se lendo só o backgroud por um tempo, pra que quando alguma coisa, como um humano, entre na cena, se faça uma subtração das ondas
- ao que parece o pessoal pega a imagem da onda mmWave, quebra o 3D dela e reconstrói depois com uma imagem 2D
- usaram as imagens de um Kinect pra montar a Ground-Truth base da rede neural cGAN
    - retiraram toda a montagem direta vinda do Kinect, mas tá lá
- a identificação é por forma corporal mesmo, dado que temos pouca resollução pra trabalhar com faces

# Experimental Results
- o pessoal construiu o próprio dataset pra conseguir treinar a rede neural deles (à partir de imagens geradas com MUSIC alg)
- *The proposed cGAN is trained on an NVIDIA GeForce RTX 4090 GPU. We trained the network for 200 epochs using the ADAM optimizer. In the first 100 epochs, Generator and Discriminator were trained using 0.001 and 1 × 10−5 learning rates, respectively. Then, the learning rate decays exponentially for the following 100 epochs.*
- a melhor distância pra avaliação ainda parece ser entre 1-5m à 2m do dispositivo
    - mais de 2m e a imagem + identificação se torna bastante complicada ou até impraticável

# Conclusion
- *Reconstructed images achieve remarkable resolution with only 5% mean silhouette difference between generated images and ground-truth images from Kinect. The Human Identification module learns distinct pose patterns and torso structures with a convolution neural network to identify human targets. Ex- periments with seven users show that the proposed system is independent of the location and can achieve 93% overall accuracy.*