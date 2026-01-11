matriz = []
temp = []
for i in range(0,3):
    for j in range(0, 3):
        n = int(input(f'Digite um valor da matriz para [{i},{j}]: '))
        temp.append(n)
    matriz.append(temp.copy())
    temp.clear()

for lista in matriz:
    for indice in range(0, len(lista)):
        print(f'[  {lista[indice]}   ]',end='') if indice <=1 else print(f'[  {lista[indice]} ]\n')