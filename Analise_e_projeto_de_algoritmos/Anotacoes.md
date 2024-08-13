-> Anotações da cadeira
-> disciplina baseada no livro do CORMEN - Algoritmos: teoria e prática

DATA: 12/Aug/24
# Introdução - Complexidade de algoritmos, Recursos e Utilização de recursos por algoritmos
- normalmente soluções menos eficientes tem mais facilidade de implementação
    - dificilmente acontece o contrário
    - por isso análise de complexidade é necessária
        - vai q é tão complexo que dá a volta
- alguns algoritmos não podem ter complexidades menores ou já chegaram em locais estagnados ou soluções "próximas da ideal"
- algoritmos precisam resolver independentemente da **instância**
    - instãncias -> diferentes entradas
- sempre conheça o seu problema
    - algoritmos de escalonamento -> existem vários
        - mas ainda assim casos diferentes requerem estruturas diferentes
- se a prova do algorimo funciona ele é favorável
    - abrir mão de algumas coisas pode ser ideial 
- algoritmo não é a implementação do algoritmo
    - algoritmo tem no máximo um pseudocódigo para facilitar a compreensão
    - colocar código como resposta é ruim
        - implementa algumas escritas desnecessárias pra entendimento geral do algoritmo
    - artigos entregam pseudocódigo
- casos de teste diferentes pras soluções (outas instâncias) vão calejar a solução
- a busca de uma solução absoluta geralmente leva pra um n! (fatorial)
    - busca exaustiva é caro
- prova de funcionamento de algortimo é só se for por indução matemática mesmo 
    - não-corretude funciona como provas de conceito e testes
    - ainda preciso usar isso pra provar que ele realmente tem a complexidade que eu estou dizendo que ele tem
- soluções candidatas podem não estar corretas
- historicamente implementações escolhem minimizar **espaço** ou **tempo**
- Tempo constante na análise é um tempo desvinculado
    - normalmente chama de *c*
    - tempos que o sistema usa pra operações não relacionadas com a atividade do algoritmo
    - eles podem influenciar o resultado final (podem variar entre os algoritmos)
- N suficientemente grande ou entrada suficientemente grande
    - isso aqui é pra dizer que passa do ponto de inflexão e vale a pena usar o algoritmo mais lerdo (mas que cresce mais lentamente)
    - tendência de N ao infinito


### Exercícios
- **Dê um exemplo de aplicação real em que é necessário usar ordenação:** Ordenar lista telefônica em ordem alfabética
- **Além da velocidade, que outro critério pode ser utilizado para medir eficiência?** Capacidade de processamento de instruções /s
- **Escolha uma estrutura de dados que você conhece, e liste seus prós e contras.** Pilha
Prós:
- FILO
- Ordenamento automático (coloca-se os itens na ordem)
- Fácil de implementar

Contra:
- Ordenamento precisa ser feito fora da pilha
- Inflexibilidade

- **Dê um exemplo de problema real em que somente a melhor solução é permitida, e um exemplo de problema em que uma solução próxima da melhor é “aceitável”.** 
-> apenas melhor permitida: ordenamento de ponto cirúrgico
-> aceiável passa: cara dos correios / roteamento de rede


## Perguntas
- como q faz pra ler esses livros enormes?
- mesmo que a solução funcione, ela ainda pode ser errada?