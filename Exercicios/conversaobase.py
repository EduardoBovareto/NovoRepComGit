value =  int(input('Escreva um numero inteiro para conversão: '))
conv = int(input('''Selecione a conversão abaixo:
                 [1] = Binario
                 [2] = Hexadecimal
                 [3] = Octadecimal
                '''))
if(conv == 1):
    bin = bin(value)
    print(f'O resultado de conversao do valor {value} em Binario e:{bin[2::]}')

elif(conv == 2):
    print(f'O resultado de conversao do valor {value} em Hexadecimal e:{hex(value)[2::]}')

elif(conv == 3):
    print(f'O resultado de conversao do valor {value} em octadecimal e:{oct(value)[2::]}')

else:
    print('Ha algo de errado! Favor reenviar o valor digitado!')