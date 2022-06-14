#SUBPROGRAMA
def GeraDict(Produtos, Preco =  None): #Gera um dicionário de produtos de mercadoria
    # Produtos = Produtos.split()
    # Preco = list(map(float, Preco.split()))
    RelacaoProd = dict()
    ArrayProdutos = []
    j = 0
    while j < len(Produtos):
        RelacaoProd[Produtos[j]] = Preco[j] #Cria a key do dict com value
        ArrayProdutos.append(RelacaoProd)
        j += 1
        RelacaoProd = dict()
    return print(ArrayProdutos)

def CriaArquivoLista(): #Lê o arquivo para pegar as informações e "Guardar em dicts."
    with open('Materiais.txt', 'r') as Linhas:
        Details = []
        value = []
        for Linha in Linhas:
           temp = Linha.split()
           for i in range(len(temp)):
                if temp[i].isnumeric():#Caso de Valor no documento txt, preco do produto.
                    value.append(temp[i])
                    continue
                elif len(temp[i]) == len('R$') or len(temp[i]) == len('$'): #Caso de símbolo no texto.
                    continue

                else:
                    Details.append(temp[i])
                    continue
        GeraDict(Details, value)#Coloca informações no disctionary
    return True
#PROGRAMA PRINCIPAL
# Mercadoria = input('Informe os produtos comprados: ')
# Valores = input('Informe os valores dos produtos: ')
CriaArquivoLista()