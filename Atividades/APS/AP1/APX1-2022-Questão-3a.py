
def VerificaDecimal(valor, p1, p2, p3):
    j = 0
    k = 0
    l = p2
    if number.find(".") != -1:
        for i in range(p1):
            if valor[i].isnumeric() == True:
                j = 1

        for p2 in range(p3):
            if valor[l].isnumeric() == True:
                k = 1
        if j and k == 1:
            print(f"Está correto, {valor} é o tipo float. <class 'float'>")
        else:
            print(f'você digitou errado, {valor}  não é do tipo float')

def verificaNumeroSemPonto(valor, p3):
    if number.find(".") == -1:
        for i in range(p3):
            if valor[i].isnumeric() == True:
                j = 1
            if valor[i].isnumeric() == False:
                j = 0
                # print(f'você digitou errado, {valor}  não é do tipo float')
        # if len(valor) == valor[0]:  # caso de uma posição emitida
        #     print('Está correto, o valor pode ser uma valor float')

        if j == 1:
            print(f"Está correto, {valor} é o tipo float. <class 'float'>")

        else:
            print(f'você digitou errado, {valor}  não é do tipo float')
number = input() 
pos = number.find('.')
pos2 = pos + 1
pos3 = len(number)

if number.find(".") != -1:
    VerificaDecimal(number, pos, pos2, pos3)
if number.find(".") == -1:
    verificaNumeroSemPonto(number, pos3)
