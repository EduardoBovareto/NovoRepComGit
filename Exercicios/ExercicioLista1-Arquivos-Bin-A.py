#Esse Programa usa 2 Arquivos binários, o primeiro "tabela.bin" trata-se de uma
#base com precos, nomes e códigos de produtos e que deve ser analisado para dar a conta 
#final. O segundo é a saída da conta final e que também pode ser colocada na saída.
#padrao
''' Inicialmente considerei fazer um "swich-case" com os códigos e depois migrar os dados para um txt ou um binário para o processamento
'''
import struct #Manipulacao de Bytes    
def ProcessaPedido(Np, Qtd): #Np == Numero do Pedido
    with open('Tabela.txt', 'r') as Linhas:
        for linha in Linhas:
            Valores = linha.split()
            for i in range(len(Valores)):
                if Valores[i].isnumeric():
                    Valores[i] = int(Valores[i])
                elif '.' in Valores[i]:
                    Valores[i] = float(Valores[i])
                else:
                    continue
            if Valores[0] == Np:
                break
    # Np, pedido, Preco = TabelaDados(Np) #Ele passa o valor que foi passado no input e ao voltar do return ele pega esse mesmo valor
        if Np == 1:
            Preco = Valores[2] * Qtd

        elif Np == 2:
            Preco = Valores[2] * Qtd

        elif Np == 3:
            Preco = Valores[2] * Qtd

        elif Np == 4:
            Preco = Valores[2] * Qtd

        elif Np == 5:
            Preco = Valores[2] * Qtd
    print(f'O Total a pagar R$: {Preco}, 00')
    return None

Pedido = input('Informe o código do seu pedido e a quantidade: ')
#Pedido[0], Quant = Pedido[1] = list(map(int,Pedido.split()))
Pedido = list(map(int,Pedido.split()))
Quant = Pedido[1]
Pedido = Pedido[0]
ProcessaPedido(Pedido, Quant)
#Falta só emitir em um arquivo binario tbm