import pickle
#SUBPROGRAMA
def CriaDict(Arquivo, LMerc):
    i = 0
    for i in range(1, len(LMerc), 2):
        LMerc[i] = int(LMerc[i]) #Conversão para inteiro        
    Arquivo = open(Arquivo, 'wb')
    while i < len(LMerc):
        Binario = pickle.dumps(LMerc[i])
        print('{}\n'.format(Binario))
        pickle.dump(Binario, Arquivo)
        i += 1
    Arquivo.close()
#PROGRAMA PRINCIPAL
nome = input('Informe um nome de arquivo existente')#.txt
Mercadorias = input('Informe os produtos que deseja e a quantidade').split()
CriaDict(nome, Mercadorias)

