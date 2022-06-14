import random
#PRIMEIRO SUBPROGRAMA
def Criamatriz(x, y, operacao = None):
    i = 0 
    Matriz = []
    SegMatriz = []
    for i in range(0, y): #Primeira Matriz.
        linhaM1 = []
        for j in range(x):
            valor = random.randint(0, 22)
            linhaM1.append(valor)
        Matriz.append(linhaM1)

    for i in range(0, y): #Segunda Matriz.
        linhaM2 = []
        for j in range(x):
            valor = random.randint(0, 15 + j)
            linhaM2.append(valor)
        SegMatriz.append(linhaM2)

    if operacao == None: #Caso de soma de matrizes
        Soma = []
        for i in range(len(Matriz)):
            linhaSoma = []
            for j in range(len(Matriz[i])):
                linhaSoma.append(Matriz[i][j] + SegMatriz[i][j])
            Soma.append(linhaSoma)
        EscreveMatriz(Soma) #Escreve a matriz dentro de um arquivo, é uma chamada de outra funcao.
        return Matriz, SegMatriz, Subtracao

    elif operacao == 'Multiplicacao': #Caso de multiplicacao de Matrizes.
        Multi = []
        for i in range(len(Matriz)): #Percorre cada array dentro da matriz
            linhaMult = []
            for j in range(len(Matriz[i])): #Percorre cada elemento na matriz
                linhaMult.append(Matriz[i][j] * SegMatriz[i][j])
            Multi.append(linhaMult)
        EscreveMatriz(Multi) #Escreve a matriz dentro de um arquivo, é uma chamada de outra funcao.
        return Matriz, SegMatriz, Multi
    
    elif operacao == 'Subtracao':
        Subtracao = []
        for i in range(len(Matriz)):
            linhaSub = []
            for j in range(len(Matriz[i])):
                linhaSub.append(Matriz[i][j] - SegMatriz[i][j])
            Subtracao.append(linhaSub)
        EscreveMatriz(Subtracao) #Escreve a matriz dentro de um arquivo, é uma chamada de outra funcao.
        return Matriz, SegMatriz, Subtracao

#SEGUNDO SUBPROGRAMA
def EscreveMatriz(Matriz):
    with open('MatrizEscrita.txt', 'w') as text: #Abre o arquivo para escrever a matriz.
        text.write('Soma de Matriz De programa Escrito\n')
        for k in range(len(Matriz)):
            for m in Matriz[k]:
                # text.write('-'*len(Matriz[k]))
                text.write(str(m))
                text.write(' ')
            text.write('\n')

def MaioresEMenores(): #Vai ler e dizer quem é quem
    pass

#PROGRAMA PRINCIPAL
Colunas = int(input('Informe a quantidade de colunas: '))
Linhas = int(input('Informe a quantidade de linhas: '))
print(Criamatriz(Colunas, Linhas, 'Multiplicacao')) #Forma de desempacotamento em 3 variaveis devido o return
# EscreveMatriz(M3)
