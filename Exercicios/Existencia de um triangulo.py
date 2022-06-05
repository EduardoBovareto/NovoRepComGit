#SUBPRODGRAMA
def VerificaTriangulo(Tri):
    Resultado = 0 
    i = 0
    a = Tri[0]
    b = Tri[1]
    c = Tri[2]

    # while i < len(Tri):
#abs pega o valor absoluto da diferença,"eliminando o sinal".
    if abs(b - c) < a <  (b + c):
            Resultado += 1

    if abs(a - c) < b < (a + c):
            Resultado += 1

    if abs(a - b) < c < (a + b):
            Resultado += 1
    
    if Resultado == 3:
        return 3
    else:
        return False
#PROGRAMA PRINCIPAL
i = 0
Lados = []
print('Padrão de lados emitidos: a, b, c')
while i < 3:
    Lados.append(int(input(f'Informe o lado {i + 1}: '))) # Adiciona a lista valores digitados pelo input()
    if 0 in Lados: # Retirando valores nulos
        del(Lados[i]) #Deleta o elemento
        Lados.append(int(input(f'Informe novamente, 0 não é permitido {i + 1}: ')))#Recoleta o valor
    i += 1
if VerificaTriangulo(Lados) == 3:
    print('O Triângulo Existe!!!')
else:
    print('Este triângulo não é possível')