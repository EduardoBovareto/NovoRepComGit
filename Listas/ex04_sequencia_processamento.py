numbers = input('Write a values sequence: ').split(',')
numbers = list(map(int, numbers))
no_repetition = list(set(numbers))
#print(no_repetition, 'Repetition', numbers)
#print(type(numbers[0]))
for indice in range(0, len(no_repetition)):
    print(f'The number:{no_repetition[indice]} appears in the list',numbers.count(no_repetition[indice]))