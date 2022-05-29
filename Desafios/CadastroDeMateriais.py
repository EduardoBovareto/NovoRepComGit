'''  # Podemos fazer contas com o aumento e preço de produto. Algorítimo que faz uma relação de materiais digitados pelo usuário.'''
# from random import randint
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
    return Matriz

def GerarLista(Dados, Extension = None): #Var gerar um documento txt com os dados da outra função e colocará nesse arquivo.
    with open(input('Write name of the file with extension: '), 'w') as Linhas: #Para criar um arquivo podemos passar como parametro o input desejando a extensão.
        k = 0
        j = 0
        Linhas.write('========== LISTA DE MATERIAIS ============')
        Linhas.write('\n\n')
        while k != len(Dados):
            j = 0
            while j != len(Dados[k]): # Pega cada array dentro da Matriz
                Material = Dados[k][j] # Pega cada elemento de cada array dentro do arrayzao
                Linhas.write(f'{Material}  ')
                if j == 1:
                    Linhas.write(' \n')
                j += 1
            k += 1
            ''' Precisa incrementar sempre para não ser infinito, pois ele volta do while interno para o externo e checa k e k precisa mudar.'''
            # TODA VARIAVEL QUE USADA NO while E QUE USA O SISTEMA DE DEPENDENCIA DE ITERAÇÃO DEVE FICAR DENTRO DO SEU while PAI. SE TIVERMOS 2 WHILES UM DENTRO DO OUTRO, SE FAZ A SEGUINTE ESTRUTURA:
            ''' 
                while j != len(AlgumArray):
                    while j1 != pai:
                        comandos
                        j1 += 1
                    j += 1
                    Perceba que para que j seja iterável e que não se torne infinoto, o j deve estar dentro do seu pai e j1 deve estar dentro do seu while pai. Sendo assim, j1 está dentro do seu avô.
            '''
# PROGRAMA PRINCIPAL
materiais = input('Informe os materiais, a quantidade').split() # Coleta os materias da loja
File = CadastraMateriais(materiais) # Chamada da function  que retorna e armazena em file
GerarLista(File)
