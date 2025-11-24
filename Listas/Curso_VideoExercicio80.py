lista_ordenada = []
temp =  i = 0
counter = 7

while True:
    temp = int(input('Write a value: ')) #recebe um numnero

    if len(lista_ordenada) == 0:
#Quando a lista esta vazia, apenas e adicionado o valor!
        lista_ordenada.append(temp)
        counter -= 1

    elif len(lista_ordenada) == 1:
#Quando ja se tem um valor dentro da lista, apenas e analisado quem e o maior e add
        if lista_ordenada[0] > temp:
            lista_ordenada.insert(0,temp)
            counter -= 1

        else:#caso do valor digitado ser maior que o da lista
            lista_ordenada.append(temp)
            counter -= 1
    else:
        i = len(lista_ordenada) - 1
#Caso o array tenha um len maior que 1 se percorrer o array para analisar!
        while i > -1:
            if lista_ordenada[i] > temp and i == 0:
                lista_ordenada.insert(i, temp)
                counter -= 1
                i = -1
#Quando tem 2 valores na lsta e a analise parou no primeiro termo da lista
            elif lista_ordenada[i] > temp:
                i -= 1
#Quando esta no meio da lista analisando e o que digitei nao e maior
            else:
                lista_ordenada.insert(i + 1,temp)
                counter -= 1
                i = -1
#caso onde nao chegou no primeiro termo e temp e maior que o termo de meio de lista
    if counter == 0:#condicao de parada
        break
print(lista_ordenada)