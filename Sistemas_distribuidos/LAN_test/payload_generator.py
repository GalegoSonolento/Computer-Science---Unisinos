import os

def gerar_payload(tamanho_em_bytes):
    """Gera um array de bytes aleatórios do tamanho exato especificado."""
    return os.urandom(tamanho_em_bytes)