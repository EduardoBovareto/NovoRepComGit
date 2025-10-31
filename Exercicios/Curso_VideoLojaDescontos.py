preco = pagamento = total = 0
flag = ''
while True:
    preco = float(input('Descreva o preço do produto: '))
    while preco < 0: #caso de valor negativo
        preco = float(input('Descreva o preço do produto: '))
    
    pagamento = int(input(''''Informe a maneira de pagamento
        \nA vista 10% de desconto[0]\n
        Cartao 5 porcento de desconto[1]\n
        Dinheiro Valor normal[2]\n
        2x cartao 20% de juros[3]\n
        3x ou mais no cartao 40% de juros[4]\n
        :'''))
        
    if pagamento == 0: #10% de desconto
       total += (preco * (100 - 10)) / 100

    elif pagamento == 1: #5% de desconto
        total += (preco * (100 - 5)) / 100

    elif pagamento == 2: #caso de preco normal
        total += preco

    elif pagamento == 3: #caso de 20% de juros no cartao
        total += (preco * (100 + 20)) / 100

    print(f'\nValor atual: {total}\n')
    flag = input('Deseja continuar comprando: [sim-Não]').capitalize()

    while flag not in ['Nao','Sim','Não']: #caso de escrita errada
        flag = input('Deseja continuar: [sim-Não]')

    if flag in ['Nao','Não']:
        break
print(f'Valor total pago: {total}')

