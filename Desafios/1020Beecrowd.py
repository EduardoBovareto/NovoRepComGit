idade = int(input(''))
ano = 0 
mes = 0
dias = 0

ano = idade // 365
idade -= (365 * ano)

mes = idade // 30
idade -= (30 * mes)

dias = idade

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dias} dia(s)')
