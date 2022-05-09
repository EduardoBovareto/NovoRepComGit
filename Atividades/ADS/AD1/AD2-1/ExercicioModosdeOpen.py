'''
Criaremos 4 arquivos, cada um com seu modo de operação e funcionalidade
'''
Arquivo01 = open('AD2-1\\Arquivo01.txt', 'r') # Modo de leitura, precisa existir ja
print(Arquivo01.read())
Arquivo01.seek(0)
print(Arquivo01.readline())
Arquivo01.close()

print('\n{}\n'.format("="*30))

Arquivo02 = open('AD2-1\\Arquivo2.txt', 'w') # Cria o arquivo
Arquivo02.write('Escrevendo pela primeira vez no arquivo')
Arquivo02.write('Metodo de apenas escrita em um arquivo')
Arquivo02.close()

print('\n{}\n'.format("="*30))

Arquivo03 = open('AD2-1\\ Arquivo3.txt', 'a') # Deve especificar se for colocar dentro de uma pasta, esse modo adciona conteudo a um arquivo existente ou inexistente
Arquivo03.write('Escrevendo pela linguagem o conteudo desse arquivo')
Arquivo03.write('Escrevendo pelo metodo de escrita leitura na  linguagem, sendo o conteudo visivel')

print('Criado o arquivo:', Arquivo03.name)
Arquivo03 = open('AD2-1\\ Arquivo3.txt', 'r')
print(Arquivo03.read())
Arquivo03.close()
# No caso acima, estou pegando um arquivo existente criado ja e adicionado conteudo pelo modo a e colocando ele dentro de uma variavel para ler ele, eu posso fazer essa jogada para ler, pois o modo a n deixa, no r deve se usar o read