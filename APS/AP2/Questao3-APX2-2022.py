#Q3 da APX2-2022
Resultado = 0
def ProcessaArquivos():
    Arquivo = input('Informe o nome do Arquivo e a extensão: ')
    primo = 0
    LinhaDeixar = []
    Falso = False
    with open(Arquivo, 'r') as Linhas:
        print(Arquivo)
        for posicao in Linhas: # Pega as linhas
            Valores = list(map(int, posicao.split()))
            # Faz o split da linha que se pegou, usa map para mudar o tipo primitivo com
            # 2 argumentos e disso, se torna uma lista novamente, porque map é um outro tipo.
            for k in range(len(Valores)):
                if Valores[k] >= 1: # Condicao principal
                    for i in range(1, 10):  # Range para teste de divisibilidade         
                        if (Valores[k] % i) == 0:
                            primo += 1

                    if primo >= 2 or Valores[k] == 1: # linha sem primos
                        primo = 0
                        Falso = True                        
                        continue

                    if primo == 1: # Ele então é divisível por ele mesmo e por 1 só.
                        #Devemos excluir a linha
                        primo = 0 
                        Falso = False
                        break

            if Falso == True: #Significa que a linha inteira não tem primos, logo, manter ela
                LinhaDeixar.append(posicao)
                continue
    Arquivo2 = 'ArquivoAlterado.txt'
    print('Conteúdo do Arquivo numeros.txt após eventuais remoções:')
    with open(Arquivo2, 'w') as Escrita:
        for L  in range(len(LinhaDeixar)):
            Escrita.write(LinhaDeixar[L])
            Escrita.write('\n')
            print(f'{LinhaDeixar[L]}')

    # with open(Arquivo2, 'r') as Escrita:
    #          {Arquivo2.read()}''')
ProcessaArquivos()
