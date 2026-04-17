'''
🧠 Exercício 2 — Ranking (nível prova)
alunos = [
    ['João', 7.5],
    ['Maria', 9.0],
    ['Pedro', 6.2],
    ['Ana', 8.8]
]
👉 Faça:
Ordenar os alunos pela nota (decrescente)
Mostrar apenas o nome do aluno com a maior nota
Mostrar apenas o nome do aluno com a menor nota
📌 Dica: depois do sort, observe índices da lista
'''
def ordena(classe, idade):
    maior_nota = 0 #guradara a nota de maior valor e o nome
    menor_nota = 0 #guaradara a nota de menor valor e nome
    maior = 0
    menor = 0

    for i in alunos:
    #Maior deve ser considerado como 0 pois e o estagio incial.
        if maior == 0 or maior < i[idade]:
            maior = i[idade]
            maior_nota = i
        
        if menor == 0 or menor > i[idade]:
            #menor deve ser considerado como 0 pois senao sempre sera menor, 0.
            menor = i[idade]
            menor_nota = i

    print(f'''O aluno de maior nota e: {maior_nota[0]}
O aluno de menor nota e: {menor_nota[0]}''')

alunos = [
    ['João', 7.5],
    ['Maria', 9.0],
    ['Pedro', 6.2],
    ['Ana', 8.8]
]
alunos.sort(reverse=True, key=lambda x: x[1])
#x[1] envia o dado ao sort que le alunos[0], sort organiza alunos[0][1] sem ter que acessar
ordena(alunos,1)
#melhor passar na chamada da funcao 1 valor do que em toda a condicao if