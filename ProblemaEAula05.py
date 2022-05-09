from traceback import print_tb


qt = int(input('Informe a quantidade de analises: '))

for i in range(1, qt + 1):
    nomes = input('Informe o nome e opção escolhida [Par] ou [Impar]: ').split()

    if len(nomes[0]) > 100 or len(nomes[2]) > 100:
        print('\n Nomes muito grandes, devem ser só até 100 caracteres, emita denovo!')
        nomes = input('Informe os nomes e as escolhas: [PAR] [IMPAR]')
    NumeroInt = input('Informe os valores inteiros').split()

    for i in range(len(NumeroInt)):
        if NumeroInt[i].isnumeric():
          NumeroInt[i] = int(NumeroInt[i])
    soma = NumeroInt[0] + NumeroInt[1]

    # PosicaoPAr = nomes.find('PAR')
    # PosicaoImpar = nomes.find('IMPAR')

    if (soma % 2) == 0:
        print(f'{nomes[0]}, {nomes[1]}')
        
    else:
        print(f'{nomes[2]}, {nomes[3]}')
        #   Existe a brincadeira do maos iguais
        
        