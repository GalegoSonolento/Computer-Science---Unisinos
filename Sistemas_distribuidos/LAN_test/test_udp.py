import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Envia os bytes para o servidor
sock.sendto(b"Ping de teste UDP", ("127.0.0.1", 5000))

# Aguarda a resposta
dados, endereco = sock.recvfrom(1024)
print(f"Recebido de volta: {dados.decode()}")
sock.close()