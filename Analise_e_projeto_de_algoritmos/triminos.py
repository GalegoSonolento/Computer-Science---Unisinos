import math

def triminos(n, x, y, matriz, p):
    cx = (x // n) * n
    cy = (y // n) * n
    n //= 2
    cx += n
    cy += n
    bx = x & n
    by = y & n
    matriz[cx - bx][cy - (not by)] = matriz[cx - bx][cy - by] = matriz[cx - (not bx)][cy - by] = p + 1

    if n >= 2:
        triminos(n, x, y, matriz, p + 1)
        triminos(n, cx - bx, cy - (not by), matriz, p + 1)
        triminos(n, cx - bx, cy - by, matriz, p + 1)
        triminos(n, cx - (not bx), cy - by, matriz, p + 1)

def print_matriz(n, matriz):
    t = int(math.log10(n * n - 1 / 3))
    for y in range(n):
        print()
        for x in range(n):
            print(matriz[x][y], end="\t")
        print("\n")

def main():
    # Preciso descobrir quais são os valores de entrada
    n, x, y = map(int, input().split())
    matriz = [[0] * n for _ in range(n)]
    matriz[x][y] = 1
    triminos(n, x, y, matriz, 1)
    print_matriz(n, matriz)

if __name__ == "__main__":
    main()
