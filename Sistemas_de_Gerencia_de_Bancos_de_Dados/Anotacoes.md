DATA: 27/Fevereiro/2025
# Introdução ao Processamento de Consultas
- Análise de custo dos queries e consegue mostrar onde a consulta está com dificuldade
- o banco de dados pode fazer uma otimização sozinho
- existe uma tradução interna no banco pra uma visão diferente
    - novas execuções rodam mais rápido
- queries no geral seguem padrões ANSI
    - poucos bancos tem estilos proprietários
- DB mostra a quantidade de tempo que o banco leva pra aplicar os filtros (e.g. where clauses)
    - planos de queries mostram gargalos

# Otimização e Estratégias no Processamento das Consultas
- indices são ótimos mas não são balas de prata
    - consultas se benficiam
    - podem tornar inserções mais pesadas
- em IOT, outras soluções mais bem montadas para INSERTS são melhores (REDIS cai por terra)
- Oracle ainda é a melhor em alterações de disco 
    - provavelmente pelo fato das paginações e gerenciamento de cache
    - com discos precisamos diminuir a utilização dos mesmos
- bancos de dados transforma o SQL (comercial) pra álgebra relacional interna
    - entrega a equivalência menos custosa
- muitas vezes quantidades de registros e número de tables variam a efetividade
    - particionamento interno dos dados pra acesso mais rápido é bastante raro nos DBs
- ao fazer qql query mais complexa, analise o banco de query para ter mais informações sobre como o DB está rodando aquela query em específico
- views guardam as consultas mais utilizadas para retorno mais rápido dos dados
- backups frios são normalmente feitos em fita magnética (incrivelmente mais segura)
- A estrutura de armazenamento 
- HASH e HEAPS são usados aqui também
    - HASH muito usado em Blockchain
        - um bloco aponta pro outro com HASHES - segurança
- 




### Perguntas
- SAP HANA tem plano de avalização proprietário?
- Redis é uma boa engine de DB ainda
- O que é o Cloud BigTable?
- a equivalência menos custosa é necessariamente a mais rápida?
- view substituem a lógica de partições internas da table?
- gravação em fita magnética ainda é a mais segura?
- como funciona um banco de dados inconsistente? porquê vale a pena?