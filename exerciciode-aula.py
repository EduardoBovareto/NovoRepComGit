'''
Algorítimo Letra D dos execícios da Aula 03, calcula o mod por 5 de números
entre x e y,que foram informados pelo usuário e classifica-os se tem o resultado
2 ou 3!
'''
def calculaMod(valor):
    cond = valor % 5
    if cond == 2 or cond == 3:
        print('Valor correto: {} '.format(valor))

x = int(input('Informe um valor:'))
y = int(input('Informe um valor:'))

for x in range(x, y):
    print(calculaMod(x))

    # cond = x % 5
    # if cond == 2 or cond == 3:
    #     print('Valor correto: {} '.format(x))
# Mudar a impressão do none!