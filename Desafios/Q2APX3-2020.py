#SUBPROGRAMA
def AnalisaDoc(Dados):
    with open(Dados, 'r') as Linhas:#Abre e Lê o arquivo linha a linha.
        counter = 0
        Primos = []
        qtdPrimo = 0
        LineNuber = 1
        for linha in Linhas:
            Inteiros = list(map(int, linha.split())) #Pega todos os os inteiros das linhas
            j = list(range(1, 10)) #Gerador de índices 
            for i in range(len(Inteiros)):
                for k in range(len(j)):
                    if Inteiros[i] % j[k] == 0:
                        counter += 1
                if counter <= 2: #Caso Divisível
                    Primos.append(LineNuber) #Guarda o numero da linha e a coluna que é o índice.
                    Primos.append(i)
                    qtdPrimo += 1 #Guarda a quantidade de primos na linha
                else: # caso que nao é primo
                    continue 

        if qtdPrimo == len(Inteiros):
            Primos = []
            Primos.appen(LineNuber)
        LineNuber += 1 

#PROGRAMA PRINCIPAL
Arquivo = input('Informe o nome do Arquivo: ')#.txt
AnalisaDoc(Arquivo)