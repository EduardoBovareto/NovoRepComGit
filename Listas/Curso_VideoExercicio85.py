numeros = input('Digite 7 numeros separados por espaco: ').split()
while len(numeros) < 7:
    print(f'Erro! Falta {7 - len(numeros)} numero(s)')
    numeros = input('Escreva novamente os numeros separados por espaco: ').split()
numeros = list(map(int, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))
impares =  list(filter(lambda x: x % 2 != 0, numeros))
print(f'\nOs valores pares digitados foram: {pares}')
print(f'\nOs valores impares digitados foram: {impares}')
