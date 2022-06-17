#SUBPROGRAMA
def GerenciaPedidos(Informacao, condition = None):
    Ordem = [] #Sempre será atualizado quando clicado em algum terminou ou se depende de Termino ==  True
    Termino = False #Colocar em relação a um objeto ou button
    Cardapio = {
        0: 'Carne Artesanal',
        1: 'Hamburguer de Frango',
        2: 'Hamburguer Bovino'
#Grupo de informações composta de um cardapio, seja por banco de dados ou pegar da internet.
    }
    if Informacao in Cardapio:
        if condition != None:
            #Aqui usar objetos para colocar visualmente
            pass
    else:
        print('Reestruturar Pedido')
        while Informacao not in Cardapio:
            Informacao = int(input('Informe novamente o índice do pedido'))
#PROGRAMA INCIAL
Pedido = list(input('Digite seu pedido e se deseja ou não alterá-lo:').split())
if 'SIM' in Pedido:
    GerenciaPedidos(int(Pedido[0]), Condicao = input('Informe a condicao'))
    
else:
    GerenciaPedidos(Pedido)
    print('Obrigado pelo Pedido')