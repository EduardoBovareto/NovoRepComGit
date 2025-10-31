nomes = [] #nomes das pessoas escritas pelo usuario
sexo = [0, 0]#sexo = [M, F] posição para contagem
temp = flag = ''
counter_idmaior = idade_pessoa_atual = sun_id = counter_pessoa = F_menor = 0

while True:
    nomes.append(input('Escreva o nome da pessoa:')) #nome das pessoas
    counter_pessoa += 1 #quantidade de idades
    idade_pessoa_atual = int(input('Escreva a idade da pessoa: ')) #idade das pessoas

    sun_id  += idade_pessoa_atual #soma as idades de todos

    temp = input('Escreva o Sexo [M-F]').upper()

    while temp not in ['M', 'F']: #tratamento de caracteres errados
        temp = input('Escreva o sexo [M-F]').upper()

    if temp == 'M': #homens
        sexo[0] += 1
        counter_idmaior += 1 if idade_pessoa_atual > 30 else 0 #maiores que 30 anos
        
    else: #mulheres
        sexo[1] += 1
        F_menor += 1 if idade_pessoa_atual < 25 else 0 #soma a quantidade de mulheres menores que 25 anos
    
    flag = input('Deseja cadastrar mais alguem: [SIM-NAO]').upper() #deseja continuar ou nao
    while flag not in 'NAO SIM':
        flag = input('Descreva novamente se quer continuar [SIM-NAO]')
    
    if flag == 'NAO':
        break
print(f'''A quantidade total de pessoas analisadas e: {counter_pessoa}
A quantidade de homens maiores de 30 anos: {counter_idmaior},
A qunatidade de mulheres e: {sexo[1]},
A media das idades e de : {sun_id / counter_pessoa} anos
A quantidade de mulheres com menos de 25 anos e de: {F_menor} mulheres
      ''')
