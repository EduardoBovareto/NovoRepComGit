# Este Arquivo trata a criptografia com uma determinada palavra e criptografa ela usando ord('string')
import math
import random as rd
def criptografia(Palavra, Nivel): # O nível é o quantos caracteres se pula na relação Unicode
    if Nivel == 'Baixa':
        for indice, letra in enumerate(Palavra):
            Palavra[indice] = chr(ord(letra) + 2) # Pega a próxima posicao alfebética
            #chr converte um inteiro em string com base em codificação Unicode, dentro do padrao
        return None, print(f'A palavra codificada é: {Palavra}')# Muda a posição de cada letra em 1 unidade em padrao unicode.

    elif Nivel == 'Media':
        for indice, letra in enumerate(Palavra):
            Palavra[indice] = chr(ord(letra) * 3 + 2)
        return None, print(f'A palavra codificada é: {Palavra}') # Muda cada posição em 3 vezes adcionado a 2 em padrao unicode.

    elif Nivel == 'Alta':
        for indice, letra in enumerate(Palavra):
            rq = math.sqrt(ord(letra) * 5)
            temp = rd.randrange(0, rd.randint(-5, 200)) * 3
            Palavra[indice] = chr(rq + temp)
        return None, print(f'A palavra codificada é: {Palavra} ')
        
Info = input('Digite a palavra: ')
Modo = input('Defina o nivel de ciptografia: [Baixa], [Media], [Alta]:')
while len(Info) < 3: #Assegura qeu palavras menores nao entrem
    print('Favor Emitir uma nova palavra, e MAIOR!')
    Info = input('Digite a Palavras')
criptografia(Info, Modo)