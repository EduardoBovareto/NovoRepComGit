
import random
def imprimeMatriz(m):
    for i in range(len(m)): # Laço que repete de acordo com o tamanho da linha, cada lista é uma linha
        for j in m[i]: # Laço que irá pegar os elementos de cada lista, se i == 0 ele pega o elemento na posição 0
            print(j, end = " ")
        print() # precisa colocar esse print para ele pular a linha
        

linha = 4
coluna = 3
i = 0
j = i + 1
Matriz = []

for i in range(linha): # cada linha é representada por uma lista dentro da matriz
    line = []
    # print(line)
    for j in range(coluna): # cada elemento seria a coluna
        # colum = [] isso é para percorrer caso se precise dividir o valores no print
        num = random.randint(1, 20)
        line.append(num)
        # print(line)
    Matriz.append(line)
    # print(Matriz)

for line in Matriz: # Laço das lstas até a matriz final, tamanho dela, 
    print(line)

# Cada lista é uma linha e cada elemento de cada lista é uma coluna
imprimeMatriz(Matriz)
