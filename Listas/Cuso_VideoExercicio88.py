from random import randint as rd
from time import sleep as sl

print(f'\n{' Mega Sena ':=^40}\n')
print(f'{'='*40}\n')
numero_jogos = int(input('Descreva a quantidade de jogos que serao jogados: '))

for rodada in range(1, numero_jogos + 1):
    print(f'Jogo {rodada} {[rd(1,60) for i in range(0,6)]}')
    sl(1) #time.sleep(2) aguarda 2 segundos

