flag = '' #condicao de parada
valor = temp = 0
lista_adicao = []
while True:
    temp = int(input('Digite um numero: '))
    if temp not in lista_adicao:
        lista_adicao.append(temp)
        print('Valor adicionado com sucesso...')

    else:
        print('Este valor ja esta cadastrado!')
    
    flag = input('\nDeseja continuar: [S/N]').upper().strip()

    while flag not in 'N S': #medida de controle
        flag = input('Tente novamente a opcao correta e S/N\n')
    if flag == 'N':
        lista_adicao.sort()
        break
print(f'Valores adicionados: {lista_adicao}')