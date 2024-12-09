def B(nome, salario, idade): 
    conta = {
        'Nome' : nome,
        'Salario' : salario,
        'Idade' :idade
        #uma chave receber um valor a partir de uma variavel, e pelos : e nao por =
    }
    return conta

Minha_conta = B('Eduardo', 4000.00, 22)
operacao = True

while operacao == True:
    temp = int(input
    ('''
        Informe a operação desejada a seguir:
        \033[1;40m0- Finalizar atendimento\033[m
        \033[1;40m1- Realizar compra\033[m
        \033[1;40m2- Receber Pagamento\033[m
        \033[1;40m3 - informar salario\033[m
'''))
    #TODA VEZ QUE SE COLOCAR COR, DEVE TERMINAE E COMEÇAR COM \033[m

    if(temp == 0):
        print('Operação Finalizada!')
        operacao = False

    elif(temp == 1):
        custo = float(input('Digite o valor da sua compra: '))
        Minha_conta['Salario'] = Minha_conta['Salario'] - custo
        print(Minha_conta['Salario'])

    elif(temp == 2): 
        ad = float(input('Qual o valor a ser adicionado: '))
        Minha_conta['Receita'] = Minha_conta['Salario'] + ad
    
    elif(temp == 3):
        print(Minha_conta['Salario'])
        print(Minha_conta.values())
