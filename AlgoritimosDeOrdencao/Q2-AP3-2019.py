#SUBPROGRAMA
def ProcessaTexto(Arquivo):
    with open(Arquivo, 'r') as Linhas:
        for Linha in Linhas:
            Palavras = list(Linha.split())
            i = 0
            j = 1
            for i in range(len(Palavras)- 1):
                menor = i
                for j in range(1, len(Palavras)):
                    if Palavras[i][i] > Palavras[j][i]:
                        menor = j

                if Palavras[i] < Palavras[menor][i]:
                        temp = Palavras[j]
                        Palavras[j] = Palavras[i]
                        Palavras[i] = temp

#PROGRAMA PRINCIPAL
Arq = input('Informe o nome do arquivo contendo dado: ') #Basededados.txt
ProcessaTexto(Arq)
