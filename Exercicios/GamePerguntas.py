import random
import emoji
import pygame

def MatematicaPlay():#Funcao mae
    pygame.init() #todo pygame precisa ser iniciado para trabalhar com metodos

    pygame.mixer.init() #inicia o mixer do pygame para tocar o arquivo
    
    print('Este é um mini jogo de perguntas e respostas matematicas!!!')
    j = 2 #variavel de controle
    n = ['+', '-', '*']
    p = resultado =  score = 0

    while j != 0: #definidor de chances
        p = input('Digite uma operação: ')
        if(p in n):
            a = random.randint(-50, 50) #Geram os valores para tentativas
            b = random.randint(-10, 100)
            resultado = eval(f'{a} {p} {b}') 
            # funcao que permite analisar "strings"  realizar resultados
            p = int(input(f'Quanto é {a} {p} {b}: '))
            #no caso aqui, resultado calcula atraves de eval que analisa!

            if(resultado == p):
                print(emoji.emojize(':thumbsup:', language='alias'))
                #Printa um emoji de positivo acertou, entre :nome do emoji no site e config:

                som_correto = pygame.mixer.Sound('Exercicios/correct-choice-43861.mp3') #tras o arquivo pro codigo, carregando-o
                #dentro de pygame, o mixer e um dos modos de colocar som
                som_correto.play()  #toca o arquivo
                score += 2
                print(f''' Score =  {score}
                ''',end=''' 
''')
            else:
                print(emoji.emojize(":dagger:"))
                j-= 1
                som_inco = pygame.mixer.Sound('Exercicios/error-10-206498.mp3')
                #Som de errado
                som_inco.play()
                print(f'Lhe resta apenas {j} chance' if j != 0 else 'Acabou para voce!')
        else:
            print('Há algo de errado, parece que você digitou um operador errado!!')
            return None

MatematicaPlay()  
            

