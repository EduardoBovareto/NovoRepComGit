import datetime as dt
''' Manipula arquivo de texto de clientes e gera data de registro'''
#SUBPROGRAMA
def processa_Arquivo(Arq, m): #Irá pegar todos os valores e somar
     with open(Arq, 'r+') as Linhas:
        total = 0 
        for linha in Linhas:
            valor = list(map(str, linha))#Pega cada parte da linha e guarda
            for i in range(len(valor)):
                if '.' in valor[i] and valor[i][0].isnumeric(): #Verifica se é um valor mesmo
                    valor[i] = float(valor[i])
                    total += valor[i]
                else:
                    continue
        print('The total amount processed was: {}'.format(total))
        return None

def acha_nome():
    pass

#PROGRAMA PRINCIPAL
name_arq = input('Write the name of the file: ') 
''' 
Codigo abaixo se trata de uma funcao de arquivo s que dependendo da operacao se chama uma outra nova funcao definida dentro da propria funcao:
def arquivos():
    def chama_valor()
    def acha()
Sendo assim, cada uma seria chamada de acordo com a operacao

# operation = int(input('Write the operation that want calculate: '))
# models = [1, 2,] #Achar alguem e informar as vendas dele
# counter = 0 
# while operation not in models:
#     print('Please! write a need information for processing: ')
#     operation = int(input('Report your operation: '))
#     counter += 0
#     if counter == 5:
#         print('We inform that the was program close ')
#         break
# else:
#     pass
#     # processa_arquivo(name_arq, operation)
'''