# Estrutura de abertura de Arquivos
'''
Abertura sem o with:
    Arquivo.open("nomeDoArquivo", "w")
    Arquivo.close()
Veja que é necessário fechar o arquivo, se eu usar o .write ali no meio,
e der erro, pode acontecer de o arquivo ainda ficar aberto, por isso se usa
o with
'''

# Com o with:

Arquivo = open("Meu_Arquivo.txt", "w") 
with open("Meu_Arquivo.txt", "w") as arquivo:
    Arquivo.write('Escrevi usando write')
# Significa basicamente, com o arquivo aberto e armazenado
#   em "arquivo", iremos fazer algo

# Quando termina de exzecutar a linha do with ele ja fecha
# o Arquivo.
