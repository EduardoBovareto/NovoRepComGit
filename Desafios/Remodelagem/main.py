'''
Mini sistema de Banco que calcula os gastos de um cliente em forma de lista.
Informa também que se houver dívida ele deve pagar dentro de um sistema de juros compostos. É um sistema simples e básico
mas que ainda precisa de arremates para se parecer mesmo com  um sistema de banco, um Menu inical e tudo mais. 
Vale notar que aina não foi colocado a função Dívida que está notificado ao decorrer do código.
'''
def Mensagem():
  Banco = 'Banco DIN'
  print('{:=^30}'.format(Banco))
  print('\n\nBem vindo ao Banco que quer o SEU DINHEIRO!\n\n ')
  print('{:=^30}'.format(Banco))

def Porcentagem(saldo):
  
  if saldo == (saldo * 10) / 100:
    # global user

    print('\n\nO senhor ATINGIU 10% DO SALÁRIO: {} \n\n'.format((saldo * 10) / 100))
    # verifica = int(input('DESEJA MESMO CONTINUAR?: 1.Sim | 2.NAO'))
    # if verifica == 2:
    #   user = 1
    # Isso pode ficar fora da função

  elif saldo == (saldo * 30) / 100:
    print('\n\n O senhor ATINGIU 30% DO SALÁRIO: {} '.format((saldo * 30) / 100))
  
  elif saldo == ((saldo * 45) / 100):
    print('\n\n O senhor ATINGIU 45% DO SALÁRIO: {} '.format((saldo * 45) / 100))

  return None

Mensagem() 
saldo_Atual = float(input('\n\nInforme seu saldo/salário atual:  '))
saldo_Inicial = saldo_Atual # Variavel que preservar o valor inicial
lista_Gastos = []
user = 1
while user != 2:
  if saldo_Atual == 0:
    condicao_Divi = int(input('\n Deseja continuar ? O senhor usará crédito pago no futuro! 1.True 2.False \n'))
    if condicao_Divi == 2:
      user = 2
    if condicao_Divi == 1:
      print('\nObrigado por nos dizer, Seja bem vindo!\n')

  gastos = float(input('\nInforme seus gastos:\n'))
  saldo_Atual = saldo_Atual - gastos
  print('Saldo Atual: {}'.format(saldo_Atual),end=" ")
  lista_Gastos.append(gastos)
  print('Gastos: {}'.format(lista_Gastos))
  Porcentagem(saldo_Atual) 
  
  if saldo_Atual > 0 and saldo_Atual != saldo_Inicial:
    user = int(input(' Deseja continuar notificando seus gastos? 1.True ou 2.False'))
  
  if saldo_Atual == 0:
    print('\nO SEU SALDO ACABOU!! {}\n'.format(saldo_Atual))
    user = int(input('\n Deseja continuar notificando seus gastos? 1.True ou 2.False\n'))

    if user == 2:
      Banco = 'Banco DIN'
      print('\n{:=^30}\n'.format(Banco))
      print('\nOBRIGADO POR ESTAR COM O BANCO DE AGIOTAS, SÓ QUEREMOS SEU DINHEIRO!!\n')
      print('{:=^30}'.format(Banco))
  
  if saldo_Atual < 0:
    print('O SENHOR FEZ UMA DÍVIDA DE: {}'.format(saldo_Atual))
    # dadosDivida()
    user = int(input('\n Deseja continuar gastando ? 1.True 2.False'))
    if user == 2:
      print('\n O SENHOR, Deve pagar {} em {} meses para o Banco BIN com uma taxa de: {}% ao mês \n'.format(saldo_Atual, 50, 8))
  # Os 10% estao dando 0 e sendo impressos quando o saldo_Atual == 0
# Fazer uma função dívida, para caso o cara entre em dívida, colocar tanto o quanto ele deve e quanto será cobrado por meses ou anos em uma taxa, além de cobrança de serviço por tantos anos junto sem pagamentos ou dívidas.
#     valor = float(input('digite o valor desejado:'))
#     periodo = int(input('Informe a quantidade de meses do empréstimo:'))
#     taxa = 5 / 100
#     valor = valor * periodo
#     total_a_Pagar = valor * ((1 + taxa) ** periodo)
#     # total_a_Pagar == Montante