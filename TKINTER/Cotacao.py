import requests
import tkinter as tk

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

j_cotacoes = tk.Tk()
j_cotacoes.title('Cotações Atualizadas')
j_cotacoes.geometry('400x400') #nao usar x em caixa alta

Frame = tk.Frame(j_cotacoes)
Frame.pack(fill='both', expand=True)

Atualiza_cotacao = tk.Button(j_cotacoes, text='Atualizar Cotações', command=pegar_cotacoes)
Atualiza_cotacao.pack(pady=50)

label = tk.Label(j_cotacoes, text='', background=None, width=None)
label.pack()

canvas = tk.Canvas(j_cotacoes)
canvas.pack(fill='both', expand=True)


j_cotacoes.mainloop()