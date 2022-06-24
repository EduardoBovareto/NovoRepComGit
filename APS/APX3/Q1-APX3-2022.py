#SUBPROGRAMA
from math import sqrt
def AchaDiferenca(X, nm):
    D1 = Distancia = 0 #Distância de pontos X1 e X2
    D2 = 0 #Distância de pontos Y1 e Y2
    i = 0
    for Linha in nm:
        Y = list(map(int, Linha.split()))  
        D1 = (X[i] - X[i + 1]) ** 2 #x1, x2
        D2 = (Y[i] - Y[i + 1]) ** 2 #y1, y2
        Distancia += sqrt(D1 + D2)
    return Distancia
def ProcessaPontos(Arquivo):
    Diferenca = 0
    Arquivo  = open(Arquivo, 'r')
    i = 0
    if len(Arquivo.read()) == 0 :
           print('Arquivo de pontos está vazio!!!')
           return None
    else:
        Arquivo.seek(0)
        for Linha in Arquivo:
            # Linha = Arquivo.readline()
            print(Linha)#Formalizar
            Pontos = list(map(int, Linha.split()))
            Diferenca += AchaDiferenca(Pontos, Arquivo)
    print(f'{Diferenca:.2f}')
    Arquivo.close()
    return None
#PROGRAMA PRINCIPAL
Nome = input('Informe o nome do arquivo: ')
ProcessaPontos(Nome)
#Vazio.txt; UmPonto.txt; Pontos.txt
