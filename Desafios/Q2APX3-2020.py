#SUBPROGRAMA
def AnalisaDoc(Dados):
    with open(Dados, 'r') as Linhas:#Abre e Lê o arquivo linha a linha.
        counter = 0
        temp = Primos = []
        qtdPrimo = 0
        LineNuber = 1
        for linha in Linhas:
            Inteiros = list(map(int, linha.split())) #Pega todos os os inteiros das linhas
            j = list(range(1, 10)) #Gerador de índices 
            for i in range(len(Inteiros)):
                for k in range(len(j)):
                    if Inteiros[i] % j[k] == 0:
                        counter += 1
                if counter == 2: #Caso Divisível
                    Primos.append(f'Line {LineNuber} Colum {i}') #Guarda o numero da linha e a coluna que é o índice.
                    # temp.append(LineNuber)
                    # temp.append(i)
                    qtdPrimo += 1 #Guarda a quantidade de primos na linha
                    counter = 0

                else: # caso que nao é primo
                    counter = 0
                    Primos = [] 
                    qtdPrimo = 0
                    break           

                if qtdPrimo == len(Inteiros):
                    Primos = f'Linha {LineNuber + 1}'
                    temp.append(Primos)
                    counter = 0
                    Primos = []
                    break
        LineNuber += 1
    return temp
#PROGRAMA PRINCIPAL
Arquivo = input('Informe o nome do Arquivo: ')#.txt
RelacaoDePrimos = AnalisaDoc(Arquivo)
for n in range(len(RelacaoDePrimos)):
    if RelacaoDePrimos[n] == 'Linha':
        RelacaoDePrimos[n + 1] = int(RelacaoDePrimos[n + 1]) 
    
    if RelacaoDePrimos[n] == 'Colum':
        RelacaoDePrimos[n + 1] = int(RelacaoDePrimos[n + 1])
