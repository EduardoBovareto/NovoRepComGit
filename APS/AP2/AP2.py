# QUESTAO 2

def ProcessaArquivo(Arq, Procurada):
    Identificacao = 0
    CounterDeLinha = 0
    i = 1
    linhasTrue = []
    temp = []

    with open(Arq,'r' ) as Linhas:
        pos = ' '
        
        for linha in Linhas: # Pega a linha de linhas
            temp = linha.split()

            if Procurada in temp:
                for k in range(1, len(temp)):
                    if temp[k] == Procurada:
                        pos =  pos + ' ' + str(k) # Indices de palavras
                        pass
                linhasTrue.append(i) # Linhas onde tem a Palavra Procurada
                pass

        
            else:
                Identificacao += 1 # Identifica a palavra
                if '\n' in linha:
                    CounterDeLinha += 1
            i += 1
            continue
    if pos != ' ':
        print('\nOcorrências da palavra nota no arquivo sambaDeUmaNotaSó.txt:\n')
        pos = pos.split()
        for i in range(len(linhasTrue)):
            print(f'Linha {linhasTrue[i]}, Palavra {int(pos[i]) + 1} nesta linha!')
    elif pos == ' ':
        print(f'\nNão há ocorrências para esta palavra "{Procurada}" ')

NomeDoArquivo = input('Informe o nome do arquivo: ') #sambadeumanotasó
TipoDeArq = input('Informe o tipo de arquivo: ')
Arquivo = NomeDoArquivo + '.' + TipoDeArq
PalavraProcurada = input('Informe a palavra procurada')
ProcessaArquivo(Arquivo, PalavraProcurada)