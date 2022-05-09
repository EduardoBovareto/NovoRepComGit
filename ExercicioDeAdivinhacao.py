''' Ideia a se implementar futuramente:
    Da para colocar um counter que a medida que o usuário erra e chega a um numero de erros, se da uma dica
    automaticamente sobre o numero.
'''
from random import randint # Módulo de valores aleatórios gerados pelo PC
valorAleatorio = randint(0, 5) # Valor aleatório
ValorDigitado = int(input('Tente adivinhar o valor que pensei:'))
if valorAleatorio == ValorDigitado:
    print(f'Parabéns, você acertou o número! foi o número {valorAleatorio}')
else:
    print(f'Era o {valorAleatorio}, Você errou tente novamente!')
