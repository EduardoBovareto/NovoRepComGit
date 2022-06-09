from random import choice
'''
Relação de valores
0 - 400.00 - 15%
400.01 - 800.00 - 12%
800.01 - 1200.00 - 10%
1200.01 - 2000.00 - 7%
Acima de 2000.00     4%
'''
#SUBPROGRAMAÇÃO
def AnalisarSalario(): #Busca Binária
    RangeSalarios = [400, 400.01, 800, 800.01, 1200, 1200.01, 2000]
    Valor = choice(RangeSalarios) # Choice é uma função do módulo random que escole aleatoriamente um valor.
    final = len(RangeSalarios)
    inicio = 0
    while inicio <= final:
        meio = (inicio + final) // 2 #Pega o meio do array

        if Valor  == RangeSalarios[meio]:
            if Valor in RangeSalarios[1:2]: #Caso de 12%
                return f'{Valor * (1 + (12 / 100)):.2f}'

            elif Valor in RangeSalarios[3:4]: #Caso de 10%
                return f'{Valor * (1 + (10 / 100)):.2f}' 
            
            elif Valor in RangeSalarios[5:]: #Caso 7%
                return f'{Valor * ( 1 + (7/ 100)):.2f}'
            
            elif Valor > RangeSalarios[-1]:#Caso 4%
                return f'{Valor * (1 + (4 / 100)):.2f}'
            
            else: #Caso 15%
                return f'{Valor * (1 + (15 / 100)):.2f}'
        
        elif Valor > RangeSalarios[meio]: #Condição para correr com o inicio dentro da lógica
            inicio = meio + 1
            # meio = (inicio + final) // 2
        
        elif Valor < RangeSalarios[meio]: #Condição para correr com o fim do array
            final = meio - 1     
    return -1
#PROGRAMA PRINCIPAL
# ValorInicial = float(input('Digite seu valor: '))
print(AnalisarSalario())
'''
Da pra colocar de forma simplificada um código que tem um array com um padrão que da pra usar com o algoritimo de busca. A ideia é ter no array, sempre valor porcentagem, valor, onde os valores fazem os ranges que queremos, podemos usar a busca exata de um dado e instituindo a noção de range, onde um valor diferente possa estar entre os mesmo, aplicando assim a %.

    Essa analise substituiria a suite de porcentagens com formatação float em 2 casas decimais.
'''