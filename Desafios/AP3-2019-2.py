'''                                 QUESTAO 1
Analisa dois inteiros e vê a diferença ou a margem de de distância entre eles.
O Arquivo analisado em txt é o "DuplaInteiros.txt". 
    
    Não se pode, na maioria dos casos pegar toda a informação de um arquivo, por mais que python permita uso ilimitado da memória, sendo o limitante ela própria, não se deve congestioná-la.
'''
#SUBPROGRAMA
from math import sqrt #Raiz quadrada == Square Root
                
def DistanciaPontos(X, nm):#X e Y devem ser Arrays para cada um ter Xa e Xb assim como Y
    D1 = 0 #Distância de pontos X1 e X2
    D2 = 0 #Distância de pontos Y1 e Y2
    i = 0
    Dist = -1
    with open(nm, 'r') as Linhas:
        for Linha in Linhas:
            Y = list(map(int, Linha.split()))  
            D1 = (X[i] - X[i + 1]) ** 2 #x1, x2
            D2 = (Y[i] - Y[i + 1]) ** 2 #y1, y2
            Distancia = sqrt(D1 + D2)
            if Distancia > Dist:
                Dist = Distancia
    return X, Y, Dist    # Usar sistema de maio e menor valores para esse return lá fora

def ProcessaArquivo(Arquivo):
        with open(Arquivo, 'r') as Linhas:
            Inteiros = []
            Vmaior = 0
            i = 0
            for Linha in Linhas:
                Inteiros = list(map(int, Linha.split())) #Pega a dupla de inteiros
                PontoA, PontoB, Resultado = DistanciaPontos(Inteiros, Arquivo) #Chamada de funcao
                Resultado = float(f'{Resultado:.3f}')
                if Vmaior < Resultado:
                    Vmaior = Resultado
            print(PontoA, PontoB, Vmaior)
            return PontoA, PontoB, Vmaior #Retorna os dois pontos e o valor maior
#PROGRAMA PRINCIPAL
Nome  = input('Informe o nome do Arquivo de analise: ')#Arquivo Existente
ProcessaArquivo(Nome)#Nome == DuplaInteiros.txt
#Essa é uma estratégia de recursividade com repeticao forçada usando estrutura de dados.