from time import sleep
f = open('Notacoes/EvitarBuffer.txt', 'w')
f.reconfigure(write_through=True) #nao deixa ter buffer de texto
f.write('Validando sem buffer')
sleep(10)
print('Sem espera!')
f.write('Sem espera')
f.close()