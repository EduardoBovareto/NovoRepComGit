import emoji as em
nome = input('Qual o seu nome: ')
nome = nome.strip() #Retira os espaços desnecessarios
total_letters = len(nome) - nome.count(' ') #A quantidade de letras e o total menos os espaçoc
space = nome.find(' ')
First_n = nome[:space - 1]
print(f'''
        Seja bem vindo {nome}, seguiremos com as formas do seu nome:
    Seu nome em Maiusculo: {nome.upper()} {em.emojize(":backhand_index_pointing_up_dark_skin_tone:")}

    Seu nome em minusculo: {nome.lower()} {em.emojize(":backhand_index_pointing_down_dark_skin_tone:")}

    O total de Letras e: {total_letters} caracteres! {em.emojize(":globe_showing_Asia-Australia:")}

    Total de espaços do seu nome: {nome.count(' ')}
     ''')
