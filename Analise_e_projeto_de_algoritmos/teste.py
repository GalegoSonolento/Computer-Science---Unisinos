def encontrar_combinacao_placas(placas):
    n = len(placas)
    total_soma = sum(x + y for x, y in placas)
    
    # Usar um dicionário para armazenar as somas possíveis
    somas = {}
    
    # Adicionar combinações de placas
    for i in range(n):
        for j in range(i + 1, n):
            soma1 = placas[i][0] + placas[j][0]
            soma2 = placas[i][1] + placas[j][1]
            if soma1 == soma2:
                return total_soma, "nenhuma placa descartada"
            if soma1 not in somas:
                somas[soma1] = []
            somas[soma1].append((placas[i], placas[j]))
    
    # Tentar descartar uma placa
    melhor_soma = -1
    placa_descartada = None
    
    for i in range(n):
        soma_total_descartando = total_soma - (placas[i][0] + placas[i][1])
        for j in range(n):
            if i != j:
                soma1 = placas[j][0]
                soma2 = placas[j][1]
                if soma1 + soma2 == soma_total_descartando:
                    if soma_total_descartando > melhor_soma:
                        melhor_soma = soma_total_descartando
                        placa_descartada = placas[i]
                    elif soma_total_descartando == melhor_soma:
                        if (placas[i][0], placas[i][1]) < (placa_descartada[0], placa_descartada[1]):
                            placa_descartada = placas[i]
    
    if melhor_soma == -1:
        return "impossível"
    else:
        return melhor_soma, f"descartada a placa {placa_descartada[0]} {placa_descartada[1]}"

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        placas = [tuple(map(int, input().split())) for _ in range(n)]
        resultado = encontrar_combinacao_placas(placas)
        if isinstance(resultado, tuple):
            print(f"{resultado[0]} {resultado[1]}")
        else:
            print(resultado)

if __name__ == "__main__":
    main()
