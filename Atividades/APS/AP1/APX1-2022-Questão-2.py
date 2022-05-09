def processaNome():
    nome = input().split()
    nomeM = nome[0]
    print(nomeM)
    print(nome[-1])
qtdNomes = int(input())
for i in range(qtdNomes):
    processaNome()