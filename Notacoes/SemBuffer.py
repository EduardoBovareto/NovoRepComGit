from time import sleep
f = open('Notacoes/SemBuffer.txt', 'w') #buffer de texto presente, manual
print('Iniciaremos a escrita no documento!')
f.write('Escrevendo primeiras linhas')
sleep(10) #aplicando 10 segundos para ver o flush manual

print('usando flush agr')
f.flush() #forca a mudanca de buffer de texto para bytes
print('flush realizado')
f.close()