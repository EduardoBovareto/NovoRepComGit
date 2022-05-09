Arquivo = open("C:\\Users\WINDOWS\\Desktop\\JS\\Python-temporário\\AD2-1\\teste.txt", "r") # Abrindo um aquivo só para leitura

# print("\n METODO READ read()\n")
# print(Arquivo.read(), end = "  ") # Le o arquivo todo

# Arquivo.seek(0) #Volta o ponteiro do arquivo lido para a primeira linha
# # Sem voltar o ponteiro a leitura não acontece, a leitura é orientada ao ponteiro do arquivo
# # Logo se precisa voltar no inicio para ler linha a linha

# print("\n METODO READLINE readline()\n")
# print(Arquivo.readline(), end = " ") # Primeira linha

# Arquivo.seek(0)
# print(Arquivo.readlines(), end = " ") # Printa e le todas as linhas dentro de uma lista []
# Arquivo.close() # Fecha a conexão com o arquivo

# Outra maneira de printar um arquivo
# counter = 0 # Contador de linhas
# for linha in Arquivo:
#     linha = linha.rstrip() # Elimina os espaços do print
#     counter += 1
#     print(linha)
# Arquivo.close
# print('O numero de linhas é: ', counter)


# counter de linhas que tem a palavra Python
counter = 0
for linhas in Arquivo:
    if "Python" in linhas:
        print(linhas)
        counter += 1
print(counter)
Arquivo.close()