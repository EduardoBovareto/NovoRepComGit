def ListaOrder(Ordenacao):
    n = len(Ordenacao)
    for j in range(n -1): 
        menor = j
        for i in range(j, n): 
            if Ordenacao[i] < Ordenacao[menor]: 
                menor = i
        if Ordenacao[j] > Ordenacao[menor]:
            temp = Ordenacao[menor]
            Ordenacao[j] = Ordenacao[i]
            Ordenacao[i] = temp
    return Ordenacao

def ProcessaNumero(Valores):
    temp = ''
    Pares = []
    counter = ordenacao = 0
    Valores = list(map(int, Valores))
    ordenacao = Valores
    if ' ' in Valores:
        print(f'A entrada {Valores} não está do formato solicitado')
        return None

    else:
        for i in range(len(Valores)):
            if Valores[i] in range(0, 10):
                temp += str(Valores[i])
            if Valores[i] % 2 == 0:
                Pares.append(Valores[i])
        Valores = temp

        for numero, i in enumerate(Valores, 1):
            if int(i) == numero:
                counter += 1
        ValorOrd = ListaOrder(ordenacao)

        if Valores == ListaOrder(ordenacao) and counter == 0:
            Pares2 = ListaOrder(Pares)
            print(f'''Na entrada {temp} não há elementos com valores iguais as suas posições
            A entrada {temp} está ordenada
            A lista dos elementos pares de {Pares} em ordem de aparição é {list(map(str, Pares2))}''')

        elif  counter != 0 and Valores != ValorOrd:
            print(f''' A entrada {temp} há {counter} elemento com valor  igual a sua posição
            A entrada {temp}  não está ordenada ''')

    return counter, Valores, ordenacao, Pares
Valor = input()
ProcessaNumero(Valor)