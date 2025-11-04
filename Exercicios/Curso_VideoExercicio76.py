print(f'{'Lista de Precos':-^40}')
print('-'*40)
# Exercício 76 - Lista de preços com tupla

listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
for i in range(0, len(listagem), 2):
    print(f'{listagem[i]:.<30}','R$', f'{listagem[i+1]:>7.2f}','\n',end=' ')

