'''
numero_desejado = usuario
tupla = com valores por extenso
Tupla que contem numeros por extenso de 0 a 20 e o que o usuario digitar tem que condizer com o que esta por extenso
'''
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito','nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um numero entre 0 e 20:'))
while n > 20 or n < 0:
    n = int(input('Tente Novamente! Digite um numero entre 0 e 20:'))
print(f'Você digitou o numero: {numeros[n]}')
# cada numero digitado representa diretamente a casa da tupla

