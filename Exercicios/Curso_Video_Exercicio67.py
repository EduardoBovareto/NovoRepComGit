n = i = count =  0
while True:
    n = int(input('Write a value for multiplication table: '))
    if n < 0:
        break

    print(f'{'-'*20}')
    for i in range(0,11):
        print(f'{n} X {i} = {n * i}')
        count += 1

    print(f'{'-'*20}')
print('PROGRAM TABLE MULTIPLICATION  ENDED')
