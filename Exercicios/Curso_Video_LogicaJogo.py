numero_player = count = maior = menor = 0
votos = [0,0,0,0,0,0,0,0,0,0]
print('-'*10,'Votação de jogadores', '-'*10)

while True:
    numero_player = int(input('Escreva um numero de um jogador entre 1 e 10: '))
    
    if numero_player == 0:
        break
    
    count += 1
    while numero_player > 10 or  numero_player < 1:
        numero_player = int(input('Digito Desconsiderado! Escreva novamente entre 1 e 10! '))

    votos[numero_player-1] += 1
    print(votos[numero_player-1])
        #incremento de voto, o numero do jogador e 1 a menos no array

for i in range(0,10):
    if maior == 0 or votos[i] > maior:
        maior = votos[i]

    elif menor == 0 or votos[i] < menor:
        menor = votos[i]
    
    pass    
print(f'''Total de votos: {count}, {votos}, {maior}, {menor}''')