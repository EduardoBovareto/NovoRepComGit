# AD2-2 16/05 2022 Eduardo Bovareto Matrícula:21213050280
import struct
Arquivo = input('Digite o nome do Arquivo: ') # Sempre será casrtoes.bin
Arquivo += '.bin'
cartao = input('Escreva o nome da sua Bandeira: ') # Informa o cartao usado
temp = 0
informacoes = open('codigo.txt', 'w') # Abre o arquivo a ser codificado
Bandeiras = ['Visa', 'Mastercard ', 'Diners ', 'Elo ']
listas = []
codigo = []
p = v = m = e = d = 0
try:
    for i in Bandeiras:
        if i == 'Visa':
            listas = [cartao]
            temp = float('123.90')
            v = 1
            break
        
        elif i == 'Mastercad':
            listas = cartao
            temp = float('245.45')
            m = 1
            break
        
        elif i == 'Diners':
            listas = i
            temp = float('367')
            d = 1
            break
        
        elif i == 'Elo':
            listas = i
            temp = float('532')
            e = 1
            break

        elif i not in Bandeiras:
            p = 1
            break
        
    for infos in Bandeiras:
        informacoes.write(infos)
    informacoes.close()

    with open(Arquivo,'wb') as Arquivo:
        # listas[0] = (listas[0] + ' ').encode("utf-8")
        # listas[1] = listas[1].encode('utf-8')
        # codigo.append(listas[0])
        # codigo.append(listas[1])
        inteiros = []
        for i in listas:
            for j in i:
                inteiros.append(ord(j))

        for i in inteiros:
            Arquivo.write(struct.pack('i', i))
            Arquivo.write(struct.pack('d', temp))
        
        if v == 1:
            print('')
            
        elif m == 1:
            m = 1
        
        elif d == 1: 
            d = 1
        
        elif e == 1:
            e = 1

except:
    if p == 1:
        print('Cartão não encontrado')