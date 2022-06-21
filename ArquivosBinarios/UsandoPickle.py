import pickle #Trabalha com conversao de numeros inteiros para binario
from random import randint #Trabalha com valores inteiros aleatórios
numero = randint(0, 20)
print(numero)
N = pickle.dumps(numero) #Converte o valor integer em binário
print('O valor {} em binário é {} '.format(numero,N))
print(f' o valor : {N} em integer é : {pickle.loads(N)}') #pickle.loads converte de binário em decimal-Integer
Novo  = 'e'
print(f'{pickle.dumps(Novo)}') #Podemos fazer com strings também
'''
pickle.dump() escreve um objeto em um arquivo == pickle.dump(objeto, arquivo)
pickle.load() Lê um objeto de um arquivo binário e lê e converte
'''