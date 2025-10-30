#interrupção de lacos
'''
parte teorica da aula
while True:
    if 'terra' == True:
        pass
    if 'vazio' == True:
        print('pula')

    if 'moeda' == True:
        print('pega')

    if 'trofeu' == True:
        print('pula')
        break
'''
n = s = 0
while True:
    n = int(input('Write a number: '))
    if n == 999: #este if captura o 99 e n deixa somar, somando apenas os outros numeros
        break
    s += n
print(f'sun: {s}')