# AD2-2 16/05 2022 Eduardo Bovareto Matrícula:21213050280
import struct
Arquivo = input('Digite o nome do Arquivo: ') # Sempre será casrtoes.bin
Arquivo += '.bin'
cartao = input('Escreva o nome da sua Bandeira: ') # Informa o cartao usado
temp = ' '
informacoes = open('codigo.txt', 'w') # Abre o arquivo a ser codificado
Bandeiras = ['Visa', 'Mastercard ', 'Diners ', 'Elo ']
listas = []
codigo = []
p = 0
try:
    for i in Bandeiras:
        if i == 'Visa':
            listas = [cartao, '123.90'] 
            break
        
        elif i == 'Mastercad':
            listas = [cartao, '245.45']
            break
        
        elif i == 'Diners':
            listas = [i, '367']
            break
        
        elif i == 'Elo':
            listas = [i, '532']
            break

        elif i not in Bandeiras:
            p = 1
            break
        
    for infos in Bandeiras:
        informacoes.write(infos)
    informacoes.close()

    with open(Arquivo,'r+b') as Arquivo:
        # listas[0] = (listas[0] + ' ').encode("utf-8")
        # listas[1] = listas[1].encode('utf-8')
        # codigo.append(listas[0])
        # codigo.append(listas[1])
        inteiros = []
        for i in listas:
            for j in i:
                inteiros.append(ord(j))
        temp = bin(ord(temp))

        for i in inteiros:
            Arquivo.write(struct.pack('i', i))
            if i == inteiros[4]:
                Arquivo.write(temp)
except:
    if p == 1:
        print('Cartão não encontrado')