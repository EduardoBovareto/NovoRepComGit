vogais = ('a', 'e', 'i', 'o', 'u' )# Vogais
counter = 0 # Contador de constantes
Caracteres = input('Informe uma palavra:')# Cadeia de caracteres a ser analisada
if len(Caracteres) > 10: # Condição mínima para a palavra
    Caracteres = input('É necessário que a palavra tenha no máximo 10 letras:')# Cadeia de caracteres a ser analisada
    while len(Caracteres) > 10:
        Caracteres = input('É necessário que a palavra tenha no máximo 10 letras:')# Cadeia de caracteres a ser analisada
Caracteres.strip()
consoantes = []
for i in Caracteres:
    if (i in vogais) == False:# Caso onde não há consoantes
        counter += 1
        consoantes.append(i)# Colocando as consoantes para printar
consoantes = tuple(consoantes)
print(f'Estas são as consoantes presentes\ndentro da palavra digitada:{consoantes}')
