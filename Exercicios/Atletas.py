from datetime import date as dt
ano_atual = dt.today().year #coleta o ano atual
ano_nasc = int(input('Ano de nascimento: '))
idade_atleta = ano_atual - ano_nasc
print(f'\n\n Idade hoje no ano de {ano_atual} e: {idade_atleta} anos \n')

if(idade_atleta <= 9):
    print('\n \033[0;40mMIRIM\033[m')

elif(idade_atleta <= 14):
    print('\n \033[1;41mINFANTIL\033[m')

elif(idade_atleta <= 19):
    print('\n  \033[2;42mJUNIOR\033[m')

elif(idade_atleta <=  25):
    print('\n \033[3;43mSENIOR\033[m')

else:
    print('\n \033[4;44mMASTER\033[m')