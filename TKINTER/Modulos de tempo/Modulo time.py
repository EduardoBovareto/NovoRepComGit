import time
Lista = (time.asctime()).split() #O Horario local da minha regiao de forma geral
print(Lista) 
print(Lista, f'A hora é: {Lista[3]}')
print(time.localtime()) #O Horario local da minha regiao bem mais específico com mais detalhes
print('CONTE 5 SEGUNDOS!!')
time.sleep(5) #cConta 5 segundos
print('contou 5')
if 'a' in 'eDUaRDO':
    time.sleep(10)
    print('Tem a letra a e contou 10s')