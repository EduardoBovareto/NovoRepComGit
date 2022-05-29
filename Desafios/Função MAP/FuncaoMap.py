#Algorithm about the function map()
''''
map() Aplica a cada elemento de uma lista uma determinada função, seja ela conversão ou seja ela uma muiltiplicação em cada elemento da lista.
Ao se usar map(), ele tornará o elemento list em objeto map então se precisa converter novamente em list.
    Perceba que o split está fora do conjunto, ele pode estar tanto dentro quanto fora do map, é uma expressão.
'''

# ValuesNew = input('Write values with between space in they').split()
# ValuesNew = list(map(int, ValuesNew))
# print(ValuesNew)
# print(type(ValuesNew[0]))
###############################
ValueNewT = list(range(0, 20)) # Generationn of the values in under a list
ValueNewT = map(str,ValueNewT) # convertion for strings in under list
print(ValueNewT) # Mas na lista o tipo muda para map e vira objeto 
print(type(ValueNewT))
ValueNewT = list(map(int, ValueNewT))

##############
Novo = list(range(0, 23))
print(Novo)
Novo = list(map(str, Novo))
print(Novo)
lista2 = [int(x) for x in Novo] # Forma condesada de for que converte cada elemento para int
print(lista2)