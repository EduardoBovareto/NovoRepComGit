from time import sleep
f = open('Notacoes/Buffer0.txt', 'wb',buffering=0)
f.write(b'Sem buffer\n')
sleep(5)
f.write(b'SEM espera')
f.close()