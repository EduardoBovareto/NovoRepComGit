peso_pessoa = float(input('Qual seu peso (Kg): '))
altura_pessoa = float(input('Qual sua altura (m): '))
imc = peso_pessoa / (altura_pessoa ** 2)

if imc < 18.5:
    print(f'Abaixo do peso! {imc:.2f}')

elif imc <=24.9:
    print(f'Parabéns!! Peso Normal com IMC = {imc:.2f}')

elif 25 <= imc  <= 29.9:
    print(f'Atenção!! Sobrepeso {imc:.2f}')

elif imc >= 30 and imc <= 34.9:
    print(f'Maior atenção!! Obesidade Grau 1 {imc:.2f}')

elif imc >= 35 and imc <= 39.9:
    print(f' Maior Atenção!!! Obesidade Grau 2 {imc:.2f}')

elif imc >= 40:
    print(f'Extrema Atenção!!!! Obesdade Grau 3 {imc:.2f}')

else:
    print(f'Favor reveja os valores enviado')