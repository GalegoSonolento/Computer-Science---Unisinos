def torre_de_hanoi (n, fonte, destino, muleta):
    if n == 1:
        print(f"Mova disco 1 da {fonte} para o {destino}")  #->c
        return
    torre_de_hanoi(n-1, fonte, muleta, destino)
    print(f"Mova disco {n} da {fonte} para o {destino}")    #->d
    torre_de_hanoi(n-1, muleta, destino, fonte)
# n = número de discos -> no caso do exercício, usei 4 discos
n = 4
torre_de_hanoi(n, "A", "B", "C")