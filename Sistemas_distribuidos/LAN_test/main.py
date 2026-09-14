# Importa a função do arquivo servidor.py
from server import iniciar_servidor

def main():
    print("=== Inicialização do Servidor Ping-Pong ===")
    
    # Permite escolher o protocolo dinamicamente no terminal
    protocolo = input("Qual protocolo deseja subir? (TCP/UDP): ").strip().upper()
    
    if protocolo not in ['TCP', 'UDP']:
        print("Protocolo inválido. Escolha TCP ou UDP.")
        return

    # Inicia o servidor com a escolha feita
    iniciar_servidor(protocolo)

if __name__ == "__main__":
    main()