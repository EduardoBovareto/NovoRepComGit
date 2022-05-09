nInt = int(input('Informe um inteiro'))
if nInt < 0 or nInt > 100:
    print('VALOR FORA DE RANGE N(0 < N < 100)!')
    while nInt < 0 or nInt > 100:
        nInt = int(input('Favor Reemitir um valor inteiro'))