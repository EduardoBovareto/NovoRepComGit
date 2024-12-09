nome = str(input('Escrava um nome: ')).strip().upper()
qtd = nome.count('A')
posIni = nome.index('A')
posFinal = nome.rfind('A')
if nome[0] == 'A':
    print(f'''
            Esta palavra começa com a letra A'
            A posição inicial da letra A é {posIni}
            A ultima ocorrencia da letra é {posFinal}
        ''')
else:
    print(f'''
            Esta palavra não começa com a letra A
            A posição inicial da letra A é {posIni}
            A ultima ocorrencia da letra é {posFinal}
          ''')
    
