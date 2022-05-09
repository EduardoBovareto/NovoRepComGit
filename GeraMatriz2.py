from random import randint

Nlinha = 3
Ncoluna = 2
Matriz = []
for i in range(1, Nlinha + 1):
    linha  = []
    for i in range(1, Ncoluna + 1):
        numero = randint(1, 100)
        linha.append(numero)
    Matriz.append(linha)
    print(linha)
print(Matriz)
print('\n\n')

j = 0
for i in range(0, len(Matriz)):
    for j in Matriz[i]:
        print(j, end = ' ')
    print('\n')

    '''
    O laço de fora que tem range(0, len(Matriz)) percorre cada array dentro da matriz, ou seja, cada linha da matriz que é cada array por definição. 

    Já o laço de dentro percorre cada elemento da linha que i está, se tivermos uma linha assim: [95, 56], o laço de dentro começa em j, e j assumirá cada elemento dessa linha ficticia, no caso 95 e depois 56.
    Os acessos por array seguem a didática de JS em seus acessos de caminhos arquivos armazenados numa lista.

    Ex: Pensamos novamente nisso: [[95, 56]], o i == 0 e o j == 0, a posição da primeira linha i == 0 é : [95, 56], isso se pega pelo laço de fora, e para pegar cada elemento colocamos [0], então ficaria assim:
    [0][0] onde i = j = 0, a ordem de pegar os valores segue o raciocinio assim: [0] == [95, 56] e a sgunda posição [0] pega o 95 e assim vai

    '''