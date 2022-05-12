dictPC = {
    'CPU': 'i5-3320M',
    'Fabricante': 'Intel',
    'Ano do PC': 2010,
    'RAM': '6G',
    'Placa De Vídeo': 'NVIDIA 5200M',
        }
for chave, valor in dictPC.items(): # Desenpacotando chaves e valores no for.
    # Precisa do .tems() para desenpacotar e colocar cada chave e valor nas variaveis.
    print(f'\nA configuração do(a){chave} corresponde: {valor}\n')
Atualizacao = input('Seu PC atualizou? S/N')
if Atualizacao == 'S':
    hardware = input('Informe sua atualização').split()
    dictPC[hardware[0]] = hardware[1] # Cria uma nova chave com a peça de hardware emitida e adiciona a segunda posição que contém o valor da chave.s
    print(dictPC)
else:
    print(f'Seu PC está assim: {dictPC}')
# Podemos usar update tambem .update(), passando o nome da chave como string ou var e o seu valor com "=" ou valor literal.