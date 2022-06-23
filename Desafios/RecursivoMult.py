def Multiplica(Value):
    if Value < 20:
        return Multiplica(Value * 2)

    return print(Value)
valor = int(input('Informe um valor'))
Multiplica(valor)
#É como se ela fosse um fim em si mesmo
