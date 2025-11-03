from random import randint
numeros = []
maior = menor = 0
for i in range(0,5):
    numeros.append(randint(0,20))
    if maior == 0 or maior < numeros[i]:
        maior =  numeros[i]

    if menor == 0 or menor > numeros[i]:
        menor = numeros[i]

print(f'Numeros gerados: {numeros}, Maior valor: {maior}, menor valor: {menor}')