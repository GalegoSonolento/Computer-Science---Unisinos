import socket

def iniciar_servidor(protocolo, porta=5000):
    # 0.0.0.0 permite que o servidor aceite conexões de qualquer IP na LAN
    host = '0.0.0.0' 

    if protocolo == 'TCP':
        # AF_INET = IPv4 | SOCK_STREAM = TCP
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Permite reutilizar a porta imediatamente se o script for reiniciado
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        servidor.bind((host, porta))
        servidor.listen(1)
        print(f"[TCP] Servidor UP e escutando na porta {porta}...")
        
        while True:
            conexao, endereco = servidor.accept()
            print(f"[TCP] Máquina conectada: {endereco}")
            # A lógica de receber/enviar as mensagens de tamanhos variados entrará aqui
            while True:
                dados = conexao.recv(65536) 
                if not dados:
                    break 
                conexao.sendall(dados)
                
            print(f"[TCP] Conexão encerrada com {endereco}")
            conexao.close()

    elif protocolo == 'UDP':
        # AF_INET = IPv4 | SOCK_DGRAM = UDP
        servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        servidor.bind((host, porta))
        print(f"[UDP] Servidor UP e escutando na porta {porta}...")
        
        while True:
            # UDP não tem accept(), ele apenas espera dados chegarem
            dados, endereco = servidor.recvfrom(65536) 
            print(f"[UDP] Dados recebidos da máquina: {endereco}")
            # A lógica de devolver o "pong" entrará aqui
            servidor.sendto(dados, endereco)
            servidor.sendto(dados, endereco)