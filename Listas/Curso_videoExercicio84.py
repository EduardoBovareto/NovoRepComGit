flag = ''
pessoas = []
maior = menor = 0
pesados = []
leves = []
while True:
    nome = input('\nEscreva um nome de uma pessoa: ')
    peso = float(input('Escreva o peso: '))
    pessoas.append(nome)

    if maior < peso or maior == 0:#exite um mais pesado que o atual
        #caso exista a galera que estava sai porque e mais leve
        maior = peso
        pesados.clear()
        pesados.append(nome) #necessario orientar o usuario quanto a valores

    elif maior == peso and nome not in leves:#tem o mesmo peso que o cara pesadao
        pesados.append(nome)#mostrar o peso que foi guardado tambem

    if menor > peso or menor == 0:#mais leves
        #caso exista uma galera mais leve eles entram e as mais pesadas saem
        menor = peso
        leves.clear()
        leves.append(nome)

    elif menor == peso and nome not in leves:#mesmo peso leve que o levinho
        leves.append(nome)

    flag = input('\nDeseja continuar: S/N').upper()
    while flag not in 'S N':#controle de escolha
        flag = input('Erro! Deseja continuar: S/N').upper()
    if flag == 'N':
        break
print(f'\nTotal de pessoas cadastradas: {len(pessoas)}')
print(f'O maior peso foi:{maior} Peso de {pesados}')
print(f'\nO menor peso foi de:{menor} Peso de {leves}')
