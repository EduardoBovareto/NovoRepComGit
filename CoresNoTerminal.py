# Colocando cores no terminal
'''
    ANSI == Códigos dentro de um padrão que permite cores no terminal:
         \033[x; y; zm] == código padrão que nao muda

         - Dentro temos 3 parâmetros não obrigatórios e que variam
            (Under of the three parameters, not obrigated and that variable )
        x = Style
        y =  Text
        z = Background

        Valores possíveis para x:
                0, 1, 4 e 7:
                0 == Sem estilo
                1 == Negrito
                4 == Sublinhado
                7 == Negativo (Troca cor de fundo com background-color)
        
        Valores possíveis para y:

                30(white),31 (red),32(green),33(yellow),34(blue),35(purple),36(Lightskyblue),37(gray).

        Valores possíveis para z:       
'''
print('\033[7;33;44m Teste\033[m') # Código ANSI, 1 == negrito, 31 vermelho a letra e fundo amarelo, se fecha a formatação com o código do ANSI