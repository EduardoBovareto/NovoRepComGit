#SUBPROGRAMA
def manipula_caminho(Arquivo: str) -> str:
    Ad = 'Funcoes\\'
    #Funcao_Soma.txt
    if Ad not in Arquivo:
        Arquivo = Ad + Arquivo

    if '.txt' not in Arquivo:
        Arquivo += '.txt' 
    return Arquivo

def cria_arquivo(Arq: str, S1: int = 1, S2: int = 1) -> True:
    ''' Cada parametro tem seu type de dados definido por ":tipo, o return da funcao é definido por True"'''
    Arq = manipula_caminho(Arq)
    with open(Arq, 'a') as Linhas:
        if Linhas.writable():
            S = S1 + S2
            Linhas.write(f'A soma resultante dos indices e: {str(S)}')
    return True

    
#PROGRAMA PRINCIPAL
cria_arquivo('Funcao_Soma.txt', 45, 67)
