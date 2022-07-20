import random as rd #Importa Random e da um nome para ele aqui dentro
import datetime as dt #Importa e da um nome para ele aqui dentro
#SUBPRIGRAMA
def configura_email(palavra = 'Email', SV = 'Gmail'):
    temp = f'@{SV}.com'
    if len(palavra)  == 3: #Caso de ter array  de 3 elemntos
        palavra[-1] = None
        i = 0
        while i != -1:
            Email = palavra[i] + '.' + palavra[i + 1] + temp
            i += 1
            if palavra[i + 1] == palavra[-1]:
                i = -1
                return Email, print(f'''Email formado: {Email} \n Registro de Cadastro: {dt.datetime.now()}''')
                #dt é o modulo datetime da classe datetime e que tem o metodo now() de agora
            else:
                continue
    
    elif len(palavra) == 2:
        Email = palavra[0] + '.' + palavra[1] + temp
        return Email, print(f'''Email formado: {Email} \n Registro de Cadastro: {dt.datetime.now()}''')
        #dt é o modulo datetime da classe datetime e que tem o metodo now() de agora

    else:
        Email = palavra[0] + temp
        return Email, print(f'''Email formado: {Email} \n Registro de Cadastro: {dt.datetime.now()}''')
        #dt é o modulo datetime da classe datetime e que tem o metodo now() de agora
    
    return None
#PROGRAMA PRINCIPAL
info = input('Informe seu nome ou uma palavra: ').split()
Server = [ 'Outlook', 'Gmail', 'Yahoo']
Server = rd.choice(Server) #Escolhea aleatóriamente um server

if len(info) == 2 and info[0] == ' ':#Caso de só ter um espaço
    info = None
    configura_email()
else:
    configura_email(info, Server)
