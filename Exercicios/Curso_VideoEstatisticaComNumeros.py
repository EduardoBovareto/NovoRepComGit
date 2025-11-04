from random import randint
numeros = tuple([randint(0,10) for i in range(0,10)])
maior =  menor = count  = 0
for i in numeros:
    if maior == 0 or maior < i: #caso de maior valor ou quando incia com 0 a variavel
        maior = i
    elif menor == 0 or menor > i:#caso de menor valor ou quando incia com 0 a variave
        menor = i
    
    elif i == 5: #caso de valores 5
        count += 1
print(numeros)
print(f'O Numero 5 aparece {count} vezes\nMaior valor:{maior},\nMenor valor:{menor}')