import datetime
import time
def  pega_data():
    data = time.asctime().split()
    # print(data)
    for i in data: #Retira o horário
        if ':' in i:
            data.remove(i)
    # print(data)

pega_data()
Hoje = datetime.date.today() #Pega a data de hoje
# print(datetime.date.today()) #Faz o mesmo papel do que está em pega_data

#Criando uma Data
data2 = datetime.date(2022, 7, 14)#Se cria no código uma hora
#print(data2)
# print(data2.ctime()) #Formatacao diferente de data na forma de string
data3 = data2.ctime().split() #Pega a formataçao que foi gerada e gera um array, acessando ele
# print(data3[:2])

#Acessos de datas
dia = data2.day 
# print(data2.day) #Acessando a propriedade  day da sub classe date
mes = data2.month
# print(data2.month) #Acessando a propriedade  month da sub classe date 
ano = data2.year
# print(data2.year) #Acessando a propriedade  year da sub classe date


#Alterando dados na data

dia = data2.replace(day=15) #Altera o atributo day do objeto data2 de classe datetime.date
# print(dia), Podemos fazer isso também com month e year