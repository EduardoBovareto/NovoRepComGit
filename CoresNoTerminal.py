# Colocando cores no terminal
'''
    ANSI == Códigos dentro de um padrão que permite cores no terminal:
         \033[x; y; zm] == código padrão que nao muda

         - Dentro temos 3 parâmetros não obrigatórios e que variam
            (Under of the three parameters, not obrigated and that variable )
        x = Style
        y =  Text
        z = Background

        Valores possíveis para x (ESTILO:
                0, 1, 4 e 7:
                0 == Sem estilo
                1 == Negrito
                4 == Sublinhado
                7 == Negativo (Troca cor de fundo com background-color)
        
        Valores possíveis para y (LETRA):
                {
        white: 30
        Red: 31
        Green: 32
        Yellow: 33
        Blue: 34
        Purple: 35
        LightSkyblue: 36
        Gray: 37
        }  

        Valores possíveis para z (BACKGROUND):
        {
        white: 40
        Red: 41
        Green: 42
        Yellow: 43
        Blue: 44
        Purple: 45
        LightSkyblue: 46
        Gray: 47
        }    
'''
print('\033[4;36mTESTE\033[m') # Código ANSI, 1 == negrito, 31 vermelho a letra e fundo amarelo, se fecha a formatação com o código do ANSI