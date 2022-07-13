class Cardapio: #Molde para criar o cardapio, uma estrututra de dados que define a estrutura de um cardapio por exemplo. 
    def __init__(self, pedidos):
        #Propriedades do cardápio, pedidos que constitue o mesmo.
        self.Pedidos = pedidos
        #Tenho uma formula que cria um cardapio e com atributos de pedidos

    def processa_pedido(self, Numero): #Processa o pedido na unidade grafica
        pass

    def adicionar(self): #Adiciona um novo item
        self.Pedidos['P5'] = input('Digite o novo pedido ').split(',') #O atributo Pedidos é modificado com uma nova informacao e preço
        self.Pedidos['P5'][1] = float(self.Pedidos['P5'][1]) #Conversão de Preço
        return Cardapio(self.Pedidos) #retorna um novo objeto modificado

Info = { #Organização de informações de cardapio
    'P1': ['Artesanal', 30],
    'P2': ['Suino', 26.90],
    'P3': ['Carne Assada', 32.50],
    'P4': ['Normal', 22.10]
    }
MrSilva = Cardapio(Info) #Cria o cardápio do MrSilva
# print(MrSilva.Pedidos) #Acessando o atributo do objeto
MrSilva = MrSilva.adicionar() #Adiciona um novo item aos pedidos
# print(MrSilva.Pedidos)
