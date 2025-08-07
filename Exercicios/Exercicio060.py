count = n = int(input('Escreva um numero para calcular o fatorial:'))
fat = 1
p = True
while  p == True:
	if n == 1 or n == 0:
		break
	fat = n * (n - 1) * fat
	n -= 2
print(f'O valor de {count}! = {fat}')