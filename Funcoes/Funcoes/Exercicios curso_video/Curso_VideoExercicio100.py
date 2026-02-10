#imports
from random import choice, randint#escolhe um valor aletorio

def sorteia():#sorteia 5 numeros
    numeros = [randint(-5,10) for i in range(0,5)]
    return numeros

def somaPar(lista_analisar):
    l = sum(x for x in lista_analisar if x % 2 == 0)
    print(l)

#Programa Principal
lista = sorteia()
print(lista)
somaPar(lista)