import random
#Leitura de nomes de um input poder ser atravẽs de uma planilha tambem
n = random.randint(1,6) #retorna valores inteiros do 'randint' criados aleatoriamente 
nomes = input(f'Escreva {n} nomes para escolha da ordem: ')
nomes = nomes.split(' ')
print(f' O escolhido foi o: {random.choice(nomes)}')
print(f' O escolhido foi o: {random.shuffle(nomes)}')
