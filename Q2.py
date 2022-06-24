isNumero = False
isOrdenada = False
cont = 0
qtdElementoValorEPosicaoIguais = 0
lista = []

entrada = input()

valorAnterior = entrada[0]

for caracter in entrada:
    cont += 1

    if caracter == "0":
        isNumero = True
    elif caracter == "1":
        isNumero = True
    elif caracter == "2":
        isNumero = True
    elif caracter == "3":
        isNumero = True
    elif caracter == "4":
        isNumero = True
    elif caracter == "5":
        isNumero = True
    elif caracter == "6":
        isNumero = True
    elif caracter == "7":
        isNumero = True
    elif caracter == "8":
        isNumero = True
    elif caracter == "9":
        isNumero = True
    else:
        isNumero = False
        break


    if caracter == str(cont):                #letra b
        qtdElementoValorEPosicaoIguais += 1


    if caracter >= valorAnterior:      #caracter é o valor atual
        valorAnterior = caracter
        isOrdenada = True
    else:
        isOrdenada = False
        break


    if int(caracter) % 2 == 0:
        lista.append(caracter)


if isNumero == False:
    print(f"A entrada {entrada} não está do formato solicitado")
else:
    entrada = str(entrada)

    if qtdElementoValorEPosicaoIguais > 0:
        print(f"Na entrada {entrada} há {qtdElementoValorEPosicaoIguais} elemento com valor igual a sua posição")
    else:
        print(f"Na entrada {entrada} não há elementos com valores iguais as suas posições")

    if isOrdenada == True:
        print(f"A entrada {entrada} está ordenada")

        if len(lista) > 0:
            print(f"A lista dos elementos pares de {entrada} em ordem de aparição é {lista}")

    else:
        print(f"A entrada {entrada} não está ordenada")



