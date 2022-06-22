from random import randint
import struct
#SUBPROGRAMA
def ProcesssaCaracteristicas(I, N, A, C):
    NomeEmByte = N.encode()
    CEmByte = C.encode()
    BlocoCarac = struct.pack(f'{len(N)- 1}s {len(C) - 1}s I f', NomeEmByte, CEmByte, I, A)
    print(BlocoCarac)
    print(struct.unpack(f'{len(N)- 1}s {len(C) - 1}s I f', BlocoCarac))
    return None

#PROGRAMA PRINCIPAL
Idade = randint(0, 35)
Nome = 'Eduardo'
Altura = 1.75
Comida = 'Lasanha'
ProcesssaCaracteristicas(Idade, Nome, Altura, Comida)