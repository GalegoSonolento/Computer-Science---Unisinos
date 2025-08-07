DATA: 06/Agosto/2025
# Introdução à Computação Quântica
- O modelo clássico chegou a um limite
    - NP-Hard -> sem execução eficiente na computação clássica
    - puxou a quântica
- A literatura passa pelos físicos top-10 brabos d+
    - Plank - Avô
        - partícula de luz (quântum)
    - Eistein
        - efeito fotoelétrico - quanta -> fótons
        - comprovou o Plank
    - Bohr
        - modêlo atômico
        - tio-avô da mecânica quântica
    - Louis de Broglie
        - dupla-fenda
        - comprovou a dualidade onda-partícula
        - vira partícula com observação
    - Heisenberg
        - pai da mecânica quântica
        - modelo matemático de qbit
        - álgebra linear
        - Incerteza (diferença da relatividade geral)
    - Schrödinger
        - quação quântica
    - Dirac
        - equação de Dirac
    - Einstein, Podolsky e Rosen
        - paradoxo EPR
        - protocolo pra desmascarar o emaranhamento
        - protocolo de criptografia
    - Bell
        - princípio de emaranhamento
- A computação quântica seguiu nesse caminho
    - Yuri Manin
        - resolver problemas intratáveis
        - 1980
    - Benioff
        - teoria pra processar problemas
        - 1980
    - Feynman
        - precisa de um computador quântico pra resolver os problemas
        - 1981
    - David Deutsch
        - Pai da comp. quântica
        - comp quântico universal
        - fez uma máquina de touring quântica
        - iniciou a área
        - 1985
    - Peter Shor
        - 1994
        - algoritmo híbrido
        - fatoração de dois números inteiros
        - entrega os números primos
            - problema exponencial (fatorial)
        - já consegue quebrar um chave de 2048 bits (ainda é simples)
    - Lov Grover
        - 1996
        - algoritmo de busca complexidade quadrática
        - sem estruturas de dados
            - só na massiva da quântica
    - Zellinger et al.
        - 1997
        - teletransporte de informação
- 53 qubits ainda é pouca coisa
    - 2^n -> 2^53
    - quebra de criptografia precisa de 2^1 000 000
- Vantagem quântica
    - resolver um problema computacional que o comp quântico resolve exponensialmente mais rápido que um convencional
- sistemas de correção de erros
    - evitar ruídos
    - manter o bit up
    - IBM promete entregar um com 1000 qubits sem erros em 2029
- IBM & AWS
    - VQE e QAOA -> otimização quântica -> 2023
- O experimento de emaranhamento foi comprovado 15 anos atrás
    - a natureza é um código em espaguete
- física teórica avança mto mais rápido que a prática
- mecânica quântica estuda o subatômico
    - conjunto de regras matemáticas
    - mecânica quântica pra processamento massivo de dados
    - a clássica é booleana e a quântica é maluca
    - probabilística
        - superposição
- Lei de Moore
    - mundo clássico acaba logo ali na frente (2027)
    - parou em 3nm - 10^-9 -> fica probabilístico
- pra evitar ruído eu rodo ele várias vezes
    - faço uma aproximação pra ver mais ou menos o resultado
- o chip quântico chega próximo de 0K
- Criptografia Boss-quântica
    - algoritmos clássicos que não são quebrados pela computação quântica
- Computador Quântico BR
    - SENAI CIMATEC
    - CBPF
    - tão fazendo chover com 90 milhões de reais
- Era NISQ
    - Noise Intermidiate Quantum-Scale
    - avanço mais recente é da IBM
    - 1 qubit sem erros precisa de uns 9 qubits físicos
- Números complexos -> imaginários -> IR+i
- Multi. de matrizes
- Produto tensor -> simulador usa clássica pra resolver uma quântica
    - não tem uma superposição natural
    - 8 qubits já n aguenta
- Probabilidade de medidas
- Definição qubit
    - menor unidade de um comp quântico
    - Feito pelo Grok:
```log
A representação matemática de um qubit é dada por um vetor de estado na forma de uma superposição linear no espaço de Hilbert bidimensional, expressa como:
$ |\psi\rangle = \alpha|0\rangle + \beta|1\rangle $
psi = alfa 0 + beta 1 -> entregam o ponteiro 3D onde preciso estar
onde:


$ |\psi\rangle $ é o estado quântico do qubit,
$ |0\rangle $ e $ |1\rangle $ são os estados base (geralmente associados a 0 e 1 clássicos),
$ \alpha $ e $ \beta $ são amplitudes de probabilidade complexas,
A normalização exige que $ |\alpha|^2 + |\beta|^2 = 1 $, representando a probabilidade total.

Essa é a forma padrão de descrever um qubit na mecânica quântica.
```

- tende a colapsar pra um valor clássico
- só da pra saber a *tendência* do valor
- as runs são chamadas de **shots** aqui
- pra valer precisa simular erro
- |n> -> notação de Dirac - chama-se **produto**
- a medição do bit quântico sempre vai colapsar pro 0 ou 1
    - criptografia quântica é impenetrável
    - qualquer espiada ele colapsa
- existem qudits tbm
    - 2+ mais camadas de elétrons ao mesmo tempo
- 