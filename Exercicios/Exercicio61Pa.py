# PA -> an = a1 + (n-1) * r
a1 = int(input('Informe o primeiro valor da PA:')) #primeiro termo
r = int(input('Informe a razao da PA: ')) #razao
n = 1 # 10 termos da PA
Pa = a1
while n < 10:
    if n == 1: print(f'{a1}',end=' -> ') 
    Pa += r
    print(f'{Pa} -> FIM' if (n == 9) else f'{Pa}', end='->')
    n += 1