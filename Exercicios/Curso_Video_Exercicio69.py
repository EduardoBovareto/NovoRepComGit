idade = count_idade = count_s = count_M = 0
sexo = flag =  ''
print('-'*20)
print('CADASTRO DE PESSOAS\n')
print('-'*20)
while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo:').upper()
    while sexo not in ['M', 'F']: #Controle de regras de dados
        sexo = input('Sexo:').upper()

    count_idade += 1 if idade > 18 else 0 #Pessoas maiores de 18
    count_s += 1 if sexo == 'M' else 0 #Pessoas do sexo M
    count_M +1 if sexo == 'F' and idade < 20 else 0 #Mulheres do sexo F menores que 20 anos

    flag = input('Quer continuar: [S-N]').upper()
    while flag not in ['N', 'S']: #continuar ate digitar a letra certa
        flag = input('Quer continuar: [S-N]').upper()
    
    if flag == 'N':
        break

print('='*10,'FIM DO PROGRAMA','='*12)
print(f'''\n\nNo total foram cadastrados {count_idade} pessoas maior de 18 anos\n
         \nForam cadastrado {count_s} Homens\n
Foram cadastrados {count_M} mulheres com mais de 20 anos''')