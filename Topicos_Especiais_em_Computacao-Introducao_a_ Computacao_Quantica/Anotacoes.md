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
- o Feynmann disse que a própria natureza é absurda - se ele disse isso quem sou eu pra questionar
- o princípio da computação quântica é, em última instância, ser massivamente paralela


DATA: 13/Agosto/2025
# Números e Vetores Complexos
- Nem sempre os reais podem descrever a realidade completamente
    - números reais são casos especiais de números complexos
- número complexo sempre fica na parte direita
- somatório de complexos é pelos reais
- representação complexa no python é um **j**
- python evita criação excessiva de classes
- teoria dos complexos só funciona com fundamento matemático
- cálculos sempre entre os reais (e partes interas)
- **a + bi (ou a + ib)**
- Reais fazem parte dos complexos
- imaginário é a parte do complexo que *provavelmente* tem √-1
    - i² = (0,1).(0,1) = (-1,0) = -1
- (a,0)+(0,b) = (a,b)
    - (0,b) = (b,0).(0,1)
- (0,1) é a representação do imaginário
- par ordennado (normalmente o imaginário é posto no eixo das ordenadas)
- o *i* é uma marcação apenas
- dois número dentro de um só (o complexo)
    - ele é 2D
    - dá pra fazer ele ser 3D ainda
    - a moral toda é q isso é um número, completo, de duas partes
        - o número real e o iimaginário
- feito pelo Heisemberg
- além de apontar a coordenada, ele diz onde o bit zero e 1 colapsam
- a parte real é usada pra calcular probabilidade - o imaginário larga a parte da esfera (do átomo) que estamos
- somas são sempre entre reais e imaginários
    - Re{somados}
    - Im{somados}
- a multiplicação é fácil o suficiente pra induzir, mas é basicamente juntar as partes
- **operações comutam**
    - resultados são os mesmos em qql ordem
    - MAS existem portas quânticas q não o fazem


## Números complexos - Conjugado
- notação da física = * (estrela)
    - conjugação/conjugado complexa
    - isso é pra trocar o sinal do estado imaginário puro
    - troca o sinal do imaginário
    - Z* é o mais usado
    - pego minha função e coloco invertida
- uso Z.Z* pra calcular a "hipotenusa", o valor do ponto (complexo) até a origem
    - nesse caso o produto notável vai ser positivo
- 1925, pega

## Divisão de complexos
- 1/algo equivalente algo^(-1)
- fica uma parada bizarramente grante

## Vetores complexos
- usam portas quânticas (matrizes) de operação em cima dos vetores complexos
- os vetores mesmos são números complexos
- Dirac criou uma notação
- BRA KET
    - |psi> e <psi|
- dá pra fazer transposiição com complexo conjugado (e convertendo a matriz de linha pra coluna ou vice-versa)
- Daggar (Dága) -> cruz (literal)
    - transposição conjugada complexa
    - transpõe a matriz (igual uma inversão de índice da matemática clássica mesmo)
        - depois faz um **conjugado** de cada elemento
    - atua em cima de um vetor/matriz KET
- KET com Dagger é um BRA
    - é uma equivalência por conveniência mesmo

## Matrizes
- soma é sempre com a mesma proporção
- escalar
    - usa o K
    - multiplica todos os valores das matrizes
- produto matricial
    - num de colunas precisa ser igual ao número de linhas da outra
    - é uma porrada de produto escalar entre todos os valores entre eles
    - no python o operador é '@'
    - A@B != B@A
    - sempre multiplicação de linha por coluna
- inversão
    - pra ser invertível precisa de um determinante != 0
    - A^(-1) = 1/det(A) . [matriz]
    - a inversa * a matriz = I (identidade)
        - na identidade passa pro próximo nível do sistema quântico
        - ||

DATA: 20/Agosto/2025
# Produtos
- produto interno
    - retorna uma informação única
    - escalar ou complexo
- BraKet dos mesmos estados (produto interno) precisa ser 1, do contrário seja 0
- para outros, calcule uma multiplicação (produto) de matrizes normal
    - sempre vai ser possível
- saber as notações semelhantes simples é bom para entender a simplificação de Dirac
- Produto externo
    - retorna outra matriz - **operador**
    - **início do conceito de porta quântica**
    - KetBra
    - definido por Heisenberg
    - vetor de estado - projetor
    - leva o qubit pra um novo estado
        - evolui = estado quântico (muda)
    - normalmente são matrizes quadradas
    - número complexo de 2 (2 estados)
    - multiplicação de matrizes
    - operação @ do python
    - existem valores padrão para os produtos externos
- Produto tensorial
    - X em um círculo
        NÃO CONFUNFIR COM XOR (mais dentro de um círculo)
    - funciona como um expansor
    - leva pra uma dimensão maior
    - ainda são matrizes quadradas
    - o operador ainda é uma matriz que age em cima delas
    - multipla o valor pela matriz inteira
        - quantidade de linhas somadas?
        - produto cartesiano
        - imbução (existe?) de matrizes
- Base computacional
    - conceito de colapso
    - toda base é **ortonormal** dois estados normalizados
        - ortogonalidade
        - normal = superposição
    - estado 0 é 100% de prob de largar zero no clássico
    - estado 1 é 100% de prob de largar um no clássico
    - Base Computacional Z
        - usa a base z pra trabalhar (referência)
            - posso criar eixos (bases computacionais) novas
        - condição de normalização é o comprimento do centro até a superfícia da esfera dando 1 - no limite da esfera
            - se n bate lá é inválido
            - é a chance de 100%
        - condição de ortogonalidade
            - um vai pra um lado e o outro pro outro
            - zero no produto interno
            - antagônicos
            - mira pros 2 lados
    - Base Hadamart
        - usa o eixo x
        - outra base, mas o princípio é o mesmo
    - as outras bases q existem já são ortonormais
    - normalmente se trabalha em Z
    - dá pra trocar pra outras bases

- uso da notação de Dirac
    - Bra-Ket
    - Â -> acento circumflexo indica que é um operador
    - a notação de Dirac é uma abstração de operação de matrizes 

- usar uma operação é trocar ele de bases

- Como fica um qubit?
- ^X -> porta de inversão
- 