import datetime as dt
# import ManipulaArquivo as mp
''' Manipula arquivo de texto de clientes e gera data de registro'''
#SUBPROGRAMA - > Arquivo_BaseData\Base.txt
def processa_Arquivo(Arq, m = None): #Irá pegar todos os valores e somar
    Arq = 'Arquivo_BaseData\\' + Arq
    if '.txt' not in Arq:
        Arq += '.txt'
    with open(Arq, 'r+') as Linhas:
        total = 0 
        for linha in Linhas:
            if linha == '\n':
                break

            valor = linha.split()#Pega cada parte da linha e guarda
            for i in range(len(valor)):
                if '.' in valor[i] and valor[i][0].isnumeric(): #Verifica se é um valor mesmo
                    valor[i] = float(valor[i])
                    total += valor[i]
                else:
                    continue
        Linhas.write(f'\nValor correspondente ao total vendido na empresa: {str(total)}\n')
        Rdate = (dt.datetime.now())
        Rdate = Rdate.strftime('%d/%m/%y %H:%M') 
        '''
        Formatacao de data, não precisa chamar denovod dt.datetime... pois o tipo ja  é datetime, o que resta é só conversao
        '''
        Linhas.write(f'Data de Registro: {Rdate}')
        print('The total amount processed was: R${}'.format(total))
        total = 0
        return None
    '''Duas coisas a tratar: 1 é verficar e colocar .txt no nome do arquivo para caso de
        erro, outra é retirar a repetiçao de escrita do valor total!'''

def acha_nome(name, Arq):
    valor_vendido = 0
    Arq = 'Arquivo_BaseData\\' + Arq
    if '.txt' not in Arq:
        Arq += '.txt'
    with open(Arq, 'r+') as Linhas:
        total = 0 
        for linha in Linhas:
            if linha == '\n':
                break

            valor = linha.split()#Pega cada parte da linha e guarda
            for infos in range(len(valor)):
                if name == valor[infos]:
                    temp = float(valor[6])
                    valor_vendido += temp

        Linhas.write(f'\nValor total vendido pelo {name} é: {str(valor_vendido)}\n')
        data_atualizada = dt.datetime.now()
        data_atualizada = data_atualizada.strftime('%d/%m/%y %H:%M') 
        Linhas.write(f'Data de Registro: {data_atualizada}')
        print('The total amount processed was: R${}'.format(valor_vendido))
    return None
#PROGRAMA PRINCIPAL
name_arq = input('Write the name of the file: ')
# processa_Arquivo(name_arq)
acha_nome('Pablo', name_arq)
