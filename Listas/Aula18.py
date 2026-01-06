galera = list()
dado = list()
totalmaior = totalmenor = 0
for c in range(0,3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])#copia
    dado.clear()
print(galera)
for i in galera:
    if i[1] >= 21:
        print(f'{i[0]} e Maior de idade')
        totalmaior += 1
    else:
        print(f'{i[0]} e Menor de idade!')
        totalmenor += 1
