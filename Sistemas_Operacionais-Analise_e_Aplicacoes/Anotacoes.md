DATA: 08/Maio/2025
# Sistemas Operacionais
- SOs são o coração da máquina
    - é claro que elas ainda podem funcionar sem eles, ma SOs são extremamente úteis como uma camada entre os softwares e o hardware em si.
- é bastante complexo entender o funcionamento total de um sistema operacional, uma vez que seria comparável a 50 linhas por página e mil páginas.
    - complicado de decorar (ainda mais em código)
## História
- Primeira Geração (1940-1955): Computação sem Sistemas Operacionais.
- Segunda Geração (1955 -1965): Surgimento dos Sistemas Batch.
- Terceira Geração (1965 -1980): Multiprogramação e Tempo Compartilhado.
- Quarta Geração (1980 - 2000): Computadores Pessoais e Redes.
- Quinta Geração (2000 - Presente): Sistemas Distribuídos, Virtualização e Computação em Nuvem.
- Claro que as diviões dessas gerações variam conforme o autor, mas esstão mais ou menos certas assim.

## Tipos de sistemas operacionais
- ✓ Batch (lote): Executa tarefas em lote sem interação do usuário. Ex: Sistemas bancários antigos.
- ✓ Multiprogramação: Vários programas executados simultaneamente. Ex: UNIX, Linux, Windows.
- ✓ Tempo Real: Respostas em tempo determinístico. Ex: Sistemas embarcados, automação industrial.
- ✓ Distribuídos: Vários computadores trabalhando juntos. Ex: Google Cloud, AWS.

## Versões e distribuições de Sistemas Operacionais 
- atualmente já existem bastantes versões dos sistemas operacionais, mas 3 segmento ainda são os principais:
    - windowsz
    - Linux
    - MacOS
    - Esses 3 competem e têm versões diferentes em si mesmos

DATA: 24/Maio/2025
# PowerShell
- PowerShell é a versão de Bash do Windows
    - dá pra montar script e automação utilizando essa ferramenta
- apesar de ser windows, PowerShell tem suporte multiplataforma
- Existe uma lista bem grande com todos os operadores do PowerShell, mas na dúvida é consultar material e perguntar pro GPT
- ela tem basicamente os mesmos comando que são feitos dentro do Linux, mas precisa de algumas diferenças (código proprietário)

DATA: 29/Maio/2025
# Processos em Sistemas Operacionais
- Processo é uma instância de um programa rodando dentro do computador com tarefas executadas dentro da CPU
- As tarefas feitas pelo usuário tem sempre maior prioridade
    - para alta responsividade
- Isso em processos pesados né
- registrador está do lado da ULA e é apoiada pela memória de cache
    - muitas vezes os dados são jogados pra memória principal já que eles não são necessário imediatamente
    - quando mais threads, mais competição por espaço
- diferentes tipos de thread usam diferentes tipos de processamento
    - por exemplo uma thread do Firefox que esteja tocando um vídeo vai usar bem mais da GPU (fica mais à mostra)
- threads são criadas para auxiliar o processo principal
    - o **processo leve** é a própria thread
- mexer o mouse é uma interrupção do sistema por si
- todos os processos param ante uma interrupção
- Tabela de Processos PCB tem todos os processos rodando no sistema
    - inclusive as permissões dadas a esses processos
- no Windows, alguns processos em segundo plano ficam visíveis para o usuário e podem ser ativos mais rapidamente
- **comunicação entre processos** (IPC)
    - vários tipos de conexão
    - aqui entram os processos de rede
- processos leve *threads* podem ser 
    - single ou multi-thread
    - varia conforme o programa (**processo pesado**)
- threads tem *overhead* bem menor
    - quase nada pra dar *load*

# Bash
- basicamente um powerShell de unix
    - tem as mesmas funções
    - ainda dá pra usar powershell no linux, mas n tem mto fundamento a n ser que seja absolutamente necessario
- comandos por terminal
- 