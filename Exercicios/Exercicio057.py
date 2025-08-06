sexo = ['M', 'F']
r = input('Digite um sexo: ').upper()
while r not in sexo:
	print('Fora do esperado! Digite M ou F')
	r = input('Escreva um sexo novamente: ').upper()
print('Obrigado!')