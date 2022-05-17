''' Esse algorítimo tem um procedimento que irei tratar como uma função, mesmo não sendo as mesmas coisas.
    Esse procedimento pega uma sequência de numeros inteiros que devem ser organizados em ordem.

    O algorítimo principal irá receber a quantidade de pessoas que irão tomar vacinas dedois tipos: 1.(Coronavac) e 2.(Astrazeneca), onde informaremos a quantidade de pessoas por tipo de vacina e veremos se tem pra todas a informadas.
'''

def OrganizaInteiros(numeros, people, v1, v2): # v1 é a coronavac, v2 é a Astrazeneca
    # Organizar os inteiros:
    maior = 0
    menor = 0
    j = 1
    k = 1
    for i in range(len(numeros)):
        numeros[i] = int(numeros[i])

    for i in numeros:
        if i == 1:
            v1 = v1 - 1

        if i == 2:
            v1 = v1 - 1
            v2 = v2 - 1

        if v1 == 0:
            j = 0
            break

        if v1 == 0 or v2 == 0:
            k = 0
            break

    if j == 0 :
        print(f'N')
    
    elif k == 0:
        print(f'N')
    else:
        print('S')

Pessoas = int(input(' Informe a quantidade de pessoas para tomarem a vacina:'))
numeros = input(' Informe vacinas por pessoas separado por espaço:').split()
Pessoas -= 1 # caso onde o array "numeros" tem uma posição a mais que o numero de pessoas pois começa do 0.
while len(numeros) == Pessoas: # A quantidade de pessoas == len(numeros)
    numeros = input(' Informe vacinas por pessoas separado por espaço:').split()
Coronavac = int(input(' Informe a quantide de  vacinas (Coronavac):'))
Astrazeneca = int(input(' Informe a quantide de  vacinas (Astrazeneca):'))

OrganizaInteiros(numeros, Pessoas, Coronavac, Astrazeneca)



# ''' Fiquei em dúvida em percorrer um laço de uma string ou array ou fazer uma repetição
#     Também em dúvida no funcionamento do split(), assim como, percorrer uma string e/ou array e conversão de string para int() dentro de um for.
#     Uma das dúvidas geradas foi a de percorrer um objeto "String/Array" para converter cada elemento da string para o tipo number, se eu tinha que criar um novo ou se eu posso substituir no mesmo array devido a imutabilidade.
# '''