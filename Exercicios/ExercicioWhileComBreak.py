'''
x = 0
while x < 60:
    if x == 50:
        print('ACABOU!')
        break
    x += 5
    print(x)

'''
produto = x =  String = 0
while String != 'n': # Multiplicação resultante de somas sucetivas
    x += 3
    produto += 1
    produto *= x
    print(f'\n {produto}\n')
    if produto > 300:
        print('A coisa esta ficando muito grande!')
        break
    String = input('Deseja continuar? [s] ou [n]')
# Se precisa analisar antes e perguntar depois ao usuário   