-> Anotações pertinentes da cadeira
Professora Zeliane

DATA: 14/Aug/24
# Integração
É o problema inverso de uma derivada. Agora vamos encontrar a função de uma derivada dada.
F'(x) = f(x)
**Teorema:** 
Se F é uma antiderivada de f no intervalo I, então G é uma antiderivada de f no intervalo I se, e só se, G tem a forma
G(x) = F(x) + C , para todo x em I
onde C é uma constante.
Note que a inclusão da constante C permite incluir uma família inteira de antiderivadas (uma soma ao final da função ainda é a integral/antiderivada).

Se y = F(x) é uma antiderivada de f, diremos que F(x) é solução da equação
dy/dx = f(x)
Ao resolver uma equação deste tipo, é conveniente reescrevê-la na forma diferencial, ou seja,dy = f(x)dx

A solução geral sendo:
y = S f(x)dx = F(x)+C

A diferencial dx serve para identificar x como variável de integração. O termo integral indefinida é sinônimo de antiderivada.
Portanto, a notação:
S f(x)dx = F(x)+C

Nesse sentido, note que F'(x) = f(x), ou seja, podemos substituir na fórmula:
S F'(x)dx = F(x)+C

E se F(x) é uma antiderivada de f(x), logo:
d/dx[S f(x)dx] = f(x) -> esse f(x) sendo a função que queremos encontrar.

**Teorema da integral indefinida**
Sejam F(x) e G(x) antiderivadas de f(x) e f(x), respectivamente, e c uma constante. Então:
(a) Uma constante pode ser movida através do sinal de integração; isto é,
S cf(x)dx = cF(x)+c

(b) Uma antiderivada de uma soma é a soma das antiderivadas; isto é,
S [f(x) + g(x)]dx = F(x) + G(x) +C

(c) Uma antiderivada de uma diferença é a diferença das antiderivadas; isto é
S [f(x) - g(x)]dx = F(x) - G(x) + C

- primitiva/anti-derivada
- letra maiúscula
- F'(x) = f(x)
- inversa das derivadas
- funções podem ter mais de uma primitiva
    - somar constante ainda mantém como primitiva
- Defina sempre com uma constante - entrega a família
[1 ]

## Integral indefinida
- resultado se entrega na forma diferencial
    - separa a derivada como se fosse uma fração
[2 ]
- O S da integral é realmente um S (de soma)
[3 ]
- Derivar uma integral te entrega a função (tipo exponenciar uma raiz)

## Fórmula básica de integração
- pra uma exponenciação simples, soma o expoente e divide -> bem o contrário da derivação nesse caso que multiplica e diminui o expoente
- Eu preciso achar a fórmula básica, logo, pra integrar alguma coisa e chegar na original, preciso integrar a derivação do negócio (ou considerar que a fórmula que tenho é uma derivada)
- Sf(x)dx = F(x)+C
    - S da integral
    - f(x) = F'(x) -> f(x) é a derivada de F(x), que é a fórmula que preciso
    - dx serve pra ser a representação da variável
        - não vai usar ele pra muita coisa
    - C -> representação da constante pra abrigar todas as famílias de repostas -> dá pra somar qualquer constante que a integral ainda é a mesma

## Anotações
<img src="imgs/14-aug-aula_1_anotacoes_e_exercicios.png">
<img src="imgs/14-aug-aula_1_anotacoes_e_exercicios_2.png">


DATA: 21/Agosto/2024
# Integração por substituição
Todo o objetivo dessa substituição é para facilitar o cáculo. Pense que integrais muito verbosas (e.g.: S(2x+7)(x²+7x+3)^(4/3)dx) são mais complexas de vizualizar resoluções (apesar de ser possível se você for o bichão memo).
A substituição não vai alterar a integral para sempre, apenas momentaneamente para que o cáculo seja facilitado.
Esse processo é análogo ao da regra da cadeia, uma vez que mais processos de derivação são adicionados para chegar à um resultado.
"Fazendo u = g(x), du = g′(x)dx e substituindo na equação acima, temos:
∫ f (g(x)).g′(x)dx = ∫ f (u)du = F(u)+ C
Note que o integrando tem dois fatores, um sendo a função composta e outro sendo a derivada g′(x) da função interna da composição.
Na prática, devemos então definir uma função u = g(x) conveniente, de tal forma que a integral
obtida seja mais simples."

- Na regra da cadeia básica deriva os de fora e vai multiplicando as derivações de dentor
- integração pega a derivada grande vai dar as funções das derivadas "aninhadas"
- precisa identificar alguém como sendo *u* -> essa deriviação faz uma integral em função de u - aí integra normalmente
    - ainda precisa substituir o *u* pelo *g(x)*
    - substituição por algo mais simples
- [1 ]
- normalmente se escolhe para *u* o que está elevado ao expoente (se houver)
- o objetivo é uma integral mais fácil
    - se dificultar a escolha do *u* foi errada