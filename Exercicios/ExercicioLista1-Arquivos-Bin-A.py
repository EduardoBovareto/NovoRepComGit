#Esse Programa usa 2 Arquivos binários, o primeiro "tabela.bin" trata-se de uma
#base com precos, nomes e códigos de produtos e que deve ser analisado para dar a conta 
#final. O segundo é a saída da conta final e que também pode ser colocada na saída.
#padrao
''' Inicialmente considerei fazer um "swich-case" com os códigos e depois migrar os dados para um txt ou um binário para o processamento
'''
import struct #Manipulacao de Bytes
def TabelaDados(Codigo): #Arquivo é Tabela.txt
    with open('Tabela.txt', 'r') as Linhas:
        for linha in Linhas:
            Valores = list(map(int, linha.split()))
            Indices = range(1, 6) #Indices dos códigos
            for i in range(len(Indices)):
                if Indices[i] == Codigo:
                    return Codigo, Valores[i], Valores[i + 2]
    
def ProcessaPedido(Np, Qtd): #Np == Numero do Pedido
    Np, pedido, Preco = TabelaDados(Np) #Ele passa o valor que foi passado no input e ao voltar do return ele pega esse mesmo valor
    if Np == 1:
        Preco = Preco * Qtd

    elif Np == 2:
        Preco = Preco * Qtd

    elif Np == 3:
        Preco = Preco * Qtd

    elif Np == 4:
        Preco = Preco * Qtd

    elif Np == 5:
        Preco = Preco * Qtd
    print(f'''O Total a pagar R$: {Preco}, 00\n
    Visto o produto: {pedido}''')
    return None

Pedido = input('Informe o código do seu pedido e a quantidade: ')
#Pedido[0], Quant = Pedido[1] = list(map(int,Pedido.split()))
Pedido = list(map(int,Pedido.split()))
Quant = Pedido[1]
Pedido = Pedido[0]
ProcessaPedido(Pedido, Quant)
#Falta só emitir em um arquivo binario tbm