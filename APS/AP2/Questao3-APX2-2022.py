#Q3 da APX2-2022
def ImparPar(Lista, Pares, Impares):
    tamanho = len(Lista) - 1
    while tamanho > 0:
        if (Lista[tamanho] % 2) == 0 : #Caso de numero Par
                Pares.append(Lista[tamanho]) #Valores Pares
        else: #Caso impar
            Impares.append(Lista[tamanho]) # Valores Impares  
    tamanho -= 1
    print(f'Par: {Pares}, Impar:{Impares}')

def ProcessaArquivos():
    Arquivo = input('Informe o nome do Arquivo e a extensão: ')
    primo = 0
    LinhaDeixar = []
    Par = Impar = []
    Falso = False
    with open(Arquivo, 'r') as Linhas: # Abrindo arquivo
        print(Arquivo)
        for posicao in Linhas: # Pega as linhas
            Valores = list(map(int, posicao.split()))
            # Faz o split da linha que se pegou, usa map para mudar o tipo primitivo com
            # 2 argumentos e disso, se torna uma lista novamente, porque map é um outro tipo.
            for k in range(len(Valores)):
                i = 9
                if Valores[k] >= 1: # Condicao principal
                    while i > 0: #for i in range(1, 10):  # Range para teste de divisibilidade         
                        if (Valores[k] % i) == 0: #Caso para analise de primo.
                            primo += 1 #Variavel counter que conta o numero de divisores.
                        i -= 1

                    if primo >= 2 or Valores[k] == 1: # linha sem primos
                        primo = 0
                        Falso = True   #Variavel controle para guardar linha                     
                        continue # Impede continuidade de outras condictions

                    elif primo == 1: # Ele então é divisível por ele mesmo e por 1 só.
                        #Devemos excluir a linha
                        primo = 0 
                        Falso = False
                        break #Break of the continuation of the execute, and back the estruct for.

            ImparPar(Valores,Par, Impar) #Função que acha Par e impar

            if Falso == True: #Significa que a linha inteira não tem primos, logo, manter ela
                if '\n' in posicao:
                   quebra = posicao.find('\n')
                LinhaDeixar.append(posicao[:quebra])  # Linhas sem primos
                continue
    Arquivo2 = 'ArquivoAlterado.txt'
    print('Conteúdo do Arquivo numeros.txt após eventuais remoções:')
    with open(Arquivo2, 'w') as Escrita: #Cria um novo arquivo para escrever as linhas.
        for L  in range(len(LinhaDeixar)):
            Escrita.write(f'{LinhaDeixar[L]}') # Escreve linhas sem primos.
            Escrita.write('\n')
            print(f'{LinhaDeixar[L]}\n')
ProcessaArquivos()