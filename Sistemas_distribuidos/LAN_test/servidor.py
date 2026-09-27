import socket
import threading
from config import IP_SERVIDOR, PORTA_TCP, PORTA_UDP, BUFFER_SIZE

def iniciar_servidor_tcp():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 0.0.0.0 permite escutar em todas as interfaces de rede (cabo, wifi, localhost)
        s.bind(('0.0.0.0', PORTA_TCP))
        s.listen()
        print(f"[*] Servidor TCP escutando na porta {PORTA_TCP}")
        
        while True:
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(BUFFER_SIZE)
                    if not data:
                        break
                    # Ecoa de volta para o cliente
                    conn.sendall(data)

def iniciar_servidor_udp():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(('0.0.0.0', PORTA_UDP))
        print(f"[*] Servidor UDP escutando na porta {PORTA_UDP}")
        
        while True:
            data, addr = s.recvfrom(BUFFER_SIZE)
            # Ecoa o datagrama de volta
            s.sendto(data, addr)

if __name__ == "__main__":
    print("Iniciando servidores...")
    thread_tcp = threading.Thread(target=iniciar_servidor_tcp, daemon=True)
    thread_udp = threading.Thread(target=iniciar_servidor_udp, daemon=True)
    
    thread_tcp.start()
    thread_udp.start()
    
    # Mantém o script principal rodando
    try:
        thread_tcp.join()
        thread_udp.join()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")