def Emprestimo(salario=float, Vcasa=float,Tempo=int):
    Tempo *= 12 #12 meses a cada ano (Gerar um valor inteiro)
    parcela = float(f'{(Vcasa / Tempo):.2f}')

    if(parcela  >= (salario * 1.30)):
        print(f'''
              Não foi possivel realizar seu emprestimo!
              Pois a parcela: {parcela} supera o salario digitado {salario} em 30%
              ''')
        return False
    
    else:
        print(f'''
              Parabens!! Emprestimo realizado com sucesso!
              A parcela ficou de: R${parcela}
              Num período de {Tempo} meses            
              ''')
        return False
    
emprestimo= True
while emprestimo == True:
    sal = float(input('Qual seu salario Atual: '))
    ValorCasa = float(input('Qual valor da casa atualmente:'))
    temp = int(input('Qunatos anos voce deseja pagar esta casa: '))
    emprestimo = Emprestimo(sal, ValorCasa, temp)
