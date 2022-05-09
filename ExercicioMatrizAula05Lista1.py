'''
Gerar uma matriz 12 por 12.
Ler um numero, que indicará uma linha da Matriz, onde será realizada uma operação, deve ter uma letra de identifcação da operação a ser feita (Média ou soma).
'''
from random import randint
L = int(input('Informe o valor de linha para operação: '))

if L < 0 or L > 11:
    print('O valor deve estar entre os conjuntos [0, 11]')
    L = int(input('Informe novamente o valor da linha'))

Operacao = input('Informe a operação a ser realizada em maiúsculas: "M" ou "S"') # S ou M 
Matriz = []
for i in range(1, 12): # Realiza o incremento de cada linha na matriz
    line = []
    for j in range(1, 12):
        numero = randint(0, 500)
        #float(input(f'\nInforme o valor da celula {j}:\n '))
        line.append(numero)
    Matriz.append(line)
soma = 0
Media = 0
for i in range(L, L + 1):
    for j in Matriz[i]:
        if Operacao == 'S':
            soma += j
        else:
            Media += j

    if Operacao == 'M':
        Media = Media / len(Matriz[L])
        print(Media)
        
    else:
        print(soma)