import random as rd
import pygame as py

def VerificaIdade(Y):
    py.init() #inicia o modulo para trabalhar
    py.mixer.init() #Inicia o mixer
    som1 = py.mixer.Sound('NovoRepComGit/Exercicios/correct-choice-43861.mp3')
    som2 = py.mixer.Sound('NovoRepComGit/Exercicios/error-10-206498.mp3')

    if(Y >= 18):
        print(f'Sua Idade é: {Y}')
        print('Bem vindo a localidade')
        som1.play()
    else:
        som2.play()

    #falta o som, tem de colocar delay no som para aparecer
VerificaIdade(rd.randint(6,80)) #idade ficticia