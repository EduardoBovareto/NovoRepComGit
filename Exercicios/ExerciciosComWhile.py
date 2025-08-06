# Exercicios com estrutura while 

i = j = 0 
while i == 0:
	print('''
		
		[1]Cadastrar Nome
		[2]Informar Salario
		[3] Informar planejamento de gastos
		[4] Abortar Menu
		''')
	j = int(input(''))
	if j == 1:
		nome = input('Nome de empregado: ')
	elif j == 2:
		salario = float(input('Informe seu salario total: '))
	elif j == 3:
		gastos_mes = float(input('Realizou algum gasto: '))
	elif j == 4:
		i += 1
