#struct program
from tkinter import *
#piplow
#tkhtmlview
class Fa: #classe de um sistema de faculdade
    class Al: #Classe de um aluno novo
        def __init__(self):
            self.register = ''#Matrícula
            self.name = ''
            self.CPF = ()
            self.year = ''
            self.years_age = ''
    class Pr:
        
        pass

Aluno = Fa.Al 
Pr = Fa.Pr

#Colocar as funções para cada um e formulários para cada um deles de preenchimento de inputs
room = Tk()
class window:
    def __init__(self):
        self.root = room
        self.tela()
        self.root = self.root.mainloop() #Toda vez vai se gerar

    def tela(self):
        self.root.title('University System project ') #Titulo da janela
        self.root.geometry("1000x700") #muda tamanho padrao
        self.root.resizable(width=True, height=True) #Responsividadde para aumentar e diminuir o tamanho
        #sendo a largura True, podendo aumentar e diminuir, respeitando os tamanhos minimos e máximos.
        self.root.maxsize(width=1200, height=1200)#muda tamanho maximo
        self.root.minsize(width=500, height=400)#muda o tamanho minimo
        self.root.configure(background='SkyBlue1')#configura a janela, um deles é o fundo
        self.root.descript = Label(self.root, text='''Este sistema será destinado a uma organização de dados de uma faculdade que terá muitos dados e eventos.''', padx=10, pady=30,  background='LightSkyBlue1')
        #Cria um texto para se colocar na root, deve se colocar sempre primeiro a janeka Tk() depois a mensagem
        #padx e pady são os paddins nas direções x e y.
        self.root.descript.grid(column=10, row=5) #trabalha com as posições de coluna e de linha para o texto.
        #Em geral grid é um metodo que se referencia auma variavel.
        _butt = Button(self.root, text='Aluno', command=Pr, padx=10, pady=10)
        _butt2 = Button(self.root, text='Professor/Encarregado', command=Pr, padx=5, pady=5)
        _butt.grid(column=9, row=10, padx=20)
        _butt2.grid(column=10, row=10)

    def frames(self):
        self.frame = Frame(self.root) #inicia o fram dentro do atributo janela incial
window()


'''
toda vez que se inicia uma nova formatação ou uma nova classe ou até uma funcão, tem que se chamar self.(alguma coisa porvavelmente o nome do que se quer fazer) = self.root, porque ai se tem em referencia a janela instanciada e self recupera todos os atributos de room, pois self é uma referencia a janela instanciada, logo ao rodar, tudo será colocado em função de self.root == room.
'''