#Exercicio de criptografia 1024 Beecrownd
#pode ser escalado para tratar nao so letras, mas simbolos tambem
def Cripto(mensagem):
    mensagem = mensagem.strip()
    MenTemp = ''
    i = 0
    #1 maiusculas e minuculas devem deslocar 3 posicoes na tabela ascii a direita - usar isupper() - OK
    #2 a linha deve ser invertida - OK
    #3 A metade da string deve andar uma posicao - OK
    #Falta resolver a umta linha do enunciado do problema
    for i in range(len(mensagem)):
        if (mensagem[i].isupper() or mensagem[i].islower()):
            temp = ord(mensagem[i]) + 3 #capta o codigo dentro da tabela ASCII-ord() + 3
            MenTemp += chr(temp)
            temp = ''
            continue

        elif (mensagem[i].isascii()):
            temp = ord(mensagem[i]) + 3 #capta o codigo dentro da tabela ASCII-ord() + 3
            MenTemp += chr(temp) #acha na tabela ascii qual caracter corresponde a tal
            temp = ''
            continue

    temp = MenTemp
    MenTemp = ''
    i = len(temp) -1 #percorrer de tras pra frente
    while i >= 0:
        MenTemp += temp[i]
        i -= 1
    meio = len(MenTemp)
    meio = meio // 2 #buscando o meio da string
    TratadoFinal = MenTemp[meio::-1]

    return TratadoFinal
            

m = str(input('Escreva uma mensgem para analise: '))
print(Cripto(m))