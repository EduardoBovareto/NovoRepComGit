#Q3 da APX2-2022
def ProcessaArquivos(Arquivo):
    pass
NomeArquivo = input('Informe o nome do Arquivo e a extensão: ')
pos = [0, 1, 2, 3, 4]
with open(NomeArquivo, 'r') as Linhas:
    pass
    for posicao in Linhas: # Pega as linhas
        Valores = list(map(int, posicao.split()))
    #     for k in range(len(posicao)): #Pega cada caractere
    #         if posicao[k] == '':
    #             pass

    #         elif posicao[k].isnumeric():
    #             int(posicao[k])

    #         elif posicao[k].isnumeric() and posicao[k + 1].isnumeric(): # caso de 2 algarismos
    #             pass

    #         elif posicao[k - 1].isnumeric() and posicao[ k + 1] == ' ': # Caso de 3 algarismos
    #             pass