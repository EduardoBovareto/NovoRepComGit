import time
f = open('Notacoes/Texte1.0.txt', 'w') #abrindo arquivo, buffer padrao
f.write('Escrevendo primeira linha\n') #escreve no arquivo
print('Arquivo com acao realizada!')
time.sleep(5) # delay de 5 segundos
f.flush() 
#flush() limpa o buffer do python que neste caso e de texto e forca o python a passar os dados para o buffer binario
print('Agora com flush')
time.sleep(15)
f.close() #finaliza o arquivo para garantir a escrita

#o tempo de delay permite ver a escrita acontecendo