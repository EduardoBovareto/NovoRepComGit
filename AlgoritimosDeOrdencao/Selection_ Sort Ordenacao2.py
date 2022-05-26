from random import shuffle 
'''
Seleciona os menores elementos primeiro, para depois selcionar os maiores.
    Ex: ele selecionaria no vetor padrão que criamos antes, o 0 primeiro depois o 1 e assim sucessivamente.
'''
def Selection_Sort(v): # Trabalha de forma posicional, encontra a posição de um elemento menor de todos
    n = len(v)
    for j in range(n -1): # Percorre cada elemento
        menor = j # Pega cada indice da posição em questao
        for i in range(j, n): # É forçado a analisar cada elemento de uma vez
            if v[i] < v[menor]: # Compara pra ver se a posição anterior que é menor, é menor que a atual 
                menor = i # Se for menor ele pega essa posicao para trocar os numeros
        if v[j] > v[menor]:
            temp = v[menor]
            v[j] = v[i]
            v[i] = temp

vetor = [7, 5, 1, 8, 3]
print(Selection_Sort(vetor))


'''
# Eu guardo a primeira posição como menor para analisar se essa posiçao é a menor, poderia fazer com a próxima também, o que daria mais efetividade, mas o que é guardado é a primeira posição como menor ja que o for irá percorrer cada indice de cada elemento.
# Guarda se na variavel menor esse primeiro valor e depois compara com os proximos se eles sao os menores.
'''
