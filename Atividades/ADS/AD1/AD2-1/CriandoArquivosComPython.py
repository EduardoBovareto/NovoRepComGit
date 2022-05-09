Ab = open('AD2-1\\arq01.txt', 'r+')
Ab.write("Boson Treinamentos")
# Nao aceita esse comando : Ab.read() com o modo de abertura == "w" pois o modo é sóde escrita
print(Ab.read())
# Arquivo.name retorna o nome do arquivo
# Ab.mode Retorna o modo de operaç!ao em relação ao arquivo
Ab.close()