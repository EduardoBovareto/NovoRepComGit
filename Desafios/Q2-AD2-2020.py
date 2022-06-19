#SUBPROGRAMA
def ProcessaPrimos(Arquivo):
    with open(Arquivo, 'r') as Linhas:        
        #Valores = list(map(int(), Linhas.split()))#Coleta de valores do primeiro arquivo
        divisores = list(range(1, 10))
        counter = 0
        NaoPrimos = 0 #Conta se na linha não tem primos
        Primos = []
        for linha in Linhas:
            Valor = list(map(int, linha.split()))
            for i in range(len(Valor)): #Passa em cada elemento do array
                for j in range(len(divisores)): #Passa por cada divisor
                    if (Valor[i] % divisores[j]) == 0:
                        counter += 1

                if counter == 2: #Vê a quantidade de divisores do elemento
                    Primos.append(Valor[i])
                    counter = 0
                    continue
                if Valor[i] not in Primos:
                    NaoPrimos += 1
                    counter = 0
        
            if NaoPrimos == len(Valor) - 1:
                Escreve(None)
                break
            
            elif NaoPrimos != 0:
                for integrantes in Primos:
                    temp = []
                    temp.append(str(integrantes))
                Escreve(temp)
                continue
def Escreve(Array):
    Arquivo = input('Informe o nome de arquivo que deseja receber o processamento:')
    with open(Arquivo, 'w') as Lines:
        if Array != None:
            Lines.write(Array)
        else:
            Lines.write()        
#PROGRAMA PRINCIPAL, O nome do arquivo existente inicial é inteiros.txt
Arq = input('Digite o nome do arquivo existente no formato: .txt ')
ProcessaPrimos(Arq)
