def VerificaBonus(ValorDeSalario, relacao):
    inicio = 0
    fim = len(relacao) - 1
    meio = (inicio + fim) // 2
    Percentual = [15, 12, 10, 7, 4]
    B = 0
    while inicio < meio:
        if ValorDeSalario < relacao[meio]:
            fim = meio - 1
            meio = (inicio + fim) // 2

        elif ValorDeSalario > relacao[meio]:
            inicio = meio + 1
            meio = (inicio + fim) // 2

        if ValorDeSalario == relacao[meio]:
            B = ValorDeSalario * Percentual[inicio]
        
    return B
salario = float(input('Informe seu salário para bônus: '))
Bonus = [400.0, 800, 800.01, 1200, 1200.01, 2000] # Lista de valores de salário
print(VerificaBonus(salario, Bonus))