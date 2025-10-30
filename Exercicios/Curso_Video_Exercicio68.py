from random import randint
n = r = count = 0
escolha = valor = ''
while True:
    pc = randint(0,10)
    print('=-'*20)
    print('VAMOS JOGAR PAR OU ÍMPAR\n')
    print('=-'*20)

    n = int(input('Write a value: '))
    escolha = input('\nPAR ou IMPAR: [P-I]').upper()
    r = n + pc

    if r % 2 == 0:
        valor = 'P'
    else:
        valor = 'I'

    if escolha == valor: #caso de vitoria
        print(f'\nVoce jogou {n} e o computador jogou {pc},Total: {r} deu {valor}\n')
        print('\nVOCE VENCEU!')
        count += 1
    
    else:
        print('VOCE PERDEU!')
        print(f'Voce jogou {n} e o computador jogou {pc},Total: {r} deu {valor} ')
        break
print(f'\nGAME OVER! Voce venceu {count} vez')