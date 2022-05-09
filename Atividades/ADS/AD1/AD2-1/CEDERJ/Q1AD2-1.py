'''                     Descrição do algorítimo
    Algorítimo que lê um arquivo .txt e analisa seu conteúdo interno, dizendo se está vazio ou se há numeros inteiros
    QUANDO FOR DAR NOME AO ARQUIVO. É O NOME DO ARQUIVO QUE ESTÁ NO DOCUMENTO TEXTO
'''
import os
def ProcessaConteudo(ArquivoInt): # Processamento de arquivo com valores inteiros
    # Variaveis locais necessárias:
    maior = menor = media = j = 0
    temp = []
    distancias = []
    simbolo = 0
    soma = Local = total = 0
    # Gerar uma string concatenada com os valores e ai colocar dentro de uma variavel, é so analisar o len
    String = ''
    contador = 0
    ArquivoInt.seek(0)

    for i in ArquivoInt:
        Linha = i
        for k in Linha:
            if k != " " and k.isnumeric() and contador >= 1:
                String += k
                contador += 1
            
            if k != " " and k.isnumeric():
                String += k

            if k == " ":
                String += k
                contador = 0
                continue
            
            if k == "-":
                simbolo = k
                String = String + " " + simbolo
            if k == '\n':
                String += ' '
            
            # Depois usar ou split ou posição de string
    contador = 0
    String = String.split()
    for i in String:  # Analise de linha USAR SPLIT COM A STRING
        if i.isnumeric():
            # Caso de 2 algarismos
            temp.append(int(i))     


        if i[0] == '-' and len(i) > 1:
            i = int(i[1:3])
            i *= -1
            temp.append(i)
            print(i)

    counter = len(temp) # Quantidade de valores
    for i in temp: 
        if i < maior: # caso menor
            if i < menor:
                    menor = i

        if i > maior: # Caso maior
                maior = i
        soma += i
    media =  soma / counter # Media final
    for i in temp:
        # distancias.append((i - media) ** (1 / 2)) # Distancias
        distancias.append((i - media) ** (1 / 2))
    for i in distancias:
        total += i

    dvp = total / counter 
    return (f'''Menor valor em {ArquivoFinal.name}: {menor}\nMaior valor em {ArquivoFinal.name}:{maior}\nMédia dos valores em {ArquivoFinal.name}:{media}\nDesvio Padrão em {ArquivoFinal.name}:{dvp}

    ''')

ArquivoInter = input('Digite o nome do arquivo:')


ArquivoInter = 'C:\\Users\\WINDOWS\\Desktop\\' + ArquivoInter
# os.rename(ArquivoInter, tempory)

ArquivoFinal = open(ArquivoInter, "r") # Abrindo e instanciando arquivo
for linhas in ArquivoFinal: # Percorrer para ver se ele esta vazio
        if linhas == " ": # Condição de vazio
            ArquivoFinal.close()  # Fechando o arquivo pois ja foi analisado
            print('Não existem menor, maior, média e desvio,pois o arquivo está vazio!!!') # Fechando a função pois não há mais o que analisar
            break
        else:
            print(ProcessaConteudo(ArquivoFinal)) # Caso com valores
ArquivoFinal.close()

