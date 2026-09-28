import csv
import matplotlib.pyplot as plt

def ler_dados(nome_arquivo):
    tamanhos_tcp, tempos_tcp, bandas_tcp = [], [], []
    tamanhos_udp, tempos_udp, bandas_udp = [], [], []

    try:
        with open(nome_arquivo, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Pula a linha do cabeçalho
            for row in reader:
                protocolo = row[0]
                tamanho = int(row[1])
                tempo = float(row[2])
                banda = float(row[3])
                
                if protocolo == 'TCP':
                    tamanhos_tcp.append(tamanho)
                    tempos_tcp.append(tempo)
                    bandas_tcp.append(banda)
                elif protocolo == 'UDP':
                    tamanhos_udp.append(tamanho)
                    tempos_udp.append(tempo)
                    bandas_udp.append(banda)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        exit()

    return tamanhos_tcp, tempos_tcp, bandas_tcp, tamanhos_udp, tempos_udp, bandas_udp

def plotar_graficos():
    # Lê os resultados do CSV
    tamanhos_tcp, tempos_tcp, bandas_tcp, tamanhos_udp, tempos_udp, bandas_udp = ler_dados('resultados_pingpong.csv')

    # Configuração global: Usamos escala logarítmica no eixo X porque os tamanhos 
    # variam muito (de 100 bytes até 10.000.000 bytes). Se fosse escala linear, 
    # os menores pacotes ficariam todos espremidos no início do gráfico.

    # Gráfico 1: Tempo de Comunicação
    plt.figure(figsize=(10, 6))
    plt.plot(tamanhos_tcp, tempos_tcp, marker='o', label='TCP', color='#1f77b4', linestyle='-', linewidth=2)
    plt.plot(tamanhos_udp, tempos_udp, marker='s', label='UDP', color='#ff7f0e', linestyle='--', linewidth=2)
    
    plt.xscale('log') 
    plt.title('Tempo de Comunicação vs Tamanho da Mensagem', fontsize=14, pad=15)
    plt.xlabel('Tamanho da Mensagem (Bytes) - Escala Logarítmica', fontsize=12)
    plt.ylabel('Tempo de Comunicação (Segundos)', fontsize=12)
    plt.grid(True, which="both", ls="--", alpha=0.4)
    plt.legend(fontsize=12)
    
    # Salva e exibe
    plt.tight_layout()
    plt.savefig('grafico_tempo.png', dpi=300)
    plt.show()

    # Gráfico 2: Largura de Banda
    plt.figure(figsize=(10, 6))
    plt.plot(tamanhos_tcp, bandas_tcp, marker='o', label='TCP', color='#1f77b4', linestyle='-', linewidth=2)
    plt.plot(tamanhos_udp, bandas_udp, marker='s', label='UDP', color='#ff7f0e', linestyle='--', linewidth=2)
    
    plt.xscale('log')
    plt.title('Uso de Largura de Banda vs Tamanho da Mensagem', fontsize=14, pad=15)
    plt.xlabel('Tamanho da Mensagem (Bytes) - Escala Logarítmica', fontsize=12)
    plt.ylabel('Largura de Banda (Mbps)', fontsize=12)
    plt.grid(True, which="both", ls="--", alpha=0.4)
    plt.legend(fontsize=12)
    
    # Salva e exibe
    plt.tight_layout()
    plt.savefig('grafico_banda.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    plotar_graficos()
    print("Gráficos gerados e salvos como 'grafico_tempo.png' e 'grafico_banda.png'.")