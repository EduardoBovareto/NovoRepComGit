import nltk 
#Modulo de analise da lingua
from nltk.corpus import names, abc #Leitura de nomes na senha,#Leitura de palavras na senha
nltk.download('abc')
nltk.download('names')

Banco_abc = set(abc.words()) #Puxa as palavras do banco
Names = set(names.words('male.txt')) #puxa os nomes
female_names = set(names.words('female.txt'))
Names = Names.union(female_names) #faz a uniao em um so dicionario dos nomes

def Trata_word(palavra):
    pass

def Analisa_pedido(pw):
    if str in pw:
        temp = password_finaly =  []
        try:
            temp = list(map(int,pw)) #converte caso haja so numero em lista separada
            password_finaly.append(temp) #retorno para manipulacao da senha, e tamanho

        except ValueError:
            qtd = len(pw) #tamanho para parametro
            count = 0
            palavra = ''

            for possible in pw: #analise das palavras
                if pw[possible] in abc.words(): #verifica letra
                    palavra += pw[possible] #separa possivel nome
                    count += 1

                    if count >= 3 or count >= 4:
                        if palavra in names.words():
                            cut = pw.index(palavra) #procura nome dentro
                            temp.append(pw[cut:len(palavra)]) #tamanho do nome ou string morta

                        else:
                            temp.append(pw[cut:len(palavra)])
                            palavra = ''
                            count = 0
                            
                else: #caso de numero ou especial
                    password_finaly.append(pw[possible])
            

def Gera_senha(): #analisara cada caracter
    pass

password = input('Descreva a senha desejada! \n') #guarda senha a ser analisada
print('Sera gerado mais senhas exemplo que podem ser adotadas')
Analisa_pedido(password)

#recebe os caracteres enviados e gera mais 6 senhas, 3 aleatorias e 3 dificeis
# 8 a 16 caracteres
# inicialmente vai gerar qualquer tipo escrito sem forca