count = n = int(input('Escreva um numero para calcular o fatorial:'))
fat = 1
while n != 1:
	fat = n * (n - 1) * fat
	n -= 2
	print(fat)