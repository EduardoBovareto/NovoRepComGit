# Entender melhor este algoritimo!
num = int(input('Escreva um numero: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print(f'{unidade}, {dezena}, {centena}, {milhar}')

