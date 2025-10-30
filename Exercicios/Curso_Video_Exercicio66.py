n = s = cont = 0
temp = ''
while True:
    n = int(input('Write a number: '))
    if n == 999:
        break
    cont += 1 #nem a contagem nem a soma deve estar antes do if
    s += n
    temp += str(n) + ' ' #string com os numeros
print(f'the sun is it: {s}, the total numbers of values entered: {cont},values: {temp}')