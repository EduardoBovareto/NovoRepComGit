import struct
#SUBPROGRAMA
#Precisa se do nome do arquivo, a informacao e a codificacao
#C:\Users\WINDOWS\Desktop\JS\Python-temporário\ArquivosBinarios\stringnova.bin
def EscreveEmArquivo(nm, info, code):
    nm = open(nm, 'wb')
    Novo = info.encode(code) #Coloca em blocs de bytes
    #Novo2 = struct.pack(f'{info}', 10)
    nm.write(Novo)
    novo2 = Novo.decode(code) #Pega o bloco de bytes e passa para caracteres
    print(novo2)
#PROGRAMAPRINCIPAL
Nome = input('Informe o nome ou caminho do arquivo: ')
Palavra = input('Digite duas palavras: ')
EscreveEmArquivo(Nome, Palavra, 'utf-8')