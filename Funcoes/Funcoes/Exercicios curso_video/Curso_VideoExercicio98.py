from time import sleep as sl
def contador():
    print(f'\n\n{'-=' * 30}')
    
    print('Contagem de 1 ate 10 de 1 em 1')
    print(f'{'-=' * 30}')
    sl(1)#aguarda 1 segundos

    for i in range(1,11,1):#1 for de 1 em 1
        print(i, end=' ', flush=True)
        sl(0.2)
    print('FIM!')

    print(f'{'-=' * 30}')
    print('Contagem de 10 ate 0 de 2 em 2')
    for i in range(10,-2,-2):
        print(i, end=' ', flush=True)
        sl(0.2)

    print('FIM!')
    print(f'{'-=' * 30}')

    print('Agora e sua vez de personalizar a contagem!')
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    print(f'{'-=' * 30}')
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
    
    if passo == 0:
        passo = 1
    if fim < inicio and passo > 0:#preciso que na contagem inversa ele conte o fim tambem!
        # 33 a -3 o fim deve ser 1 vez o passo maior
        passo *= -1
        fim += passo

    else:
        fim += passo
    for i in range(inicio, fim, passo):
        print(i,end=' ',flush=True)
        sl(0.2)
    print('FIM!')

    
#Programa principal
contador()