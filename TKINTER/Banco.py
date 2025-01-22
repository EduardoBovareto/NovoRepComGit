import requests as rq
from tkinter import *
import tkinter as tk
from tkinter import messagebox as msg
import pygame as py

#cria a interface do banco
def cadastra_lead():
    #mensagem de atenção na cadastro com som interativo
    msg.showinfo('CADASTRO DE LEAD', message='Cadastro realizado com sucesso')
    py.mixer.init()

    som = py.mixer.Sound('TKINTER/Materiais de codigo/correct-choice-43861.mp3')
    #carrega o arquivo de som para ser tocado
    som.play()


def limpa_entry():
    pass

def configura_entradas(window, campos):
    #entradas do sistema
    for i, (texto, tipo) in enumerate(campos):
        Label(window, text=texto).grid(row=i, column=2, pady=20, padx=20, sticky='w')

        if tipo == '_nome':
            Entry(window).grid(row=i, column=3, pady=10, padx=3)

        elif tipo == '_email':
            Entry(window).grid(row=i, column=3, pady=10, padx=5)

        elif tipo =='_cpf':
            Entry(window).grid(row=i, column=3, pady=10, padx=5)
            
        elif tipo == '_idade':
            Entry(window).grid(row=i, column=3, pady=10, padx=5)

        elif tipo == '_renda':
            Entry(window).grid(row=i, column=3, pady=10, padx=5)

        elif tipo == '_cadastro':
            Button(window,text=texto, command=lambda: cadastra_lead()).grid(row=i, column=3, pady=10, padx=5)
            #lambda permite argumentos das entradas

def cria_interface():
    #cria a interface

    root = tk.Tk()
    root.title('Nelson Bank')
    root.geometry('1200x900')

#cria o frame da pagina
    frame = tk.Frame(root, background='red')
    frame.grid(row=0, column=0, sticky='nsew')
    
    #array de tuplas que contem todas as informações necessária para o banco
    informacoes = [
        ('Nome:', '_nome'), ('Email:', '_email'), ('CPF:', '_cpf'), ('Idade: ', '_idade'), ('Renda: ', '_renda'), ('Cadastrar', '_cadastro')
        ]
    configura_entradas(root, informacoes)

    
    root.mainloop()

cria_interface()