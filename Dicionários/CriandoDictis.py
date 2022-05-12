# Criando Dictionaris
dict1 = {
            'Primeiro': 1, 
            'Segundo': 2, 
            'Terceiro': 3
        } # Criando dicionário da forma simples de instância.
    
dict2 = dict(primeiro = 1, segundo = 2 ) # Criando com a função dict, assim como se cria listas com list()
print(dict2)

dict3 = dict(zip(['Salario', 'Bonus', 'Porcentagem'], [3000, 0.25, 75]))
print('\n', dict3)
# Criando Dicionario com a concatenação de objetos usando zip()
###################################################################################

print('\n\n', dict1['Primeiro']) # Acessando um dict
print('\n', dict3.get('primeiro')) # Acessando o dict com get() == "Pegar".
# Caso o valor passado na função get() nao exista ele retorna "None", Mas podemos definir uma mensagem caso essa chave não exista, ex:
print('\n', dict2.get('Salario', 'Não achamos isso na nossa base de dados!')) # Imprime o segundo parametro.

###########################################################################

dictPC = {
    'CPU': 'i5-3320M',
    'Fabricante': 'Intel',
    'Ano do PC': 2010,
    'RAM': '6G',
        }
print('\n', dictPC.keys()) # Sem parâmetro passado imprime todas as chaves do dict.
print('\n', dictPC.values()) # Sem parâmetro passado imprime todos os valores das chaves do dict.
#######################################################################################################

for chaves in dict3:
    print('A definição:', chaves, ', tem valor:', dict3[chaves]) # dict3[chaves] acessa a chave e retorna o valor.