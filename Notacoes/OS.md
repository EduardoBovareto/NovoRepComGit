# Module OS
~~~python
import os
open(file = caminho, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None) 


#mode = { 
#    (opcional)

#   'r' = Padrao, ler
#   'w' = escrever apagando o que ja tem
#   'x' = criar arquivo
#   'a' = Escrever anexando no fim
#   '+' = Ler e escrever
#    {'w+','w+b'} = trunca o arquivo
#    {r+,r+b} = abre sem truncar

#    }
closefd == False, arquivo fechado
encondig == Codificação


if mode == 't' and encoding == None:
    locale.getencoding() = 'utf-8'
    #Chamar acima!

buffering = 'armazenamento de dados no disco, velocidade de armazenamento'
    {
        buffering == 0 -> 'grava direto no disco'
        buffering == 1 -> 'buffer de linha, grava quando acha \n'
        buffering > 1 -> 'Defini;'ao do buffer em bytes

    }

if buffering with mode == 'r+' or 'w+':
    [Seu texto] → Buffer de texto (TextIOWrapper) → Buffer binário → SO → Disco

else:
    TextIOWapper.reconfigure(write_through=True))
    [Seu texto] → Buffer binário → SO → Disco

#Quando True, e criado um buffer intermediario para texto  depois para Bytes

#Quando False, apenas escrita direto decodificando

newline = ['\n','\r','\r\n','']
#controla as quebras de linha

if escrita == True:
    if newline == None:
        continue
        #Traduz qualquer um dos tipos para \n e quebra linha

    elif newline == '':
        continue
        #\n e escrito como ele e sem traducao
    
    else:
        continue
        #todos os outros valores tambem serao traduzidos

elif leitura == True:
    if newlline == None:
        continue
        #le  e interpreta todos os valores possiveis menos ''
    
    elif newline in  ['\n','\r','\r\n']:
        continue
        #reconhece no fim da linha apenas o que for selecionado



~~~