n =  i =  porcent =  count = 0
escolha = ''
while True:
    n = int(input('Write a number: '))
    porcent += 1 if n % 2 == 0 else 0 #caso seja par
    count += 1 #total de numeros digitados

    for i in range(0,11):
        print(f'{n} X {i} =  {n * i} ')

    escolha = input('You want see other multiplication table of number: [sim-não]').lower()
    while escolha not in ['sim', 'não']:
        escolha = input('You want see other multiplication table of number: ').lower()
    if escolha  == 'não': break
    
print(f'''The percentage even values is: {(porcent * 100) / count}%
      In total {count} values --Program ended''')