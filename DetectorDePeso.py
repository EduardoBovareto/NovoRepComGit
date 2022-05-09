'''
    Detector de peso que ao digitar o valor emitirá uma mensagem.
    Essa mensagem será emitida caaso ele seja o maior que o peso digitado
    anteriormente.
    Ajeitar algumas coisas
'''
def MostraMensagem(Peso, maior, menor):
    print('\n{:=^20}'.format('DETECTOR DE PESO!'))
    print(f'O valor de peso digitado é: {Peso} e o peso maior é: {maior}')

maior = 0
pesos = 0
Pessoas = int(input('Informe a quantidade de pessoas:'))
while Pessoas != 0:
    pesos = float(input('Informe seu peso:'))

    if maior < pesos:
        maior = pesos
    else:
        menor = pesos
    MostraMensagem(pesos, maior, menor)
    Pessoas -= 1 # Decremento de numero de pessoas que quebra o while
    if Pessoas == 0:
        print('''
            ===========Obrigado por nos confiar as suas informações!============
        ''')
    