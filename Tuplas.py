cliente = input('Informe o cpf do individuo, separado por ponto').split(".")
nome = input(' Fale seu nome')
for i in range(len(cliente)):
    cliente[i] = int(cliente[i])
tupla = (nome, cliente)
print(type(tupla)) # Ainda não está sendo considerado como tuple, mudar
print(tupla)
# for i in tupla:
#     print(i,end = '.')