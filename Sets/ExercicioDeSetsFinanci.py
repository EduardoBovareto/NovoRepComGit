def processa_bonus(funcionario, conj):
    Veri = 'há funcionarios'
    while Veri == 'há funcionarios':
        if funcionario[0] > 3500:
            if funcionario[1] > 5 and funcionario[2] > 10:
                conj[0] = (45 / 100) * conj[0] #Caso de 45% de bonus em funcionarios antigos 

            elif funcionario[1] < 5:
                    print('Não há bônus para funcionarios novos')
        else:
            Veri = input('Informe se há funcionario')
            if Veri == 'ha funcionarios':
                funcionario = float(input('Digite: '))
                funcionario = list(map(float, funcionario))
                return processa_bonus(funcionario, conj)

Salario = float(input('Digite: '))#salario, Tempo de contribuição, Projetos
Lista = list(map(float, Salario))
Bonus = []
processa_bonus(Lista, Bonus)