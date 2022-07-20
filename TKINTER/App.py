from tkinter import * #Importa tudo do Tkinter
from turtle import color 
app = Tk() #Abre a janela inicial de classe Tk
app.title('Aplicacao de Janelas') #Configura o titulo da janela
app.geometry('900x600+300+40') #Configura o tamanho da janela, assim aparece titulos grandes, geometria da janela
#+300 é a distanca da ponta da tela na esquerda até a janela e +40 é a ditancia de cima até o topo da janela
app.configure(background ='#Ac4') #Configura a janela, nesse caso, cor
Texto = Label(app, text ='Calendario Novo', background ='#526', foreground ='#fff') #Configura o texto que será escrito passo a passo.Todo texto precisa de uma posicao que será definida pela funcao place(), mesmo estando configurado, ele precisa de um lugar
Texto.place(x=200, y=56, width = 100, height = 120) #Define o lugar conforme coordenadas num plano cartesiano
#width e heigth sao altura e largura de area de palavra.
#Variaveis:
txt = 'Mensagem de datas'
vback = '#26A'
vfrg = '#000'
texto2 = Label(app, text = txt, bg=vback, fg=vfrg) #Configura um segundo texto == label
texto2.pack(ipadx =300, ipady = 100, padx =5, pady = 300, side ='top', fill = X, expand = True) #pack é adequado para containers
'''
ipadx = 
ipady = é o padding, preenchimento interno do elemenro e que é no sentido de plano cartesiano y
pady = 

'''
#configura a posicao do label através de containers criados e dimensionados
app.mainloop() #Executa a janela e gera a interface infinitamente