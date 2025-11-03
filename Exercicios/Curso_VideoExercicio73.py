'''
criar uma tupla preeenchida com 20 primeiros colocados do Brasileirao,
depois mostre:
- priemiros 5 colocados
- Os ultimos 4
- Uma lista na ordem alfabetica
'''
IndexTime = 0
campeonato = ("Palmeiras", "Flamengo", "Cruzeiro", "Mirassol", "Bahia", "Botafogo", "Fluminense", "São Paulo", "Vasco da Gama", "Corinthians", "Grêmio", "Ceará", "Atlético-MG", "Red Bull Bragantino", "Internacional", "Santos", "Vitória", "Fortaleza", "Juventude", "Sport")
print(f' Os primeiros 5 colocados do campeonato Brasileiro sao: {campeonato[0:6]}\n')
print(f'{campeonato[len(campeonato) - 4:]}\n\n')
print(f'\n\nA lista  em ordem alfabetica do campeonato e:\n{sorted(campeonato)}\n\n')
x  = input('Busque a posição do seu time: ')
IndexTime = campeonato.index(x)
print(f"O {x} está na {IndexTime+1}ª posição.")