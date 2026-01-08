matriz = []
temp = []
for i in range(0,3):
    for j in range(0, 3):
        n = int(input(f'Digite um valor da matriz para [{i},{j}]: '))
        temp.append(n)
    matriz.append(temp.copy())
    temp.clear()
print(matriz)