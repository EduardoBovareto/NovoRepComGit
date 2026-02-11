#imports
from random import choice, randint#escolhe um valor aletorio
from time import sleep

def sorteia():#sorteia 5 numeros
    numeros = [randint(-5,10) for i in range(0,5)]#gera numeros

    print(f'Sorteando os {len(numeros)} da lista:', end=' ')
    for i in numeros:
        print(f'{i}',flush=True, end=' ')
        sleep(0.2)
    print('PRONTO!')
    return numeros

def somaPar(lista_analisar):
    l = sum(x for x in lista_analisar if x % 2 == 0)
    sleep(0.5)
    print(f'Somando os valores pares  de {lista_analisar}, temos: {l}')


#Programa Principal
lista = sorteia()
#print(lista)
somaPar(lista)