import datetime
def processa_coment(Arq, j):
    Arq = open(Arq, 'w') #DadosC.txt
    if Arq and j == 1: #Arquivo aberto e bit sginificativo de representaçao de comentário
        Mensager = input('Informe a mensgame que deseja emitir: ')
        Tempo = datetime.datetime.today()
        Tempo = Tempo.strftime('%d/%m/%Y %H:%M')
        Arq.write(Mensager)
        Arq.write(Tempo)#Error
        Arq.close()
        return None

    else:
        Arq.write((datetime.datetime.today()).strftime('%d/%m/%Y %H:%M'))
        Arq.write(' Error')
        Arq.close()
        return None, print('Não emitiremos uma mensagem')
Arquivo = input('Informe o nome do arquivo: ')
Verificacao = int(input('Quer escrever mesmo: [1]Sim [0] Não '))
processa_coment(Arquivo, Verificacao)