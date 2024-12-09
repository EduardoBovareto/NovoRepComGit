# Exercicio de valor de passagem por KM rodado
print(f'''
      
        Seja bem vindo ao calculo de Passagem  da Street!
        Seguiremos com o calculo abaixo!
      
     ''')
street = float(input('Qual a distancia em KM da sua viagem: '))
if( 50 <= street <= 200):
    print(f'O valor da sua passagem até 200 KM é de  com uma distancia de {street} KM é: R${75.80}')

elif(street > 200):
    print(f'O valor da sua passagem  e proporcional ao valor em KM, o valor é maior que 200 KM de distancia -> {street}. Valor: R${105.80}')
else:
    print(f'Nao realizamos viagens MENOR QUE 50 KM')