#SUBPROGRAMA
#Precisa se do nome do arquivo, a informacao e a codificacao
#C:\Users\WINDOWS\Desktop\JS\Python-temporário\ArquivosBinarios\stringnova.bin
def EscreveEmArquivo(nm, info, code):
    nm = open(nm, 'w')

    pass
#PROGRAMAPRINCIPAL
Nome = input('Informe o nome ou caminho do arquivo: ')
Palavra = input('Digite duas palavras: ')
Palavra = Palavra.split()
EscreveEmArquivo(Nome, Palavra, 'utf-8')