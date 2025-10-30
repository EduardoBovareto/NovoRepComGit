n = sun = count = count_pares =  0
while True:
    n = int(input('Write a value integer: '))
    if n == 0: break #funciona tambem desta maneira
    sun += n if n % 2 == 0 else 0 #soma valores pares
    count_pares +=1 if n % 2 == 0 else 0 #soma a quantidade de valores pares
    count += 1
print(f'''Foram digitados {count} numeros, desses {count_pares} sao pares, 
totalizando uma soma de:{sun}''')