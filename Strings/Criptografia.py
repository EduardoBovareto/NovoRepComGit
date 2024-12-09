#Exercicio de criptografia 1024 Beecrownd
#pode ser escalado para tratar nao so letras, mas simbolos tambem

  #1 maiusculas e minuculas devem deslocar 3 posicoes na tabela ascii a direita - usar isupper() - OK
    #2 a linha deve ser invertida - OK
    #3 A metade da string deve andar uma posicao - OK
    #Falta resolver a ultima linha do enunciado do problema
    

def Cripto(mensagem):
    mensagem = mensagem.strip() #Retira os espaços e excesso
    MenTemp = ''
    i = 0
  
    for i in range(len(mensagem)): #percorre a mensagem para troca
        if (mensagem[i].isupper() or mensagem[i].islower()):
            temp = ord(mensagem[i]) + 3 #capta o codigo dentro da tabela ASCII-ord() + 3
            MenTemp += chr(temp) #gera o caracter na tabela ASCII perante o valor
            temp = ''
            continue
        
        elif (mensagem[i].isupper() ==False or mensagem[i].islower() ==False): #se for um sibolo ou um espaço
            MenTemp += mensagem[i]
            pass
        
        # Tudo que esta aqui seria caso ele pedisse para tratar caracteres especiais também, como não pediu!
            # MenTemp += chr(temp) #acha na tabela ascii qual caracter corresponde a tal
            # temp = ''
            # continue
        # '''

    temp = MenTemp
    MenTemp = ''
    i = len(temp) -1 #percorrer de tras pra frente
    while i >= 0:
        MenTemp += temp[i]
        i -= 1
    meio = len(MenTemp)
    meio //= 2 #Forma simplificada de operação
    MenFim = MenTemp[meio::-1] #string mensagem operada ate o meio
    MenTemp = '' # limpa a variavel temporaria
    
    for i in range(len(MenFim)):
        temp = ord(MenFim[i]) - 1
        MenTemp += chr(temp)
        temp = '' #se nao esvaziar temp ele concatena com o que esta dentro sempre
    MenFim = MenTemp
    MenTemp = ''
    
    return MenFim            

m = str(input('Escreva uma mensgem para analise: '))
print(Cripto(m))