from tkinter import *
from webbrowser import BackgroundBrowser
windowNew = Tk() # Cria uma nova janela
def tela(janela):
    janela.title("Cadastro de Leads")
    janela.configure(background = "#44bb99") # fundo da janela
    janela.geometry("680x500") # tamanho da janela
    janela.minsize(width=400, height=400) # Tamanho minimo da janela em caso de diminuição
    janela.resizable(True, True) # Responsividade na horizontal e vertical
    janela.mainloop() # Abre a janela e mantém ela aberta
tela(windowNew)
