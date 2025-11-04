from random import randint
numeros = 0
temp = []
first_tupla = tuple([randint(0,100) for numeros in range(0,20)])
second_tupla = tuple([randint(0,10) for numeros in range(0,20)])
#gera os valores aleatorios das tuplas 20 vezes

first_tupla = tuple(set(first_tupla)) #retira valores repetidos
second_tupla = tuple(set(second_tupla)) #retira valores repetidos
print(f'\n\nConcatenacao: {tuple(first_tupla + second_tupla)},\nsem valores repetidos:\n\n {first_tupla},\n{second_tupla}') #concatenacao das tuplas

for numeros in first_tupla:
    if numeros % 2 == 0: #caso de par
        temp.append(numeros) #array para esta primeira tupla
    
temp = tuple(temp)
print(f'\n\nA primeira tupla de pares e: {temp}') #primeira tupla de pares
temp = []

for numeros in second_tupla:
    if numeros % 2 == 0:
        temp.append(numeros)
temp =  tuple(temp)
print(temp)