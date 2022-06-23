def ConverteBin(Valo, divi):
    if Valo != 0:
        if Valo % 2 == 0:
            divi += '0'
            return ConverteBin(Valo // 2, divi)
        else:
            divi += '1'
            return ConverteBin(Valo // 2, divi)
    return divi
Valor = -1
while Valor < 0:
    Valor = int(input('Digite o numero:'))
print(ConverteBin(Valor,''))
#Recursividade sempre retorna pra ela mesma, ou seja, na maioria das vezes usa return chamando ela mesma e dentro dela uma condicao de parada