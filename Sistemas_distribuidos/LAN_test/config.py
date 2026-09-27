# Esse aqui é pra ser o IP da máquina auxiliar (no meu caso um Lenovo com CachyOS)
# todo: trocar esse IP pro IP de verdade da máquina
IP_SERVIDOR = '127.0.0.1' 
PORTA_TCP = 5000
PORTA_UDP = 5001

# Tamanhos de mensagem: 100B, 500B, 100KB, 500KB, 1MB, 10MB
TAMANHOS_BYTES = [
    100, 
    500, 
    100 * 1024, 
    500 * 1024, 
    1024 * 1024, 
    10 * 1024 * 1024
]

# Tamanho do buffer para envio e recebimento (não estourar o limite do UDP)
BUFFER_SIZE = 65000