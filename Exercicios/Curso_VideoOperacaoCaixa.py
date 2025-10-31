'''Codigo onde calcula as notas que serao sacadas por alguem
    
        valor_desejado = valor desejado a sacar
        qtd_pornota = quantidades das notas que foram geradas
'''
valor_desejado = i = temp = 0
notas = [100,50,20,5,2]
qtd_pornota = []

print( '-'*10, 'Bem vindo ao caixa Eletronico!', '-'*10)
print('\nNOTAS DISPONIVEIS: 100, 50, 20, 5, 2\n')
valor_desejado = int(input('Qual valor deseja sacar: '))
while valor_desejado < 1:
    valor_desejado = int(input('Favor fornecer valor a ser sacado maior que 1'))

while True:
 
    if valor_desejado >= notas[i]:
        temp = valor_desejado // notas[i]
        valor_desejado -= valor_desejado // notas[i]  * notas[i]
        print(f'Notas a serem geradas: {temp} de {notas[i]},00')
    i += 1

    if valor_desejado == 0 or valor_desejado == 1:
        print(f'{valor_desejado} Nao ser mais possivel sacar este valor, nao ha notas!')
        break

    