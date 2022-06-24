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
    temp = '' 
    for i in Ordenacao:
        temp += str(i)
    Ordenacao = temp
    return Ordenacao

def ProcessaNumero(Valores):
    temp = ''
    Pares = []
    ordenacao = 0
    counter = contador = 1
    
    for letras in Valores:
        if letras.isnumeric():
            continue
        else:
            print(f'A entrada {Valores} não está do formato solicitado')
            return None

    Valores = list(map(int, Valores))
    ordenacao = Valores

    for i in range(len(Valores)):
        if Valores[i] in range(0, 10):
            temp += str(Valores[i])
        if Valores[i] % 2 == 0:
            Pares.append(Valores[i])

    for numero in (Valores):
        if int(numero) == counter:
            contador += 1
        counter += 1
        
    ValorOrd = ListaOrder(ordenacao)

    if temp == ValorOrd and contador == 1:
        # Pares2 = ListaOrder(Pares)
        print(f'''Na entrada {temp} não há elementos com valores iguais as suas posições
        A entrada {temp} está ordenada
        A lista dos elementos pares de {temp} em ordem de aparição é {list(map(str, Pares))}''')

    elif  counter != 0 and temp != ValorOrd:
        print(f''' A entrada {temp} há {contador - 1} elemento com valor  igual a sua posição
        A entrada {temp}  não está ordenada ''')

    elif temp == ValorOrd and contador > 1:
        print(f'''Na entrada {temp} há {contador - 1} elemento com valor  igual a sua posição.
        A entrada {temp} está ordenada''')
    return None
Valor = input()
ProcessaNumero(Valor)