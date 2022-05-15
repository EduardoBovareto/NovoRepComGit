from random import shuffle
temp = []
def Bubble_Sort(v): # Algoritimo de ordenacao (ruim, repete muitas vezes sem fazer nada e é lento)
    fim = len(v)
    inicio = 0
    while fim > 0: # Vai ordenando e diminuindo o fim
        i = 0
        while i < fim-1:
            if v[i] > v[i + 1]: # Casso onde o anterior é maior que o próximo
                temp = v[i] 
                v[i] = v[i + 1] # O Antecesseor pega o valor menor 
                v[i + 1] =  temp # O sucessor pega o valor maior
            i += 1
        fim -= 1
    return v
vetor = list(range(0, 5)) # Gera uma lista automática ao ser executado de numeros em ordem.
shuffle(vetor) # Função do modulo random qeu embaralha os numeros de um vetor
print(Bubble_Sort(vetor))