import random
valor = list(range(random.randrange(0, 12), random.randrange(25, 30)))
random.shuffle(valor)
print(valor)
# random.choices(valor, weights=[2, 30, 10], k = 3) Cada valor tem um peso de repetição dentro de weights
print(random.choices(valor, k = 3)) #K  representa a quantidade de valores selecionados.
# Sample faz coisas iguais a choices, só que sem os pesos de cada valor, só repete aleatoriamente, sem especificidade
print(f'{random.uniform(45, 57):.2f}') # Gera valores aleatórios do tipo float entre um range, aqui coloquei uma formatação de valores.
negativos = list(range(random.randrange(-40, -20), -1))
valor.extend(negativos) #extend adiciona um outro array no array principal.
print(valor)
valor.insert(0, 'String Sendo Adicionada em um determinada posição especifica')
print(valor)
