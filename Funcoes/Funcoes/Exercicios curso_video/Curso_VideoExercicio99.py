from random import randint as rd #fornece valores aleatorios
from time import sleep as sl #sleep da um delay na impressao

def maior(numeros):
    maior = 0
    menor  = 0

    print(f'\n{'-='*30}')
    print('Analisando os valores passados...')
    for numero in numeros:#bloco de logica maior e menor
        if maior == 0 or maior < numero:
            maior = numero

        if menor == 0 or menor > numero:
            menor = numero
        
        print(numero, end=' ' ,flush=True)
        sl(0.2)

    print(f'Foram informados {len(numeros)} numeros ao todo.')
    print(f'O maior valor foi: {maior}')
    print(f'\n{'-='*30}\n\n')  


#Programa principal
for i in range(rd(0,3), rd(0,6)):
    numeros  = [rd(2,20) for i in range(rd(0,8), rd(9,13))]
    #
    maior(numeros)
