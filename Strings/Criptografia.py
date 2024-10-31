#Exercicio de criptografia 1024 Beecrownd
#pode ser escalado para tratar nao so letras, mas simbolos tambem
def Cripto(mensagem):
    mensagem = mensagem.strip()
    MenTemp = ''
    i = 0
    #1 maiusculas e minuculas devem deslocar 3 posicoes a direita - usar isupper()
    #2 a linha deve ser invertida
    #3 A metade da string deve andar uma posicao

    for i in range(len(mensagem)):
        if (mensagem[i].isupper() or mensagem[i].islower()):
            temp = ord(mensagem[i]) + 3#capta o codigo dentro da tabela ASCII-ord() + 3
            #MenTemp = mensagem[:i] #pega a mensagem antes da alteração
            MenTemp += chr(temp)
            temp = ''
    temp = MenTemp
    MenTemp = ''
    for i in range(len(temp)): #percorre a string atual
        MenTemp += MenTemp[i * -1] #inversao de palavras
    return MenTemp
            

m = str(input('Escreva uma mensgem para analise: '))
print(Cripto(m))