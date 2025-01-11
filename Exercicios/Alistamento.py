from datetime import date
atual = date.today().year #year é um atributo de atual {atual.year}
#date.today() cria um objeto que e chamado de data e ao guardar isso nao se tem os 
# atributos mas sim o objeto, tem se que solicitar o ano

print(f'Bem vindo ao \033[2;42mAlistamento\033[m Rio das ostras {atual}')
ano = int(input('Escreva seu ano de nascimento: '))
ali = atual - ano

if (ali == 18):
    print(f'\n\nParabéns!! Seu alistamento é dentro deste ano de 2025, você tem {ali} anos\n\n')
    mes = int(input('Qual o numero do mes que você nasceu: '))

    if(mes > 1):
        print('\n\033[2;41mProcure ver o alistamento LOGO\033[m, Pois ja esta se passando o prazo.\n\n')
    elif(mes == 1):
        print('\n \033[2;42mEsta no prazo correto de solicitação\033[m')

elif(ali > 18):
    print(f'Idade além do parâmetro para alistamento. você tem : {ali} anos\n')
    anos_atras = ali - 18
    alistamento_antigo = atual - anos_atras
    print(f'Seu alistamento ja deveria ter acontecido {anos_atras} anos atras\n\n')
    print(f' Ele ocorreu provavelmente em {alistamento_antigo}')

else:
    print(f'\nAinda não esta na hora de se alistar! você tem {ali} anos, lhe faltam {18 - ali} para se alistar')