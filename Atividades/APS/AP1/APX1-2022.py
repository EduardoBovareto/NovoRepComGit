def Verifica(valores):
    if valor != []:
        maior = numeros[0]
        menor = numeros[0]
    else:
        maior = 0
        menor = 0
    for k in valores:
        if k > maior:
            maior = k
        if k < menor:
            menor = k
    print(f'O maior {maior}, o menor {menor}')    

somas = 0
valor = 0
counter = 0

valor = input().split()
while valor != []:
    if valor == [] and counter == 0:
        controle = -1
    elif valor != [] or valor != "":
        numeros = []
        maior = 0
        for i in valor:
            num = []
            temp = float(i)
            numeros.append(temp)
            somas = somas + float(i)
            # if valor[0] == []:
            #     controle = -1
        counter += len(numeros)
        Verifica(numeros)
        valor = input().split()
if counter == 0:
    print('Nenhum Número Foi Lido. Portanto, não existe média!!!')
else:
    print('Quantidade de numeros lidos: {}'.format(counter))
    print('Média dos números lidos: {:.2f}'.format(somas / counter))
