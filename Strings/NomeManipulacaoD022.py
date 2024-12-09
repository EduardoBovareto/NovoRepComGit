import emoji as em
#escalonar para criação de possiveis emails
nome = str(input('Qual o seu nome: '))
#E importante deixar claro os tipos de dados

nome = nome.strip() #Retira os espaços desnecessarios, pode ser colocado direto no input
total_letters = len(nome) - nome.count(' ') #A quantidade de letras e o total menos os espaçoc
space = nome.find(' ')
First_n = nome[:space] #Guarda a string do inicio ate o endereco de space - 1
separa = nome.split(' ')

print(f'''
        Seja bem vindo {nome}, seguiremos com as analises do seu nome:
    Seu nome em Maiusculo: {nome.upper()} {em.emojize(":backhand_index_pointing_up_dark_skin_tone:")}

    Seu nome em minusculo: {nome.lower()} {em.emojize(":backhand_index_pointing_down_dark_skin_tone:")}

    O total de Letras e: {total_letters} caracteres! {em.emojize(":globe_showing_Asia-Australia:")}

    Total de espaços do seu nome: {nome.count(' ')}

    Seu primeiro nome tem {len(First_n)} letras

    Analisando, seu nome e constituido por: {separa}
     ''')
