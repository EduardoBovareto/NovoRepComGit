''' Algorítimo que verifica 
    se o nome do usuário tem silva no nome
'''
Nome = str(input('Qual seu nome completo: '))
Nome = Nome.title().strip() # Metodos em sequência podem ser usados!
PosicaoSobreNome = Nome.find('Silva')
if PosicaoSobreNome != -1:
        print(True)
else:
    print(False)
# Da pra fazer com o for percorrendo o cada posição de array tbm
