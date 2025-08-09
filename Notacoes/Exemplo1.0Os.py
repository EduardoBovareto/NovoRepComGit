import time
f = open('Notacoes/Texte1.0.txt', 'w') #abrindo arquivo, buffer padrao
f.write('Escrevendo primeira linha\n') #escreve no arquivo
print('Arquivo com acao realizada!')
time.sleep(5) # 5 segundos
f.flush()
print('Agora com flush')
time.sleep(15)
f.close()