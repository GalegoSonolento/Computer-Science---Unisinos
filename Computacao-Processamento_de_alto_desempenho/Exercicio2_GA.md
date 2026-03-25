Exercicio 2 GA
Em grupos de de até 4 pessoas, responda:

**1) Como extrair o paralelismo em ambiente:**
**a) Multicomputador**
Para explorar o paralelismo em ambientes multicomputador, diferentes máquinas com memória própria, se é utilizado a troca de mensagens (como sockets) para comunicação e sincronização.
**b) Multiprocessador**
Para explorar o paralelismo em ambientes multiprocessador, multiplos cores em uma mesma máquina, se é utilizado uma estrutura de memória e dados compartilhada junto de threads, permitindo comunicação direta, mas exigindo mecanismos de sincronização para evitar condições de corrida.

**2) Quais os cuidados que devemos ter ao usar cache?** É importante tomarmos alguns cuidados ao usar cache, para evitarmos problemas de desempenho ou inconsistência de dados.
Em processadores multicore, podem ocorrer problemas de coerência de cache, pois diferentes caches podem possuir cópias do mesmo dado, sendo necessário manter esses valores consistentes. Também pode ocorrer "False sharing", quando threads distintas modificam variáveis diferentes que estão no mesmo bloco de cache, causando invalidações desnecessárias. Além disso, é importante organizar o acesso aos dados para aproveitar a localidade de memória, aumentando a chance de encontrar os dados na cache e reduzindo acessos à memória principal. Por fim, também é necessário garantir a sincronização correta, para que mudanças feitas por um processador se tornem visíveis para os demais.

**3) Explique com as suas palavras o que tem dentro de um chip Multicore.** Um Chip multicore compôe um processador maior; nesse sentido, em um processador quad-core (físico), teremos quatro chips multicore (o que torna o processador em um Octa-core lógico). Além disso, dentro de cada chip teremos dois cores virtuais (que o SO lerá como um processador individual), de modo que cada um terá seus próprios registradores; no entanto, eles compartilharão recursos; e.g.: uma ULA para ambos.
Vale ressaltar que processadores multi-core melhores não necessariamente usam apenas mais cores virtuais, mas também comportam mais recursos para alimentar esses cores.

**4) Por que não existe pipeline superescalar com replicação 8,16,32,...?** Não temos pipelines superescalares com esses níveis de replicação justamente por causa de scripts/códigos *não-lineares* (dependências de controle) e Hazards, que potencialmente geram pipelines vazias para evitar um problema de coerência de dados entre as pipelines. Caso absolutamente todos os códigos fossem com certeza lineares, não teríamos esse problema e a escala poderia aumentar.

**5) Por que a equação do pipeline estudada em aula é irreal?**
A equação assume um pipeline perfeito, sem interrupções. Na prática existem três problemas: dependências de dados forçam o pipeline a esperar por resultados que ainda não estão disponíveis; dependências de controle fazem o processador buscar instruções erradas em desvios; e conflitos estruturais ocorrem quando dois estágios disputam o mesmo recurso. Em todos esses casos, o pipeline precisa recorrer a bolhas, NOPs ou reordenamento, adicionando ciclos extras que a equação ignora.