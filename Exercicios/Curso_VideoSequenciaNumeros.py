'''
n = quantidade de termos
an =  ultimo termmo que a sequencia ira para
a1 =  primeiro termo da sequencia
a1 = 1
temp = 1
1 + 1 = 2
2+ 2 = 4
4 + 3 = 7
7 + 4 = 11
11 + 5 = 16
16 + 6 = 22
22 + 7 = 29
29 + 8 = 37
37 + 9 = 46
temp = variavel para as somas
'''
n = int(input('Digite a quantidade de termos desejada: '))
an = (1 + (n - 1) * n ) / 2 #revela o ultimo termo da sequencia
a1  = 1 #primeiro termo
temp = 1
print(a1)

for i in range(a1, n+1):
    print(f'{a1} + {temp} -> {a1 + temp}')
    temp += a1
    a1 += 1
