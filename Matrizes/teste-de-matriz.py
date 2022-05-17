from random import randint

def criaMatriz(l, c):
    lista = []
    for i in range(l):
        for j in range(c):
            lista.append(randint(1, 20))
        Matriz.append(lista)
        lista = [] # se precisa zerar a lista para n acumular valores
    print(Matriz)

def imprimeMatriz(m):
    for i in range(len(m)):
        for j in m[i]:
            print(j, end = ' ')
        print()
    return 'FIM '
    
#PROGRAMA PRINCIPAL#        
linha = int(input('Informe quantas linahs deseja'))
coluna = int(input('Informe a quantidade de colunas'))
Matriz = []
# Laço 1: DE FORA , trabalha com a quantidade de linhas.
# lAÇO 2: DE DENTRO, trabalha com a quantidade de colunas.

criaMatriz(linha, coluna)
print(imprimeMatriz(Matriz))