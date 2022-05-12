'''
Script que recebe numeros e decide qual é o numero par, impar, maior e menor.
'''

def calculaParImpar(conteudo):
    if conteudo % 2 == 0:  # Condição par
        par.append(conteudo)  # Adicionando ao array um valor
    
    if conteudo % 2 != 0:  # Condição impar
        impar.append(conteudo) # Adicionando ao array um valor

    return None

control = '1'
maior = 0 
menor = 0
par = []
impar = []
dadoDeCond = control.isnumeric() # Condição inicial obrigatória

while dadoDeCond != False: # Forço uma execução pois '1' sempre poderá ser um número

    i = 1 # Variavel controle obrigatória para o bloco
    if i == 1:
        valor = int(input('Informe seu valor: '))
        calculaParImpar(valor)
    
        if valor > maior:
            maior = valor
            print(maior)

        elif valor < maior:
            menor = valor

        control = input('Deseja Continuar? 1.True ou " " ') # Verificação de continuidade
        dadoDeCond = control.isnumeric() 

        if dadoDeCond != True: 
            # Preciso desse bloco, pois, eu preciso colocar 0 no i
            #  ai sim eu irei passar false para dadoDeCond.

            i = 0
            print('''
                Dos valores digitados, O deles maior:{}, o deles menor:{}
                Quantidade de numeros pares:{}, Quantidade de numeros impares:{}

                '''.format(maior, menor, len(par), len(impar))) 
                