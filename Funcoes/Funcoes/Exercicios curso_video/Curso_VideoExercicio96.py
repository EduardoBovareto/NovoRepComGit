def area(compr, larg):
    areatt = compr * larg
    print(f'Medidas do terreno: Comprimento: {compr} m X Largura: {larg} m')
    print(f'Area total: {areatt} m²')


print(f'\n\n{'Controle de terrenos':^30}')
print('-'*30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(comprimento, largura)