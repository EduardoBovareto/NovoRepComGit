lista_vdigitado = []
temp = 0
repetido = flag = ''

def Flag(): #For program, Condition for stop by the user 
    flag = input('You want continue? [y/n]').strip().lower()
    while flag not in 'y n':
        flag = input('Entry wrote incorrect! Please write again: [y/n]')
    if flag == 'n':
       return 'n'
    
def MaiorMenor(lista): #Show the Highest values
    maior  = menor = 0
    for i in range(len(lista)): #Find the highest and Lowest values in list 
        if maior == 0 or maior < lista[i]:
            maior = lista[i]

        elif menor > lista[i]:
            menor = lista[i]
    return maior, menor

def Media(lista):
    m = sum(lista) #Do sum of list
    m /= len(lista) #average final
    return m

def Filtro(lista): #filter pair and odd
    pares = impares = ''
    for numeros in lista:
        if numeros % 2 == 0:
            pares += f'{numeros} '
        else:
            impares += f'{numeros} '

    return pares, impares

while True:
    temp = float(input('\nWrite a value: \n'))
    if temp in lista_vdigitado:
        repetido = input('\nThe number wrote is in the list, you want to add it again? [y/n] ')

        if repetido == 'n':
            flag = Flag()
        else:
            lista_vdigitado.append(temp)

    else:
        lista_vdigitado.append(temp)
        flag = Flag()#Condition of stop program by the user when no number repeated

    if flag == 'n':
        lista_vdigitado.sort(reverse=True)#List sorted and Reverse
        maior, menor = MaiorMenor(lista_vdigitado)#maior e menor
        m = Media(lista_vdigitado)#media
        pares, impares  = Filtro(lista_vdigitado)#impares e pares
        break
    
print(f'\nThe values wrote are: {lista_vdigitado}')
print(f'\nTotal of values wirted: {len(lista_vdigitado)}')
print('The number 5 is in the list') if 5 in lista_vdigitado else print('5 not in list!')
print(f'\nThe major value wrote is: {maior}\nThe minor value wrote is: {menor}')
print(f'\nThe average at all is: {m:.2f}')
print(f'\nThe values Pair are: {pares} and The values odd are: {impares}')
