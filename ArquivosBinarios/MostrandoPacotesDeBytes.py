import random
import struct
numero = random.randint(0, 130)
print(f'O numero é : {numero}')
BlocoEmBytes = struct.pack('i', numero)
print(f'\nO numero {numero} virou em bytes {BlocoEmBytes} e para provar : {type(BlocoEmBytes)}\n')
BlocoConvertido = struct.unpack('i', BlocoEmBytes)
print(f'\n A forma contrária e convertida para integer  do que estava assim: {BlocoEmBytes}, é assim {BlocoConvertido} ')
Decodificado = BlocoEmBytes.decode('utf-8')
print(f'Aqui pegamos o que era {type(BlocoEmBytes)} e usamos o padrão de decodificação "UTF-8", para converter direto em string que fica assim:{Decodificado}')
print(Decodificado, f'O seu tipo {Decodificado}')
'''
Nesse caso de decode, temos que um valor que era inteiro na forma de bytes foi convertido para uma forma em string e que se decodificado representa algo totalmente diferente, pois não foi convertido ou desempacotado para integer

Pack e unpack fazem a ponte de converter aquilo em integer em bytes e vice versa, logo, não se deve decodificar ou codificar direto sem se ter a conversão de pack ou unpack
'''