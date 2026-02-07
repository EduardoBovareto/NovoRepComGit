flag = '' #controle de parada
jogadores = {} #time gerenciado
jogador = {}
gols = []
counter = 0

caracteres_proibidos = '!@#$ %&*()_-+={ }[]|\:;"<>?/'
while True:
    jogador['nome'] = str(input('\nQual o nome do Jogador: '))
    while  any(c in caracteres_proibidos for c in jogador['nome']):
        #anotar any no caderno
        print('\nNao colcoar caracteres especiais nem espacos!')
        jogador['nome'] = str(input('Qual o nome do jogador: '))
    jogador['partidas'] = int(input(f'\nQuantas partidas {jogador['nome']} jogou: '))
    
    for gol in range(0,jogador['partidas']):
        gols.append(int(input(f'\nQuantos gols na partida {gol+1}: ')))
    jogador['gols'] = gols

    counter += 1
    jogadores[counter] = jogador.copy()
    jogador.clear()

    #estrutura de parada
    flag = str(input('\n\nDeseja continuar: [S/N]')).upper()
    while flag not in 'S N':
        flag = str(input('Erro de entrada! Deseja continuar: [S/N]')).upper()
    if flag == 'N':
        print(f'{'-='*30}')       
        for i,j in enumerate(jogadores):
            print(i)
            for d in j.value():
                print(d)
        break