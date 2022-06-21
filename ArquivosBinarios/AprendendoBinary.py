arq = open('ArquivoBi.bin', 'wb')
Numero = int(input('Informe um numero inteiro: '))
arq.write(Numero.to_bytes(2, byteorder='little', signed=True))
Numero = Numero.to_bytes(2, byteorder='little', signed=True) #Armazenando numero convertido em bytes
x = int.from_bytes(Numero, byteorder='little', signed=True) #Convertendo para decimal novamente o numero convertido em bytes
print(x)
arq.close()
#to_bytes sempre converte de valores inteiros para bytes dentro de uma quantidade
#to_bytes(Quantidade de bytes, byteorder=Organização de uso de espaço de memória, #signed=Se tem sinal ou não)
#Em casos de não saber a quantidade de bytes que se tem que usar, podemos usar métodos
#da própria linguagem para  saber isso. Ex:
Number = 1000
print(int.bit_length(Number)) #Retorna a quantidade de bits necessario para representacao
