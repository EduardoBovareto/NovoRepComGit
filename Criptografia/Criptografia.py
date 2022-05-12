'''
Esse algorítimo trata de uma criptografia de palavras dentro da tabela ASCII, inicialmente de numeros e letras, ou seja, de certa forma limitado

Alterar o uso de variaveis desse código, acho que se deve limpar um pouco mais, pois tem variaveis sendo usadas sem necessidade.
'''
def Criptografa(informacao, padrao): # Função de criptografia
    temp = informacao # Variavel temporaria
    informacao = []
    # Ainda não sei converter diretamente um array para uma  string e vice-versa

    PalavraFinal = ''
    for i in temp:
      informacao.append(i) # Adiciona cada caracter a cara posição de array para analisar

    for i in range(len(informacao)):
        j = i + 2
        if informacao[i] in padrao:
            informacao[i] = padrao[j]
        else:
            informacao[i] = '#'
        PalavraFinal += str(informacao[i]) # Pega a letra
    
    return PalavraFinal
Asc = ['A', 'B', 'C', 'D', 'E', '@', '#'] # Adicionar mais letras ou usar o modulo de ASCII
for i in range(1, 10):
    Asc.append(i)
print(Asc)
Palavra = input('Informe a mensagem a ser escondida: ')
print('\nO valor antigo é: {}'.format(Palavra), '\nO criptografado é: ', Criptografa(Palavra, Asc))