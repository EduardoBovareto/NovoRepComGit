import time
f = open('Notacoes/Texte1.1.txt','w')
f.reconfigure(write_through=True) #nao ha buffer de texto intermediando apenas buffer de bytes
f.write('Validando escrita')

time.sleep(10)
f.write('Outra coisa')
f.close()