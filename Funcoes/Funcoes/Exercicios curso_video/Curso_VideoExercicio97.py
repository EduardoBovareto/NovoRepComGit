def escreva(Texto):
    print(f'{'~' *len(Texto)}')#imprime as linhas 
    print(Texto)
    print(f'{'~' *len(Texto)}')


#Programa principal
mensagem = str(input('Escreva uma mensagem: '))
escreva(mensagem)