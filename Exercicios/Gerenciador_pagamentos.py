def GerenciaPay(gasto):
    loja = 'Loja do Eduardo'
    print(f'{loja:-^40}')
    forma_pagamento = int(input('''
        [1] A vista dinheiro ou cheque
        [2] a vista no cartão
        [3] 2x no cartão
        [4] 3x ou mais no cartão
        
        Qual a opção: 
'''))
    valor_final = 0

    if forma_pagamento == 1:
        valor_final = gasto * (1 - 0.1)
        print(f'''
            Pagando a vista no dinheiro ou cheque, será inserido um desconto de 10% sobre o valor de compra!
              A partir do valor inicial {gasto} o total a pagar será de: R${valor_final:.2f}''')
        
    elif forma_pagamento == 2:
        valor_final = gasto * (1 - 0.05)
        print(f'''
            Pagando a vista no cartão, será inserido um desconto de 5% sobre p valor da compra!
              A partir do valor inicial {gasto}, o total a pagar serã de R${valor_final:.2f}
              ''')

    elif forma_pagamento == 3:
        valor_final= gasto
        print(f'''
            Pagando 2x no cartão, o valor que será pago será de: R${gasto} nao sendo adicionado taxa de serviço e etc. 
              Valor final: R${valor_final:.2f}
        ''')
        
    elif forma_pagamento == 4:
        valor_final = gasto * (1+0.2)
        print(f'''
        Pagando em 3x ou mais no cartão será inserido 20% de juros por mes
        valor incial {gasto}.
        valor com juros: {valor_final:.2f}
''')
    else:
        print('Favor, Fornecer uma das opções mostradas acima!')
        
gasto = float(input('Escreva o valor total das compras: '))
GerenciaPay(gasto)
