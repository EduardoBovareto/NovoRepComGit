'''
t1 -> Quantidade de pessoas que clicaram no primeiro link.
t2 -> Quantidade de pessoas que clicaram no segundo link.
t3 -> Quantidade de pessoas que clicaram no terceiro link

t1 = 2 * t2 
t1 = 4 * t3

t2 = 2 * t3
t2 = t3 *  2

t3 = t2 / 2
'''

t3 = int(input('Informe o valor de pessoas:')) # Pessoas que clicaram no terceiro link do site

if t3 > 1000 or t3 < 1:
    print('\n O valor está acima do range t(1 <= t <= 1000)\n')
    while t3 > 1000 or t3 < 1:
        t3 = int(input('Informe o valor de pessoas novamente:'))
t2 = 2 * t3 # Pessoas que clicaram no segundo link do site
t1 = 4 * t3 # Pessoas que clicaram no primeiro link do site
print(t1)