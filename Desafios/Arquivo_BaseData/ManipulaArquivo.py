import datetime as dt
# import ManipulaArquivo as mp
''' Manipula arquivo de texto de clientes e gera data de registro'''
#SUBPROGRAMA - > Arquivo_BaseData\Base.txt
def manipula_arq(Arq):
    Arq =  'Arquivo_BaseData\\' + Arq
    if '.txt' not in Arq:
        Arq += '.txt'
    return True, Arq

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

def acha_nome_soma_valores(name, Arq):
    valor_vendido = 0
    Arq = 'Arquivo_BaseData\\' + Arq
    if '.txt' not in Arq:
        Arq += '.txt'
    with open(Arq, 'r+') as Linhas:
        Novo = Linhas.readlines(3)
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
    return name

def acha_nome(Arq, name):
    with open(Arq, 'r') as L:
        for i in range(len(L)):
            info = L.readlines(i)
            pass
    return name, #position

def value_edit(Arq, value, name):
    ''' Muda o valor da venda feita'''
    _, Arq = manipula_arq(Arq)
    acha_nome(Arq, name)

    with open(Arq, 'r+') as valores:
        # name = acha_nome(Arq, name)
        for v in valores:
            lista = v.split()
            i = 0
            while i < (len(lista) - 1):
                if lista[i] == value:
                    lista[i] = str(value)
                    break
                i += 1
                #finalizacao de codigo para achar nomes e posicoes e mudar valores de vendas
#Criptografia de código de vendedor= importar funcao pronta por mim
#PROGRAMA PRINCIPAL
name_arq = input('Write the name of the file: ')
# processa_Arquivo(name_arq)
# acha_nome_soma_valores('Pablo', name_arq)
number = int(input('Informe o dado para mudança: '))
nome_reference = input('Digite o dono da venda: ')
value_edit(name_arq, number, nome_reference) #Depois colocar mais valores