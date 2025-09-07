import nltk
def Analisa_pedido(pw):
    if str in pw:
        temp = []
        try:
            temp = list(map(int,pw)) #converte caso haja so numero
            return temp, len(temp) #retorno para manipulacao da senha, e tamanho

        except ValueError:
            count = len(pw) #tamanho para parametro

def Gera_senha(): #analisara cada caracter
    pass

password = input('Descreva a senha desejada! \n').split() #guarda senha a ser analisada
print('Sera gerado mais senhas exemplo que podem ser adotadas')
Analisa_pedido(password)

#recebe os caracteres enviados e gera mais 6 senhas, 3 aleatorias e 3 dificeis
# 8 a 16 caracteres
# inicialmente vai gerar qualquer tipo escrito sem forca