a = [2,3,4,7]
#b = a #python cria uma ligacao entre as listas elas sao iguais entao ele liga
b = a[:] #nao cria ligacao e sim uma copia
b[2] = 8
print(a)
print(b)
'''from random import randint as rd
lista1 = [rd(0,20) for i in range(0,10)]
lista2 = list(range(4,10))
print(lista2)
lista1.append(-1)
print('Com append',lista1)
lista1.insert(0, -2) #adiciona o numero -2 na posicao 0 e desloca o array para frente
print('Com insert',lista1)
del lista1[3] 
lista1.pop(3)#normalmente usado para apagar o ultimo elemento, mas aceita parametro
#passado o indice
print(lista1)
lista1.remove(-1)
#passado o valor da lista
print(lista1)
lista2.sort(reverse=True) #ordem reversa de ordem
print(lista2)'''