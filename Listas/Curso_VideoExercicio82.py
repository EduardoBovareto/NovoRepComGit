flag = ''
number = 0
temp = []
pair = []
odd = []
while True:
    number = int(input('Write a number: '))
    if number in temp:
        print('Its number already exist in list')

    else:
        temp.append(number)#Complete List

    if (number % 2 == 0) and number not in pair:
        pair.append(number) #number pair

    if number % 2 != 0 and number not in odd:
        odd.append(number) #number odd

    flag = input('Do you want continue? S/N').upper()
    while flag not in 'N S':
        flag = input('Error! Write if do you want continue? S/N').upper()
    if flag == 'N':
        break

print(f'''\nThe complete list is: {temp}\n The pairs numbers list is: {pair}\n
The list odd numbers is: {odd}''')
