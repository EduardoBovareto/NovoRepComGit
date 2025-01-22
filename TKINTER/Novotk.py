import tkinter as tk
#from tkinter import colorchooser as co #classe de escolha de cor
#from tkinter import filedialog as fil
from tkinter import messagebox as msg

def Cadastro():
    msg.showinfo(title='Cadastrado', message='Cadastro realizado')

def Nova_tela(): #argumento usado
    texto = caixa.get() #pega o valor digitado na caixa de texto
    caixa.delete(0, tk.END) #limpa caixa de texto, o botao esta chamando esta função

    tela_new = tk.Toplevel() #cria uma nova janela num nivel acima da outra anterior
    #tela_new = tk.Tk() #tela de boas vindas
    tela_new.title('Nova tela do sistema')
    tela_new.geometry('900x440')

    #ao fechar a janela anterior, ela fecha a nova

    lb = tk.Label(tela_new, text=(f'Seja bem vindo {texto}')) #novo label
    lb.pack()

    texto_email = tk.Label(tela_new,text='Email: ')
    texto_email.place(x=50, y=50)

    email = tk.Entry(tela_new)
    email.place(x=100, y=50)

    caixa_e = email.get()
    #Pega_texto(caixa_e)

    botao2 = tk.Button(tela_new, text="Cadastrar", command=Cadastro)
    botao2.place(x=300, y=50)

    botat3 = tk.Button(tela_new, text='Fechar', command=tela_new.destroy)
    botat3.place(x=50, y=400)

    #cores = co.askcolor() #abre um layout de escolha de cor
    #fil.askdirectory() gera uma tela para carregar arquivos

    tela_new.mainloop()

def Botao_Executa(): #função que integra as duas telas criadas
    Nova_tela()
   
    #esta com problema de abrir varias telas apos apertar o botao

    #lb.config(text=f'{texto}'), isso muda o texto primario criado anteriormente

root = tk.Tk() #janela raiz que é iniciada pela classe Tk do tkinter
root.title('Primeira tela!')
root.geometry('800x420') #tamanho da tela (Largura e Altura)

frame = tk.Frame(root) 
#serve para organizar na tela os widgets e etc, para organizar a tela
frame.pack(fill='both')

canvas = tk.Canvas(root) 
#serve para mostrar rolaveis e tamanho maiores do que cabe na tela, imagens e etc.
#para mostrar coisas graficas na tela
canvas.pack(side='left', fill='both', expand=True)

scrollbar = tk.Scrollbar(frame, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')
canvas.configure(yscrollcommand=scrollbar.set)
#yscrollcommand=scrollbar.set- configura a barra de rolagem para que quando seja clocado,dentro do canvas o movimento aconteça, configura o movimento

content_frame = tk.Frame(canvas)
content_frame.update_idletasks()

canvas.create_window((50,80), window=content_frame, anchor='nw')
#anchor define a ancoragem do widget,a noroeste, nw
for i in range(50):
    tk.Label(content_frame, text=f"Item {i+1}").pack()
canvas.config(scrollregion=canvas.bbox('all'))
#scrollregion= orienta o canvas perante ao widgets que estao dentro
#bbox() passa as coordenadas de onde começa e termina o texto para que
#scrollregion= receba essas coordenadas e orienteo canvas

lb = tk.Label(root,text='Digite algo: ') #cria o texto na tela
lb.pack(padx=10, pady=10) #configura a margin do texto
lb.place(x=50, y=50) #muda a posicao do texto em x e y

caixa = tk.Entry(root) #cria a caixa de texto na tela
caixa.place(x=150, y=50) #orienta a posição da caixa de texto
#caixa.pack(padx=50, pady=20) #pack() sempre ira mostrar na tela o objeto criado

botao = tk.Button(canvas, text='Mostrar Texto', command=Botao_Executa)
#botao esta dentro do container que o engloba
#command= realiza a funcao que o botao tera, e a utilidade do botao
botao.place(x=200, y=50)
botao.pack(pady=50)


root.mainloop() #faz com que a janela fique aberta ate ser fechada