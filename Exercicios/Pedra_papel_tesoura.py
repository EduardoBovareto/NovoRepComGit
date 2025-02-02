from random import choice as ch
#Organiza jogo
def Jogo_de_escolhas(selecao = str):

    #torna as palavras iguais
    selecao = selecao.capitalize()
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    resposta = ch(opcoes) #escolhe a opção correta
    if selecao == resposta:
        print(f'PARABÉNS VOCÊ ACERTOU {resposta}')

    else:
        print(f'INFELIZMENTE VC ERROU! {resposta}')
print(f'''
    Bem vindon ao jogo de escolhas!
      {'Pedra Papel Tesoura':=^40}
    ''')
escolha = input('Escreva sua opção:')
Jogo_de_escolhas(escolha)