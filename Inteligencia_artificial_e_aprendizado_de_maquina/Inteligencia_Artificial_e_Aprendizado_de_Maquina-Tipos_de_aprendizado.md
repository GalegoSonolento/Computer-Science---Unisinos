Inteligência Artificial e Aprendizado de Máquina: Documento de Briefing

Sumário Executivo

O aprendizado de máquina (Machine Learning) é definido pela capacidade de um agente melhorar seu desempenho em tarefas futuras por meio de experiências e observações do mundo. Este campo é essencial para lidar com ambientes desconhecidos ou não totalmente compreendidos, servindo como uma alternativa eficiente para a construção de sistemas que, em vez de tentarem representar a realidade de forma exaustiva, expõem o agente à realidade para que ele aprenda com ela. O objetivo central é aprimorar os mecanismos de decisão para elevar a performance do agente.

Os três paradigmas fundamentais de aprendizado são o supervisionado (baseado em exemplos rotulados), o não-supervisionado (identificação de padrões em dados não-rotulados) e por reforço (aprendizado por tentativa e erro via recompensas). No aprendizado supervisionado, o desafio reside em encontrar uma hipótese h(x) que melhor aproxime uma função verdadeira f(x), equilibrando expressividade e complexidade, e garantindo a capacidade de generalização para dados nunca vistos.


--------------------------------------------------------------------------------


1. Fundamentos do Aprendizado de Máquina

Por que o aprendizado é necessário?

A necessidade de aprendizado surge quando as técnicas tradicionais de programação estática não são suficientes. Os principais motivadores incluem:

* Ambientes desconhecidos: Situações onde o projetista não consegue prever todas as variáveis.
* Realidade vs. Representação: É mais eficaz expor o agente à realidade do que tentar representá-la totalmente de forma manual.
* Melhoria de Performance: O aprendizado permite que o agente refine seus próprios processos de decisão.

Arquitetura de um Agente que Aprende

O processo de aprendizado dentro de um agente é composto por componentes integrados que interagem com o ambiente:

* Sensores: Captam informações do ambiente.
* Crítico (Critic): Avalia o desempenho do agente com base em um padrão de performance e fornece feedback.
* Elemento de Aprendizado (Learning element): Responsável por realizar mudanças no agente e definir metas de aprendizado.
* Elemento de Desempenho (Performance element): Utiliza o conhecimento adquirido para agir no mundo.
* Gerador de Problemas (Problem generator): Sugere experimentos e ações para explorar novas informações.
* Efetores (Effectors): Executam as ações no ambiente.


--------------------------------------------------------------------------------


2. Taxonomia do Aprendizado por Feedback

O aprendizado é classificado conforme o tipo de feedback que o agente recebe:

Tipo de Aprendizado	Descrição	Método Principal
Supervisionado	Aprende uma função que mapeia entradas para saídas.	Baseado em pares de exemplos (entrada/saída).
Não-Supervisionado	Identifica padrões e estruturas em dados.	Processamento de dados não-rotulados.
Por Reforço	Aprende comportamentos para atingir objetivos.	Recompensas eventuais e tentativa e erro.


--------------------------------------------------------------------------------


3. Aprendizado Supervisionado: Mapeamento e Hipóteses

O aprendizado supervisionado foca em descobrir uma função h(x) (hipótese) que aproxime a função verdadeira f(x) = y, a partir de um conjunto de dados (dataset) composto por amostras (x_1, y_1), (x_2, y_2), ..., (x_N, y_N).

Componentes do Processo

* Datasets: Conjuntos de dados divididos entre treino (para ajuste da hipótese) e teste (para avaliação).
* Amostras e Features: Cada amostra é descrita por atributos (features) que fornecem evidências sobre a classe ou valor de saída.
* Generalização: A capacidade crítica da hipótese de funcionar corretamente com entradas que não estavam no conjunto de treino.

Tipos de Problemas de Aprendizagem

1. Classificação: Quando a saída pertence a um conjunto finito de categorias (ex: identificar se uma imagem é de um gato ou cachorro).
2. Regressão: Quando a saída é um valor real ou contínuo (ex: prever o preço de uma casa com base no seu tamanho).


--------------------------------------------------------------------------------


4. Busca de Hipóteses e Modelagem

O processo indutivo consiste em testar diversas hipóteses até encontrar uma consistente com os dados.

Espaço de Hipóteses (\mathcal{H})

Contém todas as funções possíveis dentro de certas suposições (ex: todas as funções lineares ou polinomiais). Um problema é considerado realizável se a função verdadeira f estiver contida em \mathcal{H}.

Princípios de Seleção

* Navalha de Ockham: Diante de múltiplas hipóteses consistentes, deve-se priorizar a mais simples. Há um conflito direto entre consistência e simplicidade.
* Trade-off Expressividade vs. Complexidade:
  * Modelos mais expressivos (ex: Máquinas de Turing) podem representar funções complexas, mas são mais difíceis de aprender.
  * Modelos menos expressivos (ex: funções lineares) são mais simples, mas podem não capturar a função real.
* Risco de Sobreajuste: Hipóteses excessivamente consistentes com os dados de treino podem falhar na generalização para novos dados.


--------------------------------------------------------------------------------


5. Ecossistema de Dados e Repositórios

O sucesso do aprendizado depende de bases de dados robustas. O documento cita exemplos fundamentais:

Exemplos de Datasets

* Iris Plants Database: 150 amostras, 4 features, 3 classes de flores.
* MNIST: 70.000 imagens em escala de cinza (28x28 pixels) de dígitos de 0 a 9.
* CIFAR-10: 60.000 imagens coloridas (32x32 pixels) divididas em 10 classes.
* Large Movie Review Dataset (IMDB): 50.000 críticas de filmes para classificação de sentimento (positivo ou negativo).
* ImageNet: Mais de 14 milhões de imagens coloridas em mais de 20.000 classes para reconhecimento de objetos.
* COCO (Common Objects in Context): 328.000 imagens para detecção, segmentação e legenda de imagens (captioning).

Repositórios Principais

Para a obtenção de novos conjuntos de dados, o material destaca:

* Papers with Code (Datasets)
* Kaggle Datasets