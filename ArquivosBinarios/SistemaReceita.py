import struct
#SUBPROGRAMA
def PadraoEmPack(Array):
    i = 0
    ResultadoCod = []
    for i in range(len(Array)):
        if type(Array[i]) == type(''):
            ResultadoCod.append(f'{len(Array[i])}s')
            #Nesse caso acima, tem numeros, eu poderia muito bem pegar os valores e separa-los, mas inicialmente vamos tratar tudo com strings
        elif type(Array[i]) == type(0):
            #Como tudo vem como string eu poderia tratar um outra condicao de:
            # "or Array[i].isnumeric(): e isso poderia levar a conversao"
            if len(Array[i]) <= 4:
                ResultadoCod.append('I')
            else:
                ResultadoCod.append('l')
        
        elif type(Array[i]) == type(0.0):
            ResultadoCod.append('f')
    return ResultadoCod
'''
PadraoEmPack é uma funcao que analisa cada dado de um array para decidir dentro de um formato de compactacao de Bytes na funcao pack do modulo struct qual usar e que se tem que passar para em outra funcao muda para Bytes dentro de ProcessaDados
'''
def ProcessaDados(Arquivo, informacoes, code):
    i = 0
    Arquivo = open(Arquivo, 'wb') # Abre o arquivo chamado "DadosP.bin"
    Padrao = PadraoEmPack(informacoes)
    Resultado = []
    Bloco = []
    for i in range(len(informacoes)): #Codificando
        Resultado.append(informacoes[i].encode(code))
    #Da pra juntar os dois laços em 1 só
    while i < len(Resultado):
        Arquivo.write(struct.pack(Padrao[i], Resultado[i]))
        i += 1
    print(Resultado)
    return None
#PROGRAMA PRINCIPAL
NomeArq = input('Nome do arquivo de Armazenamento: ')
Dados = Pessoa = input('Informe o Nome, CPF  e RG: ').split()
#Processar CPF e RG espaço e guardar em uma tupla, armazenar depois, cada ponto e \
ProcessaDados(NomeArq, Dados, 'utf-8')
