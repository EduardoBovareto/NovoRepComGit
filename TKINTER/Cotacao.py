import requests
import tkinter as tk
from tkinter import messagebox as msg

# Função para pegar cotações
def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}
        '''
    
    label['text'] = texto
    label['background'] = 'yellow'
    label['width'] = 30

# Função para limpar a Entry
def limpar_entry():
    entrada.delete(0, tk.END)
    info = msg.showinfo('ATENÇÃO', message='Email enviado com sucesso!!')

# Configuração da janela principal
j_cotacoes = tk.Tk()
j_cotacoes.title('Cotações Atualizadas')
j_cotacoes.geometry('480x430')
j_cotacoes.rowconfigure(0, weight=2)
j_cotacoes.columnconfigure(0, weight=1)

# Criação do Frame
Frame = tk.Frame(j_cotacoes, height=1000)
Frame.grid(row=0, column=0, sticky='nsew')

# Texto inicial
Info_cotacao = tk.Label(Frame, text='Clique no botão para pegar cotações!')
Info_cotacao.grid(row=1, column=8, pady=30, padx=50)

# Botão para atualizar cotações
Atualiza_cotacao = tk.Button(Frame, text='Atualizar Cotações', command=pegar_cotacoes)
Atualiza_cotacao.grid(row=5, column=8, pady=50)

# Label para exibir cotações
label = tk.Label(Frame, text='', background=None, width=None)
label.grid(row=3, column=8)

# Campo de entrada (Entry)
entrada = tk.Entry(Frame, width=30)
entrada.grid(row=8, column=8, pady=10)

# Botão para limpar a Entry
botao_limpar = tk.Button(Frame, text='Mandar Email', command=limpar_entry)
botao_limpar.grid(row=10, column=8, pady=10)

# Loop principal da interface
j_cotacoes.mainloop()
