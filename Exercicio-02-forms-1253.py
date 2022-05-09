'''
casos de teste: for 
'''

def cifraJulio(valor): 
                       # Pegar o valor da string e separar cada caracter.
    valor = valor[::2] # Valores de 2 em 2 de acordo com a cifra
    print(valor)
    return None

testes = int(input('Informe a quantidade de testes: '))
i = 0
for i in range(testes):
    letras = []
    letras = input('Digite:').split()
    print(letras)
    print(cifraJulio(letras))
    