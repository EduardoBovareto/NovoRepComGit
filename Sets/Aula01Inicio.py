Conjunto = {1, 2, 3, 12, 13, 14} #Criando um sets, porém deve ter elementos para diferenciar dos dicts
#Suporta elementos imutáveis
Conjunto2 = set()
Conjunto2.add(1) #Adiciona um elemento no conjunto
# print(Conjunto2)
Conjunto.discard(12) #Retira um elemento do conjunto
# print(Conjunto)

lista = [1, 2, 3, 45, 45, 50, 50]
# print(lista)
lista = set(lista) #Nao permite elementos repetidos em sets
# print(lista)

#OPERACOES COM CONJUNTO
s = Conjunto | Conjunto2 #Operacao de uniao
s2 = Conjunto.union(Conjunto2) #Mesma uniao
#print(s, s2)

Conjunto2.add(12)
Conjunto2.add(13)
s = Conjunto.intersection(Conjunto2) #Faz a interceçao do que tem nos dois
s2 = Conjunto & Conjunto2 #Mesma operacao de intersecaçao
# print(s, s2)

Conjunto3 = {1, 2, 3, 4, 5, 6}
Conjunto2 = {5, 6, 45, 50, 67}

s2 = Conjunto3.difference(Conjunto2) #Diferença entre um e outro, o que tem em um e nao tem no outro
s = Conjunto2 - Conjunto3 #Mesma diferença
# print(s2, s)
