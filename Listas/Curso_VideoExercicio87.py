#aprimorado do Exercicio 86
'''
Docstring para Listas.Curso_VideoExercicio87
    ✅ a) Soma de todos os valores pares digitados
    ✅ b) Soma dos valores da terceira coluna
    ✅ c) O maior valor da segunda linha
'''
def Maior(x):
    maior = 0
    for i in range(len(x)):

        if maior < x[i] or maior == 0:
            maior = x[i]

        if maior == x[i]:
            maior = x[i]
    return maior

matriz = []
temp = []
n = 0
for i in range(0,3):
    for j in range(0,3):
        n = int(input(f'Escreva um numero para a matriz {[i]}{[j]}: '))
        temp.append(n)
    matriz.append(temp.copy())
    temp.clear()
for x in matriz:
    for n in range(0,len(x)):
        print(f'[ {x[n]}  ]',end='') if n <= 1 else print(f'[ {x[n]} ]\n')

p = sum(n for x in matriz for n in x if n % 2 == 0)
s = sum(n for x in matriz for n in x if x.index(n) == 2)
q = Maior(matriz[1])
print(f'\nA soma de todos os valores pares da matriz e: {p}')
print(f'\nA soma da terceira coluna e: {s}')
print(f'\nMaior valor da segunda linha e: {q}')
