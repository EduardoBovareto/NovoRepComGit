temp = a1 = int(input('Primeiro Termo: '))
r = int(input('Razao da PA: '))
count = 10
cond = True
termos = 10
while cond == True:
    if termos == 10:
        print(f'{a1}')

    else:
        #no branch main, o bloco do else esta inverso, posiicao correta!
        print(f'{temp}')
        temp += r #a partir do a1 se soma a razao em temp para imprimir

    #se estiver no primeiro termo ele emite a1, senao os temos e PAUSA quando termos == 1
    termos -= 1

    if termos == 0:
        termos = int(input('Quantos termos deseja mais? '))
        if termos == 0:
           print(f'Total de termos: {count}')
           cond = False
        
        if termos < 0: #impede o uso de termos negativos
            print('Favor digitar numero acima de 0!')
            termos = int(input('Quantos termos deseja mais? '))
            count += termos

        else:
            count += termos         
#Quando termo == 0 ele limita na hora o while e termina
#count que esta emitindo o valor errado, em 2 de diferença