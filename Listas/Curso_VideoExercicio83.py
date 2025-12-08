expression = input('Write a expression: ')
countrigth = 0
countleft = 0
while '(' and ')' not in expression:#two parameters for expression
    print('Its not valid expression, Please, repeat expression!')
    expression = input('Write a expression: ')
for string in range(0, len(expression)):
    if expression[string] == '(':
        countleft += 1

    elif expression[string] == ')':
        countrigth += 1

if countleft > countrigth:
    print(f'Its expression:{expression} not is valid, because missing parentheses:   {countleft - countrigth} )')

elif countrigth > countleft:
    print(f'Its expression:{expression} not is valid, because missing parentheses:   {countrigth - countleft} (')

else:
    print(f'The expression is confirm! {expression}')