n1 = float(input('VALOR 1: '))
n2 = float(input('VALOR 2: '))
control = 0
print('''
		Escolha:
			[0] Ver Menu Novamente
			[1] somar
			[2] multiplicar
			[3]	maior
			[4] novos numeros
			[5] sair do programa
		\n
		''')

while control != 5:


	control = int(input(':'))
	if control > 5 or control < 0:
		print('FAVOR RESPEITAR O MENU') 

	if control == 0:
		print('''
		Escolha:
			[0] Ver Menu Novamente
			[1] somar
			[2] multiplicar
			[3]	maior
			[4] novos numeros
			[5] sair do programa
		\n
		''')

	if control == 1:
		print(f'Soma: {n1 + n2}')

	elif control == 2:
		print(f'Multiplicacao: {n1 * n2}')

	elif control == 3:
		if n1 > n2:
			print(f'Maior: {n1}')
		else:
			print(f'Maior:{n2}')

	elif control == 4:
		n1 = int(input('Novo numero 1:'))
		n2 = int(input('NOvo numero 2: '))

print('Programa finalizado!')
