
def VerificaDecimaltaxado(valor, p1, p2, p3):
    j = 0
    k = 0
    l = p2
    if valor.find(".") != -1:
        for i in range(p1):
            if valor[i].isnumeric() == True:
                j = 1

        for p2 in range(p3):
            if valor[l].isnumeric() == True:
                k = 1
        if j and k == 1:
            print(f"Está correto, {valor} é o tipo float. <class 'float'>")
            number = float(valor)
            taxa = float(input(''))
            taxado = number * taxa
            print(f"O valor {taxado} USD com a taxa {taxa} vai para {taxado} BRL")
            return number      
        else:
            print(f'você digitou errado, {valor}  não é do tipo float')

    if valor.find(".") == -1:
        for i in range(p3):
            if valor[i].isnumeric() == True:
                j = 1
                number = float(valor)
                taxa = float(input(''))
                taxado = number * taxa
                print(f"Está correto, {valor} é o tipo float. <class 'float'>")
                print(f"O valor {taxado} USD com a taxa {taxa} vai para {taxado} BRL")
            else:
                j = 0  
        
number = input()
pos = number.find('.')
pos2 = pos + 1
pos3 = len(number)
VerificaDecimaltaxado(number, pos, pos2, pos3)

