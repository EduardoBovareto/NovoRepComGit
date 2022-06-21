#SUBPROGRAMA
def ProcessaPrimos(Arquivo):
    with open(Arquivo, 'r') as Linhas:        
        #Valores = list(map(int(), Linhas.split()))#Coleta de valores do primeiro arquivo
        divisores = list(range(1, 10))
        counter = 0
        NaoPrimos = 0 #Conta se na linha não tem primos
        Primos = []
        temporario = []
        for linha in Linhas:
            Valor = list(map(int, linha.split()))
            for i in range(len(Valor)): #Passa em cada elemento do array
                for j in range(len(divisores)): #Passa por cada divisor
                    if (Valor[i] % divisores[j]) == 0:
                        counter += 1
                    # if (counter == 1) and (Valor[i] != 1) and (Valor[i] % Valor[i] == 0) and Valor[i] not in Primos:
                    #     counter += 1

                if counter == 2: #Vê a quantidade de divisores do elemento
                    Primos.append(Valor[i])
                    counter = 0
                    continue
                
                if (counter == 1) and (j == 8) and (Valor[i] % Valor[i] == 0) and (Valor[i] > 1):
                    counter += 1
                    Primos.append(Valor[i])
                    counter = 0

                if Valor[i] not in Primos:
                    NaoPrimos += 1
                    counter = 0
        
            if NaoPrimos == len(Valor) - 1:
                Escreve(None, 'Resultado.txt') #Falta pular linha a cada escrita
                NaoPrimos = 0
                Primos = []
                break
            
            elif NaoPrimos != 0:
                NaoPrimos = 0
                temp = ''
                for integrantes in Primos:
                    temp += (str(integrantes)) + ' '
                temporario.append(temp)
                Primos  = []
                continue
        
        j = 0
        while i < len(temporario):
            temp = temporario[i].split()
            string = ''
            while j < len(temp):
                if temp[j] == None:
                    Escreve('Linha Vazia', 'Resultado.txt')
                else:
                    string += temp[j]
                    Escreve(string, 'Resultado.txt')
                    string = ''
                j += 1
            i += 1
            j = 0
            
def Escreve(informacao, nome):
    #Arquivo = input('Informe o nome de arquivo que deseja receber o processamento:')
    with open(nome, 'a') as Lines:
        Lines.write(f'{informacao}')
        Lines.write('\n')
        
#PROGRAMA PRINCIPAL, O nome do arquivo existente inicial é inteiros.txt e o resultado é Rsultado.txt
Arq = input('Digite o nome do arquivo existente no formato: .txt ')
ProcessaPrimos(Arq)
