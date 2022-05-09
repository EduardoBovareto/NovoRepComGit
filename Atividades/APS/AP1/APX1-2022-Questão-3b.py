def VerificaDecimal(valor, p1, p2, p3):
    j = 0
    k = 0
    posicaoErro = 0
    local = 0
    p = 0
    l = p2

    if number.find(".") != -1:
        for i in range(p1):
            if valor[i].isnumeric() == True:
                j = 1

        for p2 in range(p3):
            if valor[p2].isnumeric() == True:
                k = 1
            else:
                if valor.count(".") > 1:
                    posicaoErro = p2
                    local = valor[p2]
                    k = 0

                elif valor[0].isnumeric() == False:
                    for i in valor:
                        if valor[i].isnumeric() == False:
                            p = 0 

        if j == 1 and k == 1:
            print(f"Está correto, {valor} é o tipo float. <class 'float'>")

        if j == 1 and k == 0:
            print(f'Você digitou errado,{valor} não é do tipo float. Na posição {posicaoErro} há o caracter {local}.')

    if number.find(".") == -1:
        for i in range(p3):
            if valor[i].isnumeric() == True:
                j = 1
            if valor[i].isnumeric() == False:
                j = 0

        if valor.count(".") > 1 and k == 0:
            controle = controle + 1
            print(f'Você digitou errado,{valor} não é do tipo float. Na posição {local} há o caracter a mais do que um "{valor[local]}".')

        if j == 0 and k == 0:
            print(f'Você digitou errado,{valor} não é do tipo float. Na posição {local} há o caracter a mais do que um "{valor[local]}".')

number = input()
pos = number.find('.')
pos2 = pos + 1
pos3 = len(number)
VerificaDecimal(number, pos, pos2, pos3)