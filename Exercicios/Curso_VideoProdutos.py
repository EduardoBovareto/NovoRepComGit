from random import randint as ran
from math import ceil
array_temp = []
temp =  preco_final = desconto_final =  indice = 0
flag = '' #condicao de parada
produtos = [
    ('Notebook', 3500.00, 10, ran(0,20)),
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

for nome, preco, estoque, desconto in produtos: #mostra cada produto desempacotado
    desconto_final = ceil((preco * (100 -  desconto)) / 100 )#calculo do dvalor com desconto
    print(f'{indice}-{nome:.<25}| Estoque: {estoque:.>15}| Preco: R${preco:.>15.2f} | Desconto atual: {desconto:.>10}%| Valor final:R$ {desconto_final:.>10}')
    indice += 1 #indice da tabela impresso

produtos.append(tuple(array_temp))#adiciona a nova tupla de valores calculados final de desconto
while True:
    qtd = i = 0 #variavel de acesso a primeira tupla de produtos
    j = 5 #variavel de acesso aos descontos em produtos
    #preco_final  que sera atribuido a compra do usuario

    escolha = int(input('Qual produto deseja leva hoje? '))
    #opcoes de escolha do cliente
    qtd = int(input('Pode informar  a quantidade do produto: '))
    
    if escolha == 0:#Notebook
        preco_final += (produtos[j][i] * qtd) #adiciona o valor do produto escolhido ja com desconto
        print(f'O valor a ser pago atual e:R${preco_final}')

    elif escolha == 1:#Gabinete
        i += 1
        preco_final += (produtos[j][i] * qtd)
        print(f'O valor a ser pago e de: R${preco_final}')

    elif escolha == 2:#Celular A346
        i += 2
        preco_final += (produtos[j][i] * qtd)
        print(f'O valor a ser pago e de: R${preco_final}')

    elif escolha == 3:#Teclado Mecanico
        i += 3
        preco_final += (produtos[j][i] * qtd)
        print(f'O valor a ser pago e de: R${preco_final}')

    else:#Mouse gamer
        i += 4
        preco_final += (produtos[j][i] * qtd)
        print(f'O valor a ser pago e de: R${preco_final}')   
    i = 0
    
    flag = input('\n\nDeseja continuar a compra: [S/N]').upper().strip() #controle de selecao e parada
    while flag not in 'S, N':
        flag = input('\nESCOLHA UMA DAS OPCOES!Deseja continuar a compra?[S-N] ')
    if flag == 'N':
        break
print(f'Valor total a ser pago:R${preco_final:.2f}\n')
print(f'''Pix Cartao de Credito-(12x S/Juros) Cartao de Debito-(Avista)''')
array_temp = input('Qual a foma de pagamento: ').strip().capitalize() #forma de pagamento em uma variavel que nao ser mais usada com []
while array_temp not in ['Pix' , 'Cartao de credito', 'Cartao de debito']:
    array_temp = input('Acho que escreveu errado! Digite novamente')

if array_temp == 'Pix':
    print(f'Finalizada a compra no Pix, valor: {preco_final}')

elif array_temp == 'Cartao de credito':
    vezes = int(input('Quantas vezes deseja:'))
    print(f'Finalizada a copra no Credito em {vezes}vezes de {preco_final} = {preco_final / vezes:.2f} ')

elif array_temp == 'Cartao de debito':
    print(f'Finalizada a compra no Cartao de Debito, valor total de: {preco_final}')
'''
A tupla array_temp foi adicioanda por ultimo devido ter 5 outras tuplas com 4 indices e a tupla de valores calculados em cima dos deconstos possuir 5 indices.
'''