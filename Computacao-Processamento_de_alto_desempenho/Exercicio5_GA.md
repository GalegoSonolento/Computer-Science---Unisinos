Exercício 5 do GA: Em grupos, até a prova do GA.

1) **No seu entendimento, para que serve o último parâmetro da função pthread_create()?**
O último parâmetro da função pthread_create() serve para passar um contexto/dado inicial para a thread executar sua tarefa. Pelo parâmetro ser do tipo void*, permite passar qualquer tipo de dado por meio de um ponteiro genérico. No entanto, é necessário realizar o cast para o tipo correto dentro da função da thread.

2) **Você tem o problema de ajustar o brilho de uma imagem. Mostre como você faria o algoritmo paralelo para um ambiente multicore.**

3) **Para que servem as variáveis de condição?**
Variáveis de condição são utilizadas para sincronização de threads, para isso, elas são utilizadas em conjunto com mutexes para coordenar a execução dessas threads. Elas permitem que uma thread aguarde até que uma determinada condição sobre um estado compartilhado seja satisfeita.

Sua utilização é composta das funções wait(), que faz com que uma thread fique em espera e libere o mutex associado, retomando a execução apenas após receber uma notificação. E as operações signal() e broadcast() que são usadas por outra thread para acordar, respectivamente, uma ou todas as threads que estão aguardando. Após acordar, a thread recupera o mutex e verifica novamente se a condição desejada foi atendida.

4) **Você tem o problema de ordenação de números. Pode ser Merge, Quick, bolha, insertion... Mostre a modelagem paralela para a execução num ambiente multicore.**
A modelagem paralela para dado problema seria algo nessa linha a seguir (para divisão e conquista):
- Definição de uma estrutura sinples, com inteiro inicial, final e um vetor de referência para remontar o vetor dado mais tarde;
- Divisão do vetor original em N partes (tantas partes quando o programador quiser/existirem cores);
- Dadas as N fatias, rodar o algoritmo de ordenação em cada uma deles e, ao invés de juntá-las todas à thread-mãe de uma só vez, utilizar merges sequanciais com as threads vizinhas (pid próximo);
- Ao final devemos ter um vetor ordenado.

Essa lógica segue uma linha usando pthreads com memória compartilhada e as chamadas threads vizinhas se juntam com Joins.