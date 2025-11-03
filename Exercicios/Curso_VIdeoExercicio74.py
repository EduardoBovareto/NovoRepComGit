from random import randint
numeros = []
maior = menor = 0
numeros  = [randint(0,20) for i in range(5)] 
#gera valores inteiros para u laço de 0-5 dentro da lista

t =  tuple(numeros)

for i in range(0,5):
    
    if maior == 0 or maior < t[i]:
        maior =  t[i]

    if menor == 0 or menor > t[i]:
        menor = t[i]

print(f'Numeros gerados: {numeros}, Maior valor: {maior}, menor valor: {menor}')