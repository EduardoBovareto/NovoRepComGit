from random import randint as rd
def MaioMenor(lista):
    maior = 0
    menor = 0
    for i in range(0, len(lista)):
        if maior <= lista[i] or maior == 0:
        #caso de valor zerado ou maior < menor que o utlimo adicionado
            maior = lista[i]

        elif menor >= lista[i] or menor == 0:
            #caso de valor zerado ou menor sendo um valor <  que o utlimo adicionado
            menor = lista[i]
    return maior, menor
turmas = [[rd(2,10) for i in range(0,4)] for i in range(0,4)]
print(turmas)
s = maior = menor = 0
r_turmas = []
for i in range(0, len(turmas)):
    s += sum(turmas[i])
    maior, menor = MaioMenor(turmas[i])
    print(f'A turma: {i + 1} tem media: {s / len(turmas[i])}, Maior nota: {maior}, menor nota: {menor}')
#realizar menor media de todas as tumas!
   