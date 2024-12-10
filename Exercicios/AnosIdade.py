idade = int(input('Escreva sua idade: '))
if(idade <= 12):
    print('E criança')
elif(idade <= 17):
    print('E Adolescente')
elif(idade <= 59):
    print('Adulto')
else:
    print('Jovem senhor')