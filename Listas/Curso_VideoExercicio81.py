lista_vdigitado = []
temp = 0
repetido = flag = ''

def Flag(): #PARA O PROGRAMA, pois sera usado em outros blocos locais
    flag = input('You want continue? [y/n]').strip().lower()
    while flag not in 'y n':
        flag = input('Entry wrote incorrect! Please write again: [y/n]')
    if flag == 'n':
       return 'n'
    
while True:
    temp = float(input('Write a value: '))
    if temp in lista_vdigitado:
        repetido = input('The number wrote is in the list, you want to add it again? [y/n] ')

        if repetido == 'n':
            flag = Flag()
        else:
            lista_vdigitado.append(temp)

    else:
        lista_vdigitado.append(temp)
    
    flag = Flag()
    if flag == 'n':
        lista_vdigitado.sort(reverse=True)
        break
    
print(f'Os valores digitados foram: {lista_vdigitado}')
print(f'Total of values wirted: {len(lista_vdigitado)}')
print('The number 5 is in the list') if 5 in lista_vdigitado else print('5 not in list!')