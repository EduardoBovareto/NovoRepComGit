# Este Arquivo trata a criptografia com uma determinada palavra e criptografa ela usando ord('string')

def FazCriptografia(Palavra, Nivel): # O nível é o quantos caracteres se pula na relação Unicode
    if Nivel == 'Baixa':
        for indice, letra in enumerate(Palavra):
            print() # Muda a posição de cada letra em 1 unidade em padrao unicode.
    elif Nivel == 'Media':
        for indice, letra in enumerate(Palavra):
            print() # Muda cada posição em 3 unidades em padrao unicode.
    elif Nivel == 'Alta':
        for indice, letra in enumerate(Palavra):
            print() # Trabalha com interio de raiz quadrada do indice do caracter, somando também ao modulo do numero sendo ele impar (3) ou par (2) multiplicado por 2, caso não haja caracter respectivo ou permitido, colocaremos um sorteio de um array com símbolos

Info = input('Digite a palavra que deseja criptografar:')
Modo = input('Defina o nivel de ciptografia: [Baixa], [Media], [Alta]:')
# Cada mível brinca com a posição de caracteres em relação ao unicode
FazCriptografia(Info, Modo)