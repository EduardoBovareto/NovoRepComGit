Nome = 'CursoEmVideo' #String inicial- caderia de caracteres
'''
Cada um das letras do {Nome} tem um indice sequencial de identificação 0-11

C u r s o E m V i d e o
0 1 2 3 4 5 6 7 8 9 10 11
'''
print(f' {Nome[9]}') #imprime uma letra
print(f'{Nome[9:12]}') #imprime uma sequencia de letras
print(f'{Nome[3:12:2]}') #Imprime uma sequencia de caracteres pulando de 2 em 2
#ao pular, le imprime sempre n-1 do valor que vai pular, ele pula 2 e mostra o que contou 2, ou seja deixou de mostrar só 1
print(f'{Nome[:5]}') #sempre começa do caracter 0 quando se assume essa configuração
print(f'{Nome[10:]}')

print(f'{len(Nome)} Caracteres') #tamanho da string
print(f'{Nome.count('o')} letras o') #contagem de quantas letras o tem
print(f'{Nome.count('o',0,12)} letras o') #conta dentro de um fatiamento, quantidade
print(f'Video começa na posição: {Nome.find('Video')}') #procura o caracter que foi colocado como argumento e diz quantas vezes ele encontrou e a posição que o arguento começa

#find pode retornar -1, que é quando nao existe aquela string la

print(f' "Curso" in Nome: {'Curso' in Nome}')
#forma de verificação de existencias através do in

print(f'{Nome.find('Novo')}, Existe "Novo" in Nome: {'Novo' in Nome}')

print(f'{Nome.replace('Curso', 'Urso')}')

Nome2 = '  Curso Em Video   '
print(f'{Nome2.title()}')
print(f'{Nome2.capitalize()}')
print(f'{Nome2} com sespaços, {Nome2.strip()}Sem espaço')

print(f'{Nome2.split()}')
print(f'{'_'.join(Nome)}')
print(f'{Nome[:-1]}')