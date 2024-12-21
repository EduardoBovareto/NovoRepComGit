def Emprestimo(salario=float, Vcasa=float,Tempo=int):
    Tempo *= 12 #12 meses a cada ano (Gerar um valor inteiro)
    parcela = float(f'{(Vcasa / Tempo):.2f}')
    validacao = (parcela * 100) / salario
    if(validacao >= 30.0):
        print(f'''
              Não foi possivel realizar seu emprestimo!
              Pois a parcela: {parcela} supera o salario digitado {salario} em 30%
              A parcela representa {validacao}% do salario {salario}
              ''')
        return False
    
    else:
        print(f'''
              Parabens!! Emprestimo realizado com sucesso!
              A parcela ficou de: R${parcela}
              Num período de {Tempo} meses
              A parcela representa {validacao}% do salario {salario}

              ''')
        # return False
        return True
    
# emprestimo = True
# while emprestimo == True:
sal = float(input('Qual seu salario Atual: '))
ValorCasa = float(input('Qual valor da casa atualmente:'))
temp = int(input('Qunatos anos voce deseja pagar esta casa: '))
emprestimo = Emprestimo(sal, ValorCasa, temp)

'''

validacao -- salario
30 ------    x
x = valor da parcela que atende o cliente
valor da parcela ate 30% - (0,3 * salario ) :validacao
agr so encontrar o tempo
'''
