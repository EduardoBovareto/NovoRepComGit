sexo = ['M', 'F']
r = input('Digite um sexo: ').upper().strip()[0]
#Se o cara digitar Masculino será pego o M
#strip() retira os espaços que não são necessários e coloca em letra maiúscula
while r not in sexo:
	print('Fora do esperado! Digite M ou F')
	r = input('Escreva um sexo novamente: ').upper()
print('Obrigado!')