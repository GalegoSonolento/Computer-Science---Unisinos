import socket
import time
import csv
from config import IP_SERVIDOR, PORTA_TCP, PORTA_UDP, TAMANHOS_BYTES, BUFFER_SIZE
from payload_generator import gerar_payload

def testar_tcp(tamanho, payload):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP_SERVIDOR, PORTA_TCP))
        
        inicio = time.perf_counter()
        
        # Envia tudo
        s.sendall(payload)
        
        # Recebe tudo
        bytes_recebidos = 0
        while bytes_recebidos < tamanho:
            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            bytes_recebidos += len(data)
            
        fim = time.perf_counter()
        
    return fim - inicio

def testar_udp(tamanho, payload):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        endereco_servidor = (IP_SERVIDOR, PORTA_UDP)
        
        inicio = time.perf_counter()
        
        # Envio fracionado (Chunking) para evitar erro de MTU/Message too long
        for i in range(0, tamanho, BUFFER_SIZE):
            pedaco = payload[i:i+BUFFER_SIZE]
            s.sendto(pedaco, endereco_servidor)
            
        # Recebimento fracionado
        bytes_recebidos = 0
        while bytes_recebidos < tamanho:
            data, _ = s.recvfrom(BUFFER_SIZE)
            bytes_recebidos += len(data)
            
        fim = time.perf_counter()
        
    return fim - inicio

def executar_testes():
    resultados = []
    
    for tamanho in TAMANHOS_BYTES:
        print(f"\nTestando carga de {tamanho} bytes...")
        payload = gerar_payload(tamanho)
        
        # Teste TCP
        try:
            tempo_tcp = testar_tcp(tamanho, payload)
            # Banda = (Tamanho(bytes) * 8 bits * 2 (ida e volta)) / tempo / 1.000.000 (para Mbps)
            banda_tcp = (tamanho * 8 * 2) / tempo_tcp / 1_000_000
            resultados.append(['TCP', tamanho, tempo_tcp, banda_tcp])
            print(f"  TCP -> Tempo: {tempo_tcp:.5f}s | Banda: {banda_tcp:.2f} Mbps")
        except Exception as e:
            print(f"  TCP falhou: {e}")
            
        # Teste UDP
        try:
            tempo_udp = testar_udp(tamanho, payload)
            banda_udp = (tamanho * 8 * 2) / tempo_udp / 1_000_000
            resultados.append(['UDP', tamanho, tempo_udp, banda_udp])
            print(f"  UDP -> Tempo: {tempo_udp:.5f}s | Banda: {banda_udp:.2f} Mbps")
        except Exception as e:
            print(f"  UDP falhou: {e}")

    # Salvar resultados
    nome_arquivo = 'resultados_pingpong.csv'
    with open(nome_arquivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Protocolo', 'Tamanho_Bytes', 'Tempo_Segundos', 'Banda_Mbps'])
        writer.writerows(resultados)
        
    print(f"\nTestes concluídos. Resultados salvos em '{nome_arquivo}'.")

if __name__ == "__main__":
    executar_testes()