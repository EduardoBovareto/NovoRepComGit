# SUBPROGRAMAÇÃO
def CadastraMateriais(Mat): # Pegará os materiais e colocará em matraiz
    Matriz = [] # Matriz final
    temporario = [] # Materiais
    i = 0
    while i != len(Mat): #  i começa em 0 e é diferente de len(Mat) == 4 até que i chegue a 4
        while len(temporario) != 2: #Temporario começa com 0 e deve ser adicionado 2 elementos 
            if Mat[i].isnumeric():
                temporario.append(int(Mat[i])) # Ou temporário = list(map(int, Mat[i]))
            else:
                temporario.append(Mat[i])
            i += 1 # Sempre aqui dentro, pois ao terminar as verificações ele incrementa, se estiver fora não muda a posicao de Mat[i].
        Matriz.append(temporario)
        temporario = [] 
        
    
    # for i in Mat: # Percorre as informações para diferenicar cada uma
    #     if i.isnumeric(): # Caso de numero de material
    #         i = int(i) # Cso seja válido, se converte o numero antes em string
    #         temporario.append(i) # Adicionando o valor em forma inteira
    #     else:
    #         temporario.append(i) # Caso onde é o nome do material

    #     if len(temporario) == 2: # Condição de array temporario saturar cada material
    #         Matriz.append(temporario) # Adiciona as informações a matriz
    #         temporario = [] # limpa o aray temporário
    #         continue # Passa para o próximo i
    
    j = 0
    for i in range(len(Matriz)): # Laço que percorre cada linha da matriz
        for j in Matriz[i]: # laço que percorre cada coluna da matriz
            # if j == Matriz[i][2]: # Caso onde se tem o valor do dinheiro
            #     print('\033[1;34;44m', 'R$', j ,'\033[m' , end=' ')
            print('\033[1;34;44m', j ,'\033[m' , end=' ')  # Printa cada elemento e no final coloca um espaço e cores no terminal
        print('\n') # Quebra a linha no final para a próxima linha

# PROGRAMA PRINCIPAL
materiais = input('Informe os materiais, a quantidade').split() # Coleta os materias da loja
CadastraMateriais(materiais) # Chamada da function
# Podemos fazer contas com o aumento e preço de produto.
