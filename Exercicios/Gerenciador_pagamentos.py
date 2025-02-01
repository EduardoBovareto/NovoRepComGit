def GerenciaPay(gasto):
    loja = 'Loja do Eduardo'
    print(loja.center(36, '='))
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
              A partir do valor inicial {gasto} o total a pagar será de: R${valor_final}''')
        
    elif forma_pagamento == 2:
        valor_final = gasto * (1 - 0.05)
        print(f'''
              Pagando a vista no cartão, será inserido um desconto de 5% sobre p valor da compra!
              A partir do valor inicial {gasto}, o total a pagar serã de R${valor_final}
              ''')

    elif forma_pagamento == 3:
        print(f'Pa{gasto} R${forma_pagamento}')
        pass

gasto = float(input('Escreva o valor total das compras: '))
GerenciaPay(gasto)

'''
em ate 2x no cartao : preço normal
em ate 3x ou mais sera 20% de juros
'''
