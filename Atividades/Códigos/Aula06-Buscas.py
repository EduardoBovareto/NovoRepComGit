from random import randint # Importa módulo gerador de valores aleatório

def BinarySearch(ListaOrdenada, ValorDesejado):
    # Sempre em busca binária trabalhamos com o índice do array, nunca com o numero do elemento.
    # A busca binária sempre trabalha com o indice dos elementos, meio, inicio e fim sao indices
    inicio = 0 # Toda Posição de array começa com 0.
    Fim = len(ListaOrdenada) - 1 # Ultima posição do array
    meio = (inicio + Fim) // 2 # Indice do meio, conta lógica

    while ValorDesejado != ListaOrdenada[meio] and inicio < Fim: 
        #Enquanto o que eu quero for diferente do valor do meio do array e inicio < Fim significa que eu vou procurar. Se inicio == Fim, então, eu achei meu desejado, se menor ainda e ValorDesejado == ListaOrdenada[meio] se quebra o while também
        #  
        if ValorDesejado > ListaOrdenada[meio]: # Caso de ValorDesejado ser Maior que o elemento do meio
           inicio = meio + 1
           meio = (inicio + Fim) // 2 # Sempre precisa mudar o meio, mesmo se o fim ou o inicio aumentam, nos dois casos, de maior e menor

        else:
            Fim = meio - 1 # Se menor é porque está para a esquerda
            meio = (inicio + Fim) // 2
        
        if ValorDesejado == ListaOrdenada[meio]: # Caso onde nas primeiras análises o ValorDesejado está no meio
            local = ListaOrdenada[meio] # Guardando Valor do meio.
        else:
            local = -1 # Retorna -1 se não encontrou nada

    return local

Lista = []
for i in range(0, 11):
    Lista.append(i)

print('Valor encontrado é:', BinarySearch(Lista, randint(0, 12)))
# Chama a função com a lista de valores e um valorDesejado aleatório com 1 a mais para dar -1 em algum caso.