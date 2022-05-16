# AD2-2 16/05 2022 Eduardo Bovareto Matrícula:21213050280
Arquivo = input('Digite o nome do Arquivo; ') # Sempre será casrtoes.bin
Arquivo += '.bin'
cartao = input('Escreva o nome da sua Bandeira: ') # Informa o cartao usado

informacoes = open('codigo.txt', 'w') # Abre o arquivo a ser codificado
lista = ['Visa#', '123.90\n', 'Mastercard#', '245.45\n', 'Diners#', '367\n', 'Elo#', '532\n']

for infos in lista:
    informacoes.write(infos)
informacoes.close()
with open(Arquivo,'w'):
   pass