from random import shuffle
#SUBPROGRAMA
def OrdenaComBuble(Numeros):
    fim = len(Numeros)
    inicio = 0
    i = 0
    while fim > 0:
        temp = 0
        i = 0
        while i < fim -1:
            if Numeros[i] > Numeros[i + 1]:
                temp = Numeros[i]
                Numeros[i] = Numeros[i + 1]
                Numeros[i + 1] = temp
            i += 1
        fim -= 1
    return Numeros
'''
Analisa do inicio pro fim diminuindo o fim, sempre te um while dentro do outro, o de dentro trabalha com os indices, o de fora trabalha para diminuir o fim dele, repetir cada parte até que o array acabe.
'''
#PROGRAMA PRINCIPAL
conjunto = list(range(0, 30, 4))
print(conjunto)
shuffle(conjunto) #Desorganiza o conjunto
print('Ordenado: ', OrdenaComBuble(conjunto))