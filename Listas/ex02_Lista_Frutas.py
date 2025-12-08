fruits = ["maçã", "banana", "laranja", "uva", "pera"]
fruits.append("manga")
print('\n',fruits)
fruits.remove("banana")
print('\n',fruits)
fruits.insert(1, "abacaxi")
print('\n', fruits)
print('Its in list!') if "uva" in fruits else print('Its not in list')
for fruit in range(0, len(fruits)):
    print(f'The fruit {fruits[fruit]} is in the position: {fruit}')
fruits.pop(0)
print(fruits)