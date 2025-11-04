from random import randint as ran
from math import ceil
array_temp = []
temp =  preco_final = indice = 0
flag = ''
produtos = [
    ('Notebook', 3500.00, 10, ran(0,9)),
    ('Gabinete Simples Azul', 700.30, 40, ran(10,30)),
    ('Celular A346', 2360.99, 190, ran(30,35)),
    ('Teclado Mecânico', 450.50, 30, ran(35,50)),
    ('Mouse Gamer', 150.90, 50, ran(50,55)),
] #prpdutos da loja, adicionado os diferentes ranges de desconto

print('\n\n')#enquadramento no terminal
print(f'{'Bem vindo a Tectropolis':.^30}\n\n')

for itens in produtos:
    temp = ceil((itens[1] * (100 - itens[3])) / 100) #calcula o desconto e arredonda
    array_temp.append(temp)#calcula desconto em cima do valor

for nome, preco, estoque, desconto in produtos: #mostra cada produto
    preco_final = ceil((preco * (100 -  desconto)) / 100 )#calculo do dvalor com desconto
    print(f'{indice}-{nome:.<25}| Estoque: {estoque:.>15}| Preco: R${preco:.>15.2f} | Desconto atual: {desconto:.>10}%| Valor final:R$ {preco_final:.>10}')
    indice += 1
produtos.append(tuple(array_temp))#adiciona a nova tupla de valores calculados final de desconto
while True:
    escolha = int(input('Qual produto deseja leva hoje? '))
    #opcoes de escolha do cliente
    if escolha == 0:
        pass
    elif escolha == 1:
        pass
    elif escolha == 2:
        pass
    elif escolha == 3:
        pass
    else:
        pass

    flag = input('\n\nDeseja continuar a compra: [S/N]').upper().strip() #controle de selecao e parada
    while flag not in 'S, N':
        flag = input('\nESCOLHA UMA DAS OPCOES!Deseja continuar a compra?[S-N] ')
    if flag == 'N':
        break


'''
A tupla array_temp foi adicioanda por ultimo devido ter 5 outras tuplas com 4 indices e a tupla de valores calculados em cima dos deconstos possuir 5 indices.

proximas operacoes:
    Calcular o total da compra aplicando o desconto correspondente.
    Mostrar o valor total final.
'''
