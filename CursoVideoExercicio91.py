from random import randint as rd
jogador = {}
maior = 0
menor = 0
organizado = []

def organizar(D):
    maior = 0
    menor = 0
    for i in range(0, len(d)):
        if maior == 0 or maior <= D[i]:
            organizado.insert(3,D[i])
        
        elif menor == 0 or menor > D[i]:
            organizado.insert(0, D[i])
            
            
for i in range(0, 4):
    jogador[f'jogador {i+1}'] = rd(1,6)
    print(f'Jogador {i+1} tirou: {jogador[f'jogador {i+1}']}')
    
p = jogador.items()
p = list(p)
p = list(map(list, p))

#printar p[0] e p[0][1]
for i in p:
    for i in range(0,len(p)):
    
        if p[i][1] < p[i+1][1]:
            temp = p[i]
            p[i] = p[i+1]
            p[i+1] = temp
            
        if p[i][1] > p[i][1]:
            continue
        
        if i == 2:
            break
print(p)
    
#print(organizado)



#print(organizado)
    