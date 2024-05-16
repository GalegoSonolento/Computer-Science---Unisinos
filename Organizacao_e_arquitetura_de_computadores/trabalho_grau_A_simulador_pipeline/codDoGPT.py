# Banco de registradores inicializado com todos os valores em zero.
registradores = [0] * 32


# Função para ler a memória de programa (arquivo de texto com instruções).
def ler_memoria_de_programa(arquivo):
    try:
        with open(arquivo, 'r') as file:
            instrucoes = [linha.strip().split() for linha in file.readlines()]
        return instrucoes
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return []


# Função que simula o estágio de busca de instrução.
def buscar(instrucoes, pc):
    if pc < len(instrucoes):
        return instrucoes[pc]
    else:
        return None


# Função que simula o estágio de decodificação de instrução.
def decodificar(instrucao):
    try:
        return {
            'Opcode': instrucao[0],
            'Op1': int(instrucao[1]),
            'Op2': int(instrucao[2]),
            'Op3': int(instrucao[3]) if len(instrucao) > 3 else None,
            'Valida': True
        }
    except IndexError:
        print("Erro de formato de instrução: ", instrucao)
        return None


# Função que simula o estágio de execução da instrução.
def executar(instrucao):
    global registradores
    if instrucao is None:
        return None
    opcode = instrucao['Opcode']
    op1 = instrucao['Op1']
    op2 = instrucao['Op2']
    op3 = instrucao['Op3']

    if opcode == 'ADD':
        registradores[op1] = registradores[op2] + registradores[op3]
    elif opcode == 'ADDI':
        registradores[op1] = registradores[op2] + op3
    elif opcode == 'SUB':
        registradores[op1] = registradores[op2] - registradores[op3]
    elif opcode == 'SUBI':
        registradores[op1] = registradores[op2] - op3
    elif opcode == 'BEQ':
        if registradores[op1] == registradores[op2]:
            return op3  # Retorna o novo valor de PC se o desvio for tomado
    elif opcode == 'J':
        return op1  # Retorna o novo valor de PC para o salto incondicional
    return None


# Função que simula o estágio de escrita do resultado.
def escrever_resultado(instrucao):
    pass  # A escrita dos resultados já é feita na função executar neste exemplo simplificado.


# Função principal que executa o simulador.
def executar_simulador(arquivo_de_instrucoes):
    instrucoes = ler_memoria_de_programa(arquivo_de_instrucoes)
    pc = 0  # Program Counter

    while pc < len(instrucoes) and pc >= 0:
        instrucao_busca = buscar(instrucoes, pc)
        if instrucao_busca is None:
            break
        instrucao_decodificada = decodificar(instrucao_busca)
        novo_pc = executar(instrucao_decodificada)

        if novo_pc is not None:
            pc = novo_pc
        else:
            pc += 1

    print("Estado final dos registradores:")
    for i, val in enumerate(registradores):
        print(f"R{i}: {val}")


# Nome do arquivo de texto com as instruções.
nome_arquivo_instrucoes = 'instrucoes.txt'

# Chama a função para executar o simulador.
executar_simulador(nome_arquivo_instrucoes)