import requests as rq
from tkinter import *
import tkinter as tk
from tkinter import messagebox as msg
import pygame as py
from PIL import ImageTk, Image

#cria a interface do banco
def cadastra_lead(lista):
    #mensagem de atenção na cadastro com som interativo
    msg.showinfo('CADASTRO DE LEAD', message='Cadastro realizado com sucesso')
    py.mixer.init()

    som = py.mixer.Sound('TKINTER/Materiais de codigo/correct-choice-43861.mp3')
    #carrega o arquivo de som para ser tocado
    som.play()


def limpa_entry():
    pass
    

def configura_entradas(window, campos):
    nome = email = cpf = Idade = renda = None
    lista = [nome, email, cpf, Idade, renda]
    #entradas do sistema
    for i, (texto, tipo) in enumerate(campos):
        Label(window, text=texto).grid(row=i + 1, column=5, pady=20, padx=5, sticky='w')

        if tipo == '_nome':
            nome = tk.Entry(window)
            nome.get()
            nome.grid(row=i +1, column=6, pady=10, padx=3)
            
        elif tipo == '_email':
            email = tk.Entry(window)
            email.get()
            email.grid(row=i + 1, column=6, pady=10, padx=3)
            
        elif tipo =='_cpf':
            cpf = tk.Entry(window)
            cpf.get()
            cpf.grid(row=i + 1, column=6, pady=10, padx=3)
            
        elif tipo == '_idade':
            Idade = tk.Entry(window)
            Idade.get()
            Idade.grid(row=i + 1 , column=6, pady=10, padx=3)

        elif tipo == '_renda':
            renda = Entry(window)
            renda.get()
            renda.grid(row=i + 1, column=6, pady=10, padx=3)
            
        else:
            lista = [nome, email, cpf, Idade, renda]
            Button(window,text='Cadastro', command=lambda: cadastra_lead(lista)).grid(row=i + 1, column=6, pady=10, padx=5)
        #lambda permite argumentos das entradas

#mostra imagem
def imagem(frame, imagem):
    mostra_imagem = Label(frame, image=imagem)
    mostra_imagem.grid(row=0, column=0, sticky='nsew', padx=30, pady=30)


def cria_interface():
    #cria a interface

    root = tk.Tk()
    root.title('Nelson Bank')
    root.geometry('700x700')
    #root.iconbitmap('TKINTER/Materiais de codigo/icone.ico')

#cria o frame da pagina
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky='nsew')

    #Label titulo
    Title = Label(frame, text='Seja bem vindo ao Nelson Bank', font=('Arial', 20))
    Title.grid(row=0, column=6)
    
    #cria a imagem de tela

    #array de tuplas que contem todas as informações necessária para o banco
    informacoes = [
        ('Nome:', '_nome'), ('Email:', '_email'), ('CPF:', '_cpf'), ('Idade: ', '_idade'), ('Renda: ', '_renda'), ('Cadastrar', '_cadastro')
        ]
    
    configura_entradas(frame, informacoes)

    #carrega uma imagem
    my_image = ImageTk.PhotoImage(Image.open('TKINTER/Materiais de codigo/icone.png'))
    imagem(frame, my_image)
    
    #fecha a janela principal
    fecha_janela = Button(frame, text='Finalizar', fg='white', bg='black', command=root.quit)
    fecha_janela.grid(row=14, column=0, pady=100, padx=10)

    root.mainloop()

cria_interface()