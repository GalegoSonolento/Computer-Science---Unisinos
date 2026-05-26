Lista de Exercícios 1 GB - Computação de Alto Desempenho

**1) O que você entende por aplicações fracamente e fortemente acopladas?**
Aplicações fracamente acopladas possuem tarefas mais independentes, exigindo pouca comunicação e sincronização. Já aplicações fortemente acopladas possuem alta dependência entre processos, necessitando troca frequente de dados e sincronização constante.

**2) Por que aplicações fracamente acopladas podem tirar melhor proveito de cloud computing?**
Porque aplicações fracamente acopladas possuem processos ou componentes que demandam pouca comunicação entre si, o que facilita o paralelismo e a distribuição entre diversas máquinas na cloud. Já aplicações fortemente acopladas possuem maior dependência entre seus componentes, exigindo mais comunicação e sincronização, o que pode gerar latência de rede e reduzir a eficiência em ambientes distribuídos.

**3) Na execução de uma aplicação HPC em cloud, você optaria por elasticidade vertifical ou horizontal?**
A escolha usual seria da elasticidade horizontal, uma vez que ela é a padrão de mercado e não me limita ao máximo de recursos alocáveis à apenas uma máquina (como na elaticidade vertical). Além disso, a horizontal me permite criar clusterizaão e evitar o *Single point of failure*; embora, em casos específicos, com componentes fortemente acoplados, elasticidade vertical possa ser necessária.