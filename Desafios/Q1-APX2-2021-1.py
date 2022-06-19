#SUBPROGRAMA
def SomaArray(Lista): #Faz a soma dos valores da linha recebida
    pass
    soma = i = 0
    while i < len(Lista):
        soma += Lista[i]
        i += 1
    return soma   

def ProcessaMatriz(Arq):
    with open(Arq, 'r+') as Linhas:
        SomasMaior = Maior = 0
        Menores = counter = 1
        Valores = []
        LinhaMaior = 0
        for Linha in Linhas:
            Valores = list(map(int, Linha.split())) #Pode pegar Linha[i] de linhas que é melhor para anlisar o numero da linha
            counter += 1 #Conta as linhas
            Soma = SomaArray(Valores) #Passa cada arrar para percorrer e somar
            if Soma > Maior: #CASO DE MAIOR
                Maior = Soma
                LinhaMaior = Valores
                SomasMaior = Linha
                posi = counter

            elif Soma < Menores: #CASO DE MENOR
                Menores = Soma
        Valores = [] #Limpa os valores para pegar outra linha
        k = 0
        i = k + 1
        while k < len(LinhaMaior) - 1: #Organização da linha, pode instituir algoritimos, o de fora é uma posicao a menos que o de dentro
            while i < len(LinhaMaior):
                if LinhaMaior[k] > LinhaMaior[i]: #Precisa de um algoritimo de ordenacao
                    temp = LinhaMaior[i]
                    LinhaMaior[i] = LinhaMaior[k]
                    LinhaMaior[k] =  temp
                i += 1
            k += 1
            i = k + 1
        Linhas.seek(0)
        for Linha in Linhas:
            if SomasMaior == Linha:
                Linhas.write(f'\n{str(LinhaMaior)}')

    #PROGRAMA PRINCIPAL Delta.txt e Gama.txt
Arquivo = input('Informe o nome do arquivo.txt:')
ProcessaMatriz(Arquivo)
