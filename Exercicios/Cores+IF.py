def Mostracerto(v1, v2):
    s = v1 + v2
    if(s < 10):
        return f'The sun is \033[7;42mAlgarism unicode! {s}\033[m'
    else:
        return f'The sun in \033[7;41mmore 10 algarisms {s}\033[m'
num1 = int(input('Write a number: '))
num2 = int(input('Write a other number: '))
print(Mostracerto(num1, num2))