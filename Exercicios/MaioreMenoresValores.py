#SUBPROGRAMA
def AchaMaior(Valores = None):
    i = 0
    menor = Valores[i]
    maior = Valores[i]
    j = i + 1
    while i != (len(Valores) - 1):
        if maior < Valores[j]:
            maior = Valores[j]
            continue
            
        elif menor >  Valores[j]:
            menor = Valores[j]
            continue
        i += 1
        j = i + 1
    return maior, menor
#PROGRAMA PRINCIPAL
import random
Verifica = input('Deseja usar valores aleatório ou Digitar?')
if Verifica == 'Sim':
    ValorAnalise = list(range(-5, 10,)) #Gera uma lista com valores de 0 até 30
    random.shuffle(ValorAnalise)
    print('Aleatorio, ', ValorAnalise)
    print(AchaMaior(ValorAnalise))
else:
    Numeros = input('Digite os valores com espaço')
    Numeros = list(map(int, Numeros.split()))
    print(AchaMaior(Numeros))
# random.shuffle(ValorAnalise) #Embaralha os valores. 