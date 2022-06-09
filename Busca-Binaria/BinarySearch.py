from random import choice
def BinarySearch(Array, buscado):
    Start = 0 # Inicio
    end = len(Array) - 1 # Fim do array
    elemento = 0
    
    while Start <= end:
        meio = (Start + end) // 2 # Meio do array

        if buscado == Array[meio]:
            return ('O meio', meio, Array[meio])

        elif buscado > Array[meio]:
            Start = meio + 1
            elemento = Array[Start:]

        elif Array[meio] > buscado:
            end = meio - 1
            elemento = Array[Start:end]

    return None
c1 = [1, 2, 3, 4, 5, 6]
c2 = [2000, 1000, 500, 10]
L = [c1, c2]
print(BinarySearch(c1, choice(c1)))