'''
👉 Dica de raciocínio:

Quem são os 3 mais pesados?

Quem são os 3 mais leves?
Quantas pessoas têm o mesmo peso máximo?

Quantas têm o mesmo peso mínimo?

Existe alguém com peso exatamente igual à média?
Peso negativo é válido?

Peso zero faz sentido?

Nome vazio deve ser aceito?
'''
def AcimaMedia(listaP, media):#pessoas acima da media
    RelacaoPeso = {
        'Ate 60': '',

        'Ate 80': '',

        '+ de 80': ''
    }
    
    for p in listaP:#desempacota cada array dentro de p e analisa cada peso
        if p[1] <= 60:
            RelacaoPeso['Ate 60'] += f'{p} '

        elif p[1] <= 80:
            RelacaoPeso['Ate 80'] += f'{p} '

        else:
            RelacaoPeso['+ de 80'] += f'{p} '

    print(RelacaoPeso)
    return None

def Lenome(nome):
    if len(nome) < 3:#nome ou sigla
        while len(nome) < 3:
            print('\n Este nome e muito pequeno ou indevido!\n')
            nome = input('Escreva um nome de uma pessoa: ')
        return nome
    
    else:
        return nome
    
def VePeso():
    pass

flag = ''
pessoas = []
maior = menor = 0
pesados = []
leves = []
Media = 0
Soma = 0
while True:
    nome = input('\nEscreva um nome de uma pessoa: ')
    nome = Lenome(nome)

    peso = float(input('Escreva o peso: '))
    pessoas.append([nome,peso])#nome e peso para calculo estatistico
    Soma += peso #media de peso das pessoas

    if maior < peso or maior == 0:#exite um mais pesado que o atual
        #caso exista a galera que estava sai porque e mais leve
        maior = peso
        pesados.clear()
        pesados.append(nome) #necessario orientar o usuario quanto a valores

    elif maior == peso and nome not in leves:#tem o mesmo peso que o cara pesadao
        pesados.append(nome)#mostrar o peso que foi guardado tambem

    if menor > peso or menor == 0:#mais leves
        #caso exista uma galera mais leve eles entram e as mais pesadas saem
        menor = peso
        leves.clear()
        leves.append(nome)

    elif menor == peso and nome not in leves:#mesmo peso leve que o levinho
        leves.append(nome)

    flag = input('\nDeseja continuar: S/N').upper()
    while flag not in 'S N':#controle de escolha
        flag = input('Erro! Deseja continuar: S/N').upper()
    if flag == 'N':
        break

Media = f'{Soma / len(pessoas):.2f}'#media de peso com 2 casas
AcimaMedia(pessoas, Media)
print(f'\nTotal de pessoas cadastradas: {len(pessoas)}')
print(f'O maior peso foi:{maior} Peso de {pesados}')
print(f'\nO menor peso foi de:{menor} Peso de {leves}')
print(Media)
#print(pessoas): [['Eduardo', 68.0], ['Maria', 56.0], ['Joao', 57.0], ['Jobiscleiva', 78.0]
