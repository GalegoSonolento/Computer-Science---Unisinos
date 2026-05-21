Nessa cadeira é preciso ler o material antes de chegar na aula - normalmente será disponibilizado antes
-> aima.cs.berkeley.edu - repositório de código usado pro livro da aula - Artificial Intelligence: A Modern Approach 
Alguns do conteúdos podem ter sido gerados por IA porque 1) po é muito texto e 2) o NotebookLM do Google é bastante competente no que ele faz e faço os testes dele com frequência - eu ainda tomo muitas notas em papel, então n enche meu saco.

https://qiao.github.io/PathFinding.js/visual/ -> site interessante pra testar algoritmos e desempenho

25 Fevereiro 2025
# Agente e conceitos
- ciclagem de sensores e analise de informação
- valores matemáticos de métrica (réguas) são geranlamente mais fáceis de usar
- multiagentes atuam no mesmo ambiente apenas
- defini~çao precisa ser por tarfa

# Transformers
- Bert
    - modelo genérico e utulizável pra tarefas específicas
    - outros usos mais específicos 
    - modelo original serve para fornecer a sequência (palavra) seguinte

- GPT
    - autorregrassivo
    - lê as próprias entradas
    - grupo de etapas atravessado 12x
    - ajuste pra tarefas específicas

# Tipos de LLMs
- modelos default auxiliam a completar sequências
- GPT-3 entregava variações da frase
    - InstructGPR entendia as entradas como prompts de instrução
    - oferecer uma sequência de resposta
    - adaptado pra responder
- LLMs maiores passaram a usar aprendizado por reforço, principalmente no começo

# Aprendizado por reforço
- não temos mais dados prontos
- geração de dados, clusterização, etc
- o agente coleta os dados por conta conforme interage com o ambiente
- sinal de feedback avaliativo
    - não totalmente externa, o agente pode fazer pra ele mesmo
- decisão por tentativa e erro
    - quase um adestramento
- é possível indução de estímulos relacionados não necessariamente o que deveria causar dado estímulo
- ambiente feedback avaliativo pra IA
    - o modelo precisa necessariamente observar o ambiente e avaliar as concequências de suas ações
    - estado + ação = estado resultante -> dados que são armazenados
- processo sequencial
    - diferente das antigas, episódicas
- recompensa não necessariamente precisa de um superespecialista pra avaliar suas ações
- assume-se um agente racional que quer maximização 
    - eventualmente assume um comportamento ótimo
- pode ter recompensa atrasada
- ações agora que podem gerar uma recompensa futura várias iterações mais tarde
- os estados devem conter toda a informção relevante para o agente
    - uma CNN pode extrair isso pra nós a partir de um contexto
- dá pra fazer mta aplicação
    - mas os nerdolas da computação botaram ela pra jogar videogame