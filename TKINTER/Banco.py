import requests as rq
from tkinter import *
import tkinter as tk
from tkinter import messagebox as msg
import pygame as py
from PIL import ImageTk, Image

#cria a interface do banco
def Login():

    #cria a pagina de login
    login = tk.Tk()
    login.title('Login')
    login.geometry('480x450')

    container = Frame(login)
    container.grid(sticky='nsew')
    frame_secundario = tk.Frame()
    frame_secundario.grid(sticky='nsew', padx=80)

    arquivo_imagem = ImageTk.PhotoImage(Image.open('TKINTER/Materiais de codigo/icone.png'))
    mostra_image = Label(container, image=arquivo_imagem)
    mostra_image.grid( row=0, column=0, padx=10, pady=10)

    texto_intro = tk.Entry(frame_secundario, font=("Arial", 14, "italic"))
    texto_intro.grid(row=10, column=6, pady=40, ipady=80, ipadx=40)
    texto_intro.insert(0,'  Selecione uma categoria atual!')
    texto_intro.config(state='readonly')

    botao_cliente = Button(container, text='Cliente', command=lambda: cliente(frame_secundario))
    botao_cliente.grid(row=5, column=5, padx=20)
        
    botao_consultor = Button(container, text='Consultor', command=lambda: consultores(frame_secundario))
    botao_consultor.grid(row=5, column=4, padx=20)
  
    login.mainloop()

def realiza_dados(login_usuario, senha_usuario):
    login_usuario.delete(0, tk.END)
    senha_usuario.delete(0, tk.END)
    #gerenciamento de clientes

def cadastra_lead(lista):
    #mensagem de atenção na cadastro com som interativo
    msg.showinfo('CADASTRO DE LEAD', message='Cadastro realizado com sucesso')
    py.mixer.init()

    som = py.mixer.Sound('TKINTER/Materiais de codigo/correct-choice-43861.mp3')
    som.play()
    #carrega o arquivo de som para ser tocado

    #limpa campos escritos
    for i in range(len(lista)):
        lista[i].delete(0, tk.END)

def consultores(frame_secundario):
    limpa_widgets(frame_secundario) 

    Title = Label(frame_secundario, text='Nelson Bank', font=('Arial', 20))
    Title.grid(row=5,column=3, padx=5, pady=30)
    usuario = Label(frame_secundario, text='Usuário:', font=('Arial', 10))
    usuario.grid(row=20, column=2, padx=10)

    login_usuario = Entry(frame_secundario,border=2)
    login_usuario.grid(row=20, column=3, pady=20)
    login_usuario.get()

    senha = Label(frame_secundario, text='Senha:', font=('Arial', 10))
    senha.grid(row=22, column=2, pady=20, padx=10)

    senha_usuario = Entry(frame_secundario, border=2)
    senha_usuario.grid(row=22, column=3, pady=20)
    senha_usuario.get()

    entrar = Button(frame_secundario, text='Login', command=lambda:cria_interface(login_usuario, senha_usuario))
    entrar.grid(row=24, column=3, pady=20)

def cliente(frame_secundario):
    limpa_widgets(frame_secundario)

    Title = Label(frame_secundario, text='Nelson Bank (Clientes)', font=('Arial', 20))
    Title.grid(row=5,column=3, padx=5, pady=30)

    usuario = Label(frame_secundario, text='Email:', font=('Arial', 10))
    usuario.grid(row=20, column=2, padx=10)

    login_usuario = Entry(frame_secundario,border=2)
    login_usuario.grid(row=20, column=3, pady=20)
    login_usuario.get()

    senha = Label(frame_secundario, text='Senha:', font=('Arial', 10))
    senha.grid(row=22, column=2, pady=20, padx=10)

    senha_usuario = Entry(frame_secundario, border=2)
    senha_usuario.grid(row=22, column=3, pady=20)
    senha_usuario.get()
        
    entrar = Button(frame_secundario, text='Login', command=lambda: realiza_dados(login_usuario, senha_usuario))
    entrar.grid(row=24, column=3, pady=20)

def limpa_widgets(frame_secundario):
    widgets = frame_secundario.winfo_children()
    for widgets in frame_secundario.winfo_children():
        widgets.destroy()
    
def configura_entradas(window, campos):
    nome = email = cpf = Idade = renda = None
    lista = [nome, email, cpf, Idade, renda]

    #entradas do sistema
    for i, (texto, tipo) in enumerate(campos):
        Label(window, text=texto).grid(row=i + 1, column=5, pady=20, padx=3)
        #valores vazios sao coletados no getr como strings

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
            if Idade and renda == str:
                return
            else:
                if Idade and renda == int:
                    msg.showerror('Atenção','Os valores informados devem ser números')
                
            
            #botao que cadastra os leads
            Button(window,text='Cadastro', command=lambda: cadastra_lead(lista)).grid(row=i + 1, column=6, pady=10, padx=1)
        #lambda permite argumentos das entradas

def imagem(frame, imagem):#mostra imagem
    mostra_imagem = Label(frame, image=imagem)
    mostra_imagem.grid(row=0, column=0, sticky='nsew', padx=30, pady=30)

def cria_interface(login_usuario, senha_usuario):
    #realiza limpeza das Entrys
    login_usuario.delete(0, tk.END)
    senha_usuario.delete(0, tk.END)

    #cria a interface secundaria
    root = tk.Toplevel()
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
    my_image = ImageTk.PhotoImage(Image.open('TKINTER/Materiais de codigo/icone.png'))
    imagem(frame, my_image)
    
    #array de tuplas que contem todas as informações necessária para o banco
    informacoes = [
        ('Nome:', '_nome'), ('Email:', '_email'), ('CPF:', '_cpf'), ('Idade: ', '_idade'), ('Renda: ', '_renda'), ('Cadastrar:', '_cadastro')
        ]
    
    configura_entradas(frame, informacoes)
   
    #fecha a janela principal
    fecha_janela = tk.Button(frame, text='Finalizar', fg='white', bg='black', command=root.destroy)
    fecha_janela.grid(row=14, column=0, pady=100, padx=10)

    root.mainloop()

Login()
