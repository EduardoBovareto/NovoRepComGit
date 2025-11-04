palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')
vogais_temp = ''
for i in palavras:
    for letras in i:
        if letras in vogais:
            vogais_temp += f'{letras} '
    print(f'Na palavra {i} temos {vogais_temp}')
    vogais_temp = ''