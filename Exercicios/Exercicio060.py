n = int(input('Escreva um numero para calcular o fatorial:'))
fat = 1
count = 0
p = True
while  p == True:
	if n == 1:
		p = False
	fat = n * (n - 1) * fat
	n -= 2
print(f'O valor de {n}! = {fat}')