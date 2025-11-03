pares = ' '
numeros = tuple([(int(input('Digite um valor: '))) for i in range(4)])
print(numeros.index(3))
print(f'A posição do primeiro valor 9 é: {numeros.count(9)} vezes')
print(f'O numero 3 aparece a primeira vez a posição: {numeros.index(3)}') if numeros.index(3) >= 0 else print(f'O valor de numero 3 nao foi digitado em nenhuma posição!')
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        pares += str(numeros[i]) + ','
print(f'Valores pares digitados: {pares}')