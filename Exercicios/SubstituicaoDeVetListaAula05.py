'''
Algorítimo que faz a substituição de valores negativos e nulos por 1
'''
x = []
for i in range(1, 11):
    numero = int(input(f'Informe o valor de numero {i}:'))
    x.append(numero)

for i in range(len(x)):
    if x[i] == 0:
        x[i] = 1
    
    elif x[i] < 0:
        x[i] = 1
    print(f'x[{i}] = {x[i]}')