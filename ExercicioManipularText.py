name = input('Digite seu nome completo').strip()
print('Analisando seu nome...\n\n')
print('your name in Upper case is: {}'.format(name.upper()))
print('your name in Lower case is: {}'.format(name.lower()))
print('your name have in all: {} lettles'.format(len(name) - name.count(" ")))
posi = name.find(" ") # return an number of the position
FirstName = name[:posi]
lengthName = len(FirstName)
print('your first name is: {},  and him have {} lettles'.format(FirstName, lengthName))
PartsName = name.split()
print('Your name have contituation of the: {}'.format(PartsName))