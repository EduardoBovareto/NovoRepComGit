'''
Algorítimo que simboliza uma calculadora
Colocar o número de testes com while, pois assim temos mais controle e incrementação de var-control 
'''
def Calculadora(value1, value2, op): # Criação da função responsável por calcular
    if op == "+": # Caso de Soma
        print("SOMA!")
        soma = value1 + value2 # Operação entre os operandos
        print('A soma encontrada é: {}'.format(soma)) # Impressão
            
    elif op == "-":  # caso de subtração
        print("SUBTRAÇÃO!\n")
        subt = value1 - value2  # Operação entre os operandos
        print('\nA subtração é: {} '.format(subt)) # Impressão
    
    elif op == "*": # caso de Multilicação
        print('MULTIPLICAÇÃO')
        mult = value1 * value2 # Operação entre os operandos
        print('O resultado da subtração é: {}'.format(mult)) # Impressão
    
    elif op == "/": # caso de divisão decimal
        print('\nDivisão decimal\n')
        div = value1 / value2 # Operação entre os operandos
        print('O resultado da operação é: {}'.format(div)) # Impressão
    
    elif op == "//": # caso de divisão inteira
        print('\nDivisão Inteira decimal\n')
        DivInt = value1 // value2 # Operação entre os operandos
        print('O resultado da operação é: {}'.format(DivInt)) # Impressão

    elif op == "**": # Caso de Exponenciação
        print('\nExponenciação\n')
        Exp = pow(value1, value2)  # Ou valuE1 **value2
        print('O resultado da operação é: {}'.format(Exp))
    
    elif op == "rq2": # Caso de raíz quadrada
        print('\n Raíz Quadrada\n')
        rq2 = value1 ** (1/2) # Operação matemática, regra algébrica do sol e da sombra
        print('O resultado da operação é: {}'.format(rq2)) # Impressão

    elif op[0] and op[1] != '':
        for i in op:
            print()
        # Percorrer um laço comparando as variaveis pois ai não precisa gastar linhas
        print()

    elif op == "%": # Porcentagem de v1 em relação v2
        print('\nPorcentagem\n')
        verifica = int(input('Qual a pocentagem? 0.valor1 em relação ao valor2 ? 1.Ou o inverso?')) # Verificação de sentido de comparação

        if verifica == 0: # Caso 0
            Porcent = (value1 * 100) / value2 # Regra de 3 desenvolvida
            print('O resultado da operação é: {}'.format(Porcent)) 
        else: # Caso 1
            Porcent = (value2 * 100) / value1 # Regra de 3 desenvolvida
            print('O resultado da operação é: {}'.format(Porcent))

    elif op == "mod": # Operação de resto da divisão inteira
        print('\nResto de Divisão\n')
        modulo = value1 % value2
        print('O resultado da operação é: {}'.format(modulo))

    elif op == "n": # Caso onde se digita qalquer coisa 
        # colocar variavel controle == 1 que se for digitado algo fora de padrao e 
        # for != de 1 se emite algo
        print('Não há operador logo não há conta!')


print("{:=^20}".format("Calcula o que você quiser!\n\n"))
operacao = input('Informe a operação desejada:')

if operacao == 'conversao': # Conversão de unidades simples
    conv = input('Qual variavel deseja trabalha ?')
    EstruturaDeconversao = input('Informe o valor, a unidade convertida e o destino').split(" ")
    unidade = []
    for i in EstruturaDeconversao:
        if i.isnumeric():
            Vconv = float(i) # Valor de conversão
        else:
            unidade.append(i) # Considerar casos de comprimento
    Calculadora(Vconv, 0, unidade) # Passando os argumentos de conversão
    
else:
    valor = float(input('Informe um valor a se calcular:'))
    valor2 = float(input('Informe o segundo operando:'))
    Calculadora(valor, valor2, operacao)