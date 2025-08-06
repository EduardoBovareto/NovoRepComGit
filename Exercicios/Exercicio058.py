from random import randint
escolhido = randint(0, 10)
counter = 1
r = None

while r != escolhido:
	r = int(input('Adivinhe um numero de 0 a 10: '))
	if r > 10 or r < 0:
		print('\nFAVOR INFORMAR ENTRE 0 E 10\n')
	else:
		if r != escolhido:
			print('Você errou! Tente novamente!')
			counter += 1

		if counter > 3:
			if r > escolhido:
				print('DICA! Esta antes desse numero!')

			if r < escolhido:
				print('DICA! esta depois desse numero!')
print(f'Você acertou!, Total de tentativas: {counter}')
