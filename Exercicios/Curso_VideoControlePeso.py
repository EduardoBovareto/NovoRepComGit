peso = count_pessoas = 0
maior = menor = 0
flag = ''
while True:
    peso = float(input('Write your weight: '))
    count_pessoas += 1
    if maior == 0 or maior < peso:
        maior = peso

    if menor == 0 or menor > peso:
        menor = peso
        
    flag = input('Do You want continue: [sim - nao]').lower()
    while flag not in ['sim','nao']:
        flag = input('Do You want continue: [sim - nao]').lower()

    if flag == 'nao':
        break
print(f'''O maior peso foi: {maior}, o menor foi: {menor},
       e o total de pessoas analisadas: {count_pessoas}''')