#funcoes
def soma(a, b): #parametros da funcao
    s = a + b
    print(f'A = {a} e B = {b}, a soma da: {s}')


def contador(*num):#poderia ser uma lista tambem
    #o * permite colocar varios valores no parametro num e adiciona ees em uma tupla
    print('elementos : ',len(num))


def dobra(lst):
    lst = list(map(lambda x: x * 2,lst))
    print(lst)
    '''outro metodo
    pos = 0
    while pos < len(lst):
        lst[pos] * 2
        pos += 1
    '''

#programa principal
soma(8,9)
soma(a=3, b=5)
contador(2,1,8)
contador(0,8,9,4,3,2)
contador(0)
dobra([2,4,6])
