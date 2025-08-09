temp = a1 = int(input('Primeiro Termo: '))
r = int(input('Razao da PA: '))
count = 0
cond = True
termos = 10
while cond == True:
    
    if termos == 10 and count == 0:
        print(f'{a1}')
        temp += r
        count += 1

    elif termos == 0:
        print('PAUSA!')
    
    else:
        print(f'{temp}')
        temp += r #a partir do a1 se soma a razao em temp para imprimir
        count += 1

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
         
#Quando termo == 0 ele limita na hora o while e termina
#count que esta emitindo o valor errado, em 2 de diferença