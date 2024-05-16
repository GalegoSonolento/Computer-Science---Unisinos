resgistradores = {
    'R0': 0,
    'R1': 0,
    'R2': 0,
    'R3': 0,
    'R4': 0,
    'R5': 0,
    'R6': 0,
    'R7': 0,
    'R8': 0,
    'R9': 0,
    'R10': 0,
    'R11': 0,
    'R12': 0,
    'R13': 0,
    'R14': 0,
    'R15': 0,
    'R16': 0,
    'R17': 0,
    'R18': 0,
    'R19': 0,
    'R20': 0,
    'R21': 0,
    'R22': 0,
    'R23': 0,
    'R24': 0,
    'R25': 0,
    'R26': 0,
    'R27': 0,
    'R28': 0,
    'R29': 0,
    'R30': 0,
    'R31': 0,
}
PC = 0
instrucoes = []

historico = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
}

dict_busca = {
    'Opcode': '',
    'Op1': '',
    'Op2': '',
    'Op3': '',
    'Temp1': '0',
    'Temp2': '0',
    'Temp3': '0',
    'Valida': True,
    'PC': 0
}
dict_decodificacao = {
    'Opcode': '',
    'Op1': '',
    'Op2': '',
    'Op3': '',
    'Temp1': '0',
    'Temp2': '0',
    'Temp3': '0',
    'Valida': True,
    'PC': 0
}
dict_execucao = {
    'Opcode': '',
    'Op1': '',
    'Op2': '',
    'Op3': '',
    'Temp1': '0',
    'Temp2': '0',
    'Temp3': '0',
    'Valida': True,
    'PC': 0
}
dict_memoria = {
    'Opcode': '',
    'Op1': '',
    'Op2': '',
    'Op3': '',
    'Temp1': '0',
    'Temp2': '0',
    'Temp3': '0',
    'Valida': True,
    'PC': 0
}
dict_write_back = {
    'Opcode': '',
    'Op1': '',
    'Op2': '',
    'Op3': '',
    'Temp1': '0',
    'Temp2': '0',
    'Temp3': '0',
    'Valida': True,
    'PC': 0
}
dict_temp = {
    'Opcode': '',
    'Op1': '',
    'Op2': '',
    'Op3': '',
    'Temp1': '',
    'Temp2': '',
    'Temp3': '',
    'Valida': True,
    'PC': 0
}


def lerArquivo(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as file:
            # Lê cada linha individualmente
            # instrucoes = [linha.strip().split() for linha in file.readlines()]
            for linha in file:
                # Imprime cada linha do arquivo
                instrucoes.append(linha.strip().split())
                # print(linha.strip())  # O método strip() remove espaços em branco e quebras de linha extras
        return instrucoes
    except FileNotFoundError:
        print(f"O arquivo {arquivo} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")


def busca(pc, hazardOn):
    if PC < len(instrucoes):
        dict_busca['Opcode'] = instrucoes[PC][0]
        dict_busca['Op1'] = '0'
        dict_busca['Op2'] = '0'
        dict_busca['Op3'] = '0'
        dict_busca['Temp1'] = '0'
        dict_busca['Temp2'] = '0'
        dict_busca['Temp3'] = '0'
        dict_busca['Valida'] = True
        dict_busca['PC'] = PC
    elif PC >= len(instrucoes):
        dict_busca['Opcode'] = ''
        dict_busca['Op1'] = '0'
        dict_busca['Op2'] = '0'
        dict_busca['Op3'] = '0'
        dict_busca['Temp1'] = '0'
        dict_busca['Temp2'] = '0'
        dict_busca['Temp3'] = '0'
        dict_busca['Valida'] = True
        dict_busca['PC'] = PC

    inst = str(dict_busca['PC'])
    primer_alg = int(inst[len(inst) - 1])
    #print(f"mostrando o valor de primer_alg {primer_alg}")
    if dict_busca['Opcode'] == 'beq' and hazardOn:
        if historico[primer_alg] == 1:
            pc = int(instrucoes[pc][3]) - 1

    return pc


def decodificacao():
    if dict_busca['Opcode'] == 'add':
        dict_decodificacao['Opcode'] = dict_busca['Opcode']
        dict_decodificacao['Op1'] = instrucoes[dict_busca['PC']][1]
        dict_decodificacao['Op2'] = instrucoes[dict_busca['PC']][2]
        dict_decodificacao['Op3'] = instrucoes[dict_busca['PC']][3]
        dict_decodificacao['Temp1'] = str(resgistradores[instrucoes[dict_busca['PC']][1]])
        dict_decodificacao['Temp2'] = str(resgistradores[instrucoes[dict_busca['PC']][2]])
        dict_decodificacao['Temp3'] = str(resgistradores[instrucoes[dict_busca['PC']][3]])
        dict_decodificacao['Valida'] = dict_busca['Valida']
        dict_decodificacao['PC'] = dict_busca['PC']

    elif dict_busca['Opcode'] == 'addi':
        dict_decodificacao['Opcode'] = dict_busca['Opcode']
        dict_decodificacao['Op1'] = instrucoes[dict_busca['PC']][1]
        dict_decodificacao['Op2'] = instrucoes[dict_busca['PC']][2]
        dict_decodificacao['Op3'] = instrucoes[dict_busca['PC']][3]
        dict_decodificacao['Temp1'] = str(resgistradores[instrucoes[dict_busca['PC']][1]])
        dict_decodificacao['Temp2'] = str(resgistradores[instrucoes[dict_busca['PC']][2]])
        dict_decodificacao['Temp3'] = instrucoes[dict_busca['PC']][3]
        dict_decodificacao['Valida'] = dict_busca['Valida']
        dict_decodificacao['PC'] = dict_busca['PC']

    elif dict_busca['Opcode'] == 'sub':
        dict_decodificacao['Opcode'] = dict_busca['Opcode']
        dict_decodificacao['Op1'] = instrucoes[dict_busca['PC']][1]
        dict_decodificacao['Op2'] = instrucoes[dict_busca['PC']][2]
        dict_decodificacao['Op3'] = instrucoes[dict_busca['PC']][3]
        dict_decodificacao['Temp1'] = str(resgistradores[instrucoes[dict_busca['PC']][1]])
        dict_decodificacao['Temp2'] = str(resgistradores[instrucoes[dict_busca['PC']][2]])
        dict_decodificacao['Temp3'] = str(resgistradores[instrucoes[dict_busca['PC']][3]])
        dict_decodificacao['Valida'] = dict_busca['Valida']
        dict_decodificacao['PC'] = dict_busca['PC']

    elif dict_busca['Opcode'] == 'subi':
        dict_decodificacao['Opcode'] = dict_busca['Opcode']
        dict_decodificacao['Op1'] = instrucoes[dict_busca['PC']][1]
        dict_decodificacao['Op2'] = instrucoes[dict_busca['PC']][2]
        dict_decodificacao['Op3'] = instrucoes[dict_busca['PC']][3]
        dict_decodificacao['Temp1'] = str(resgistradores[instrucoes[dict_busca['PC']][1]])
        dict_decodificacao['Temp2'] = str(resgistradores[instrucoes[dict_busca['PC']][2]])
        dict_decodificacao['Temp3'] = instrucoes[dict_busca['PC']][3]
        dict_decodificacao['Valida'] = dict_busca['Valida']
        dict_decodificacao['PC'] = dict_busca['PC']

    elif dict_busca['Opcode'] == 'beq':
        dict_decodificacao['Opcode'] = dict_busca['Opcode']
        dict_decodificacao['Op1'] = instrucoes[dict_busca['PC']][1]
        dict_decodificacao['Op2'] = instrucoes[dict_busca['PC']][2]
        dict_decodificacao['Op3'] = instrucoes[dict_busca['PC']][3]
        dict_decodificacao['Temp1'] = str(resgistradores[instrucoes[dict_busca['PC']][1]])
        dict_decodificacao['Temp2'] = str(resgistradores[instrucoes[dict_busca['PC']][2]])
        dict_decodificacao['Temp3'] = instrucoes[dict_busca['PC']][3]
        dict_decodificacao['Valida'] = dict_busca['Valida']
        dict_decodificacao['PC'] = dict_busca['PC']

    elif dict_busca['Opcode'] == 'j':
        dict_decodificacao['Opcode'] = dict_busca['Opcode']
        dict_decodificacao['Op1'] = 0
        dict_decodificacao['Op2'] = 0
        dict_decodificacao['Op3'] = 0
        dict_decodificacao['Temp1'] = 0
        dict_decodificacao['Temp2'] = 0
        dict_decodificacao['Temp3'] = 0
        dict_decodificacao['Valida'] = dict_busca['Valida']
        dict_decodificacao['PC'] = dict_busca['PC']

    elif dict_busca['Opcode'] == 'halt':
        dict_decodificacao['Opcode'] = dict_busca['Opcode']
        dict_decodificacao['Op1'] = 0
        dict_decodificacao['Op2'] = 0
        dict_decodificacao['Op3'] = 0
        dict_decodificacao['Temp1'] = 0
        dict_decodificacao['Temp2'] = 0
        dict_decodificacao['Temp3'] = 0
        dict_decodificacao['Valida'] = dict_busca['Valida']
        dict_decodificacao['PC'] = dict_busca['PC']

    elif dict_busca['Opcode'] == '':
        dict_decodificacao['Opcode'] = ''
        dict_decodificacao['Op1'] = 0
        dict_decodificacao['Op2'] = 0
        dict_decodificacao['Op3'] = 0
        dict_decodificacao['Temp1'] = 0
        dict_decodificacao['Temp2'] = 0
        dict_decodificacao['Temp3'] = 0
        dict_decodificacao['Valida'] = dict_busca['Valida']
        dict_decodificacao['PC'] = dict_busca['PC']


def execucao():
    dict_execucao['Opcode'] = dict_decodificacao['Opcode']
    dict_execucao['Op1'] = dict_decodificacao['Op1']
    dict_execucao['Op2'] = dict_decodificacao['Op2']
    dict_execucao['Op3'] = dict_decodificacao['Op3']
    dict_execucao['Temp1'] = dict_decodificacao['Temp1']
    dict_execucao['Temp2'] = dict_decodificacao['Temp2']
    dict_execucao['Temp3'] = dict_decodificacao['Temp3']
    dict_execucao['Valida'] = dict_decodificacao['Valida']
    dict_execucao['PC'] = dict_decodificacao['PC']

    if dict_execucao['Opcode'] == 'add':
        dict_execucao['Temp1'] = str(resgistradores[dict_execucao['Op1']])
        dict_execucao['Temp2'] = str(resgistradores[dict_execucao['Op2']])
        dict_execucao['Temp3'] = str(resgistradores[dict_execucao['Op3']])

    elif dict_execucao['Opcode'] == 'addi':
        dict_execucao['Temp1'] = str(resgistradores[dict_execucao['Op1']])
        dict_execucao['Temp2'] = str(resgistradores[dict_execucao['Op2']])

    elif dict_execucao['Opcode'] == 'sub':
        dict_execucao['Temp1'] = str(resgistradores[dict_execucao['Op1']])
        dict_execucao['Temp2'] = str(resgistradores[dict_execucao['Op2']])
        dict_execucao['Temp3'] = str(resgistradores[dict_execucao['Op3']])

    elif dict_execucao['Opcode'] == 'subi':
        dict_execucao['Temp1'] = str(resgistradores[dict_execucao['Op1']])
        dict_execucao['Temp2'] = str(resgistradores[dict_execucao['Op2']])

    elif dict_execucao['Opcode'] == 'beq':
        dict_execucao['Temp1'] = str(resgistradores[dict_execucao['Op1']])
        dict_execucao['Temp2'] = str(resgistradores[dict_execucao['Op2']])

    elif dict_execucao['Opcode'] == 'j':
        resgistradores['R0'] = 0

    elif dict_execucao['Opcode'] == 'halt':
        resgistradores['R0'] = 0

    elif dict_execucao['Opcode'] == '':
        resgistradores['R0'] = 0

    if dict_execucao['Opcode'] == 'add':
        dict_execucao['Temp3'] = str(int(dict_execucao['Temp1']) + int(dict_execucao['Temp2']))
    elif dict_execucao['Opcode'] == 'addi':
        dict_execucao['Temp2'] = str(int(dict_execucao['Temp1']) + int(dict_execucao['Temp3']))
    elif dict_execucao['Opcode'] == 'sub':
        dict_execucao['Temp3'] = str(int(dict_execucao['Temp1']) - int(dict_execucao['Temp2']))
    elif dict_execucao['Opcode'] == 'subi':
        dict_execucao['Temp2'] = str(int(dict_execucao['Temp1']) - int(dict_execucao['Temp3']))
    elif dict_execucao['Opcode'] == 'beq':
        if dict_execucao['Temp1'] == dict_execucao['Temp2']:
            resgistradores['R0'] = 0
    elif dict_execucao['Opcode'] == 'j':
        resgistradores['R0'] = 0
    elif dict_execucao['Opcode'] == 'halt':
        resgistradores['R0'] = 0
    elif dict_execucao['Opcode'] == '':
        resgistradores['R0'] = 0


def memoria(pc, hazardOn):
    dict_memoria['Opcode'] = dict_execucao['Opcode']
    dict_memoria['Op1'] = dict_execucao['Op1']
    dict_memoria['Op2'] = dict_execucao['Op2']
    dict_memoria['Op3'] = dict_execucao['Op3']
    dict_memoria['Temp1'] = dict_execucao['Temp1']
    dict_memoria['Temp2'] = dict_execucao['Temp2']
    dict_memoria['Temp3'] = dict_execucao['Temp3']
    dict_memoria['Valida'] = dict_execucao['Valida']
    dict_memoria['PC'] = dict_execucao['PC']

    if dict_memoria['Opcode'] == 'beq':
        inst = str(dict_memoria['PC'])
        primer_alg = int(inst[len(inst) - 1])
        #print(f"valor de primer_alg 2: {primer_alg}")
        if dict_memoria['Temp1'] == dict_memoria['Temp2']:
            if hazardOn and historico[primer_alg] == 0:
                historico[primer_alg] = 1
                pc = int(dict_execucao['Temp3'])
                dict_decodificacao['Valida'] = False
                dict_busca['Valida'] = False
            elif not hazardOn:
                pc = int(dict_execucao['Temp3'])
                dict_decodificacao['Valida'] = False
                dict_busca['Valida'] = False

        elif dict_memoria['Temp1'] != dict_memoria['Temp2'] and historico[primer_alg] == 1 and hazardOn:
            historico[primer_alg] = 0
            pc = int(inst)
            dict_decodificacao['Valida'] = False
            dict_busca['Valida'] = False

    return pc


def write_back(qtde_proc_falso):
    dict_temp['Opcode'] = dict_write_back['Opcode']
    dict_temp['Op1'] = dict_write_back['Op1']
    dict_temp['Op2'] = dict_write_back['Op2']
    dict_temp['Op3'] = dict_write_back['Op3']
    dict_temp['Temp1'] = dict_write_back['Temp1']
    dict_temp['Temp2'] = dict_write_back['Temp2']
    dict_temp['Temp3'] = dict_write_back['Temp3']
    dict_temp['Valida'] = dict_write_back['Valida']
    dict_temp['PC'] = dict_write_back['PC']

    dict_write_back['Opcode'] = dict_memoria['Opcode']
    dict_write_back['Op1'] = dict_memoria['Op1']
    dict_write_back['Op2'] = dict_memoria['Op2']
    dict_write_back['Op3'] = dict_memoria['Op3']
    dict_write_back['Temp1'] = dict_memoria['Temp1']
    dict_write_back['Temp2'] = dict_memoria['Temp2']
    dict_write_back['Temp3'] = dict_memoria['Temp3']
    dict_write_back['Valida'] = dict_memoria['Valida']
    dict_write_back['PC'] = dict_memoria['PC']

    if dict_temp['Valida']:
        if dict_temp['Opcode'] == 'add':
            resgistradores[dict_temp['Op3']] = int(dict_temp['Temp3'])

        elif dict_temp['Opcode'] == 'addi':
            resgistradores[dict_temp['Op2']] = int(dict_temp['Temp2'])

        elif dict_temp['Opcode'] == 'sub':
            resgistradores[dict_temp['Op3']] = int(dict_temp['Temp3'])

        elif dict_temp['Opcode'] == 'subi':
            resgistradores[dict_temp['Op2']] = int(dict_temp['Temp2'])

        elif dict_temp['Opcode'] == 'beq':
            resgistradores['R0'] = 0

        elif dict_temp['Opcode'] == 'j':
            resgistradores['R0'] = 0

        elif dict_temp['Opcode'] == 'halt':
            resgistradores['R0'] = 0

        elif dict_temp['Opcode'] == '':
            resgistradores['R0'] = 0
    else:
        qtde_proc_falso += 1

    return qtde_proc_falso


if __name__ == '__main__':
    qtde_proc_falso = 0
    contador_de_instrucoes = 0
    hazardOn = False
    lerArquivo('instrucoes.txt')
    print("Relação dos registradores")
    print(resgistradores)
    print("Relação das instruções de execução")
    print(instrucoes)

    opt = str(input("Deseja ligar a manutenção de hazards de controle? [S/N]: "))
    if opt[0].upper() == "S":
        print("Você ativou a proteção contra hazards de controle")
        hazardOn = True
        print()

    print("\033[0;30;41mO sistema será contínuo a partir de agora, para parar digite:'pare' \033[m")
    while PC < len(instrucoes) + 4:
        print('=' * 10)
        print("Registradores: ")
        print(resgistradores)
        print('=' * 10)
        print("Tabela de histórico")
        print(historico)

        qtde_proc_falso = write_back(qtde_proc_falso)
        PC = memoria(PC, hazardOn)
        execucao()
        decodificacao()
        PC = busca(PC, hazardOn)

        print("=" * 10)
        print("Fase de busca")
        print(dict_busca)
        print("=" * 10)
        print("Fase de decodificação")
        print(dict_decodificacao)
        print("=" * 10)
        print("Fase de execução")
        print(dict_execucao)
        print("=" * 10)
        print("Fase de memória")
        print(dict_memoria)
        print("=" * 10)
        print("Fase de write back")
        print(dict_write_back)

        teste = input("Next: ")
        if teste == "pare":
            break
        PC += 1
        contador_de_instrucoes += 1

    print()
    print()
    print("Estatísticas: ")
    print(f"Trocas de local no processador: {contador_de_instrucoes}")
    print(f"Quantidade de ciclos de clock: {contador_de_instrucoes / 5}")
    print(f"Quantidade de instruções inválidas: {qtde_proc_falso}")
