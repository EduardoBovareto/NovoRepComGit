# São listas com rótulos, nas listas normais, se tem índices de identificação, nos dicionários temos rótulos, nomes que identificam cada agrupamente dessa lista que é o dicionário. 

# É uma estrutura de dados e um objeto que suporta informações no modelo chave e valor. É realmente uma lista com nome de cada valor, uma identificação de cada valor.

emails = { # criando o dicionario
    'Eduardo': 'Firma@gmail.com',
    'Maria': 'Suatia3@Outlook.com',
    'Marcos': 'MarcosAnt@yahoo.com',
}
print(emails['Eduardo']) # printando e acessando uma determinada chave.
emails['Lebron'] = 'Leon@gmail.br' # Adiciona uma nova posição com seu valor
print(emails)
#################

# Pegando todas as chaves do dicionario:
for chaves in emails:
    print(chaves) # printa todas as chaves do dicionario
    print(emails[chaves]) # chaves assume cada valor de chave do dicionario e emails[chaves] pega cada posição que assume a var chaves e mostra eles.
    # Podemos pegar esses valores através da função "emails.value()".

# Usando .keys()
# Se coloca emails.keys() dentro de um print, pois, .keys retorna todas as chaves.

# Retirando uma chave-valor:
emails.pop('Eduardo') # Retira a chave e valor 'Eduardo'
print(emails)
