temp = []
maior = menor = 0
posicao_maior = posicao_menor = ''

for i in range(0,5):
    temp.append(float(input('Write a value: ')))

    if maior <= temp[-1] or maior == 0:
        #caso de valor zerado ou maior < menor que o utlimo adicionado
        maior = temp[-1]
        posicao_maior += f'{i} ' #posicao do valor maior

    elif menor >= temp[-1] or menor == 0:
        #caso de valor zerado ou menor sendo um valor <  que o utlimo adicionado
        menor = temp[-1]
        posicao_menor += f'{i} '

print(f'O maior valor digitado foi: {maior} nas posicoes: {posicao_maior} ')
print(f'O menor valor digitado foi: {menor} nas posicoes {posicao_menor}')