import random
import emoji
import pygame

def MatematicaPlay():
    pygame.init() #todo pygame precisa ser iniciado

    pygame.mixer.init() #inicia o mixer do pygame para tocar o arquivo
    
    print('Este é um mini jogo de perguntas e respostas matematicas!!!')
    j = 2 #variavel de controle
    n = ['+', '-', '*']
    p = resultado =  score = 0

    while j != 0:
        p = input('Digite uma operação: ')
        if(p in n):
            a = random.randint(-50, 50)
            b = random.randint(-10, 100)
            resultado = eval(f'{a} {p} {b}')
            p = int(input(f'Quanto é {a} {p} {b}: '))

            if(resultado == p):
                print(emoji.emojize(':thumbsup:', language='alias'))
                #Printa um emoji de positivo acertou, entre :nome do emoji no site e config:

                som_correto = pygame.mixer.Sound('NovoRepComGit/Exercicios/correct-choice-43861.mp3') #tras o arquivo pro codigo, carregando-o

                som_correto.play()  #toca o arquivo
                score += 2
                print(f''' Score =  {score}
                ''',end=''' 
''')
            else:
                print(emoji.emojize(":dagger:"))
                j-= 1
                som_inco = pygame.mixer.Sound('NovoRepComGit/Exercicios/error-10-206498.mp3')
                #Som de errado
                som_inco.play()
                print(f'Lhe resta apenas {j} chance')
        else:
            print('Há algo de errado, parece que você digitou um operador errado!!')
            return None

MatematicaPlay()  
            

