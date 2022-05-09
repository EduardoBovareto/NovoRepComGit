# Exemplo de lista de compras
# Uma ideia é futuramente gerar uma matriz com os produtos e preços
def OrganizaLista(Nicho): # Função que oeganiza os produtos em dictionary
    Produtos = {} # Cria o dicionário
    Temp = []
  
    for i in range(1,len(Nicho), 2): # For para pegar os produtos dentro de cada quantidade
        j = int(Nicho[i]) # Quantidades de cada nicho de produtos
        for i in range(j):
            Materiais = input('Digite os produtos da lista:') # Array de Produtos
            Temp.append(Materiais)
        for i in range(0, len(Nicho), 2): #Pega os nichos da lista de compra
            Produtos[Nicho[i]] = Temp[::] # Coloca os nichos como chaves do dict
            # Esta pegando duas vezes o mesmo array ['sal', 'fejao']
        temp = []
NichoDeProdutos = input('Digite os tipos de produtos e a quantidade:').split() 
# Obtém o nicho de cada produto para as keys
#Coleta de produtos em array
OrganizaLista(NichoDeProdutos)
