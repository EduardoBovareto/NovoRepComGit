#analise de triangulos com if..elif.. else
import math as mt
def AnalisaExistencia(a = int, b = int, c = int):

    condicao1 = (a + b) > c
    condicao2 = (a + c) > b
    condicao3 = (b + c) > a

    if condicao1 == False or condicao2 == False or condicao3 == False:
        return 'Não forma um triângulo'
    
    else:
        #triangulos isoceles
        if b == c and a != b:
            return 'Formam um triângulo Isóceles!!'
        
        elif a == b == c:
            return 'Formam um triângulo Equilatero!!'
        
        else:
            return 'Formam um triângulo Escaleno!!'

#coleta os valores
Valores = input('Escreva 3 valores para lados de triangulo: ').split()

#transforma os valores
temp = list(map(lambda x: int(x), Valores[::]))
Valores = temp
#separa os valores
a, b, c = Valores
print(AnalisaExistencia(a, b, c))
