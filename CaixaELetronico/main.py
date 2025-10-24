import names #temporariamente, pois a senha sera atralada a um nome
from random import randint, choice
'''
2 - informar saldo de debito e credito(def Debito(), def Credito(), def MostraSaldo())
3 - realizar pagamentos - selecionar (boleto, fatura de credito, pix), (def Pagamento())
4 - realizar saques - (def Saque)
5 - extrato bancario com data (def Extrato)
6 -limite de credito (LimitaCredito)
7 - Emprestimo (def Emprestimo)
8 - Juros acima do Cheque especial (cheque especial)
'''
def DadosPessoais():
    # DP sera um set
    salario = randint(1200, 20000)
    nome = names.get_last_name() #nome aleatorio
    pais = 'Brazil'
    dependentes = randint(0,5)
    residencia =  choice(True, False) #escolhe um dos DadosPessoais
    
    
def Lesenha(senha):
    #tratar senha forte e emitir mensagem futuramente
    return len(senha)
    
def debito():
        
pass
def credito():
    pass

def Saldo()

menu = True
template = None #tempate do banco
senha = None

while menu == True:
    senha = str(input('Digite a sua senha de acesso:  10 caracteres!'))
    Lesenha(senha)
    if len(senha) < 10:
        senha = str(input('Digite a sua senha de acesso:  10 caracteres!'))
    else:
        template = int(input('''
            Bem Vindo ao Caixa Eletronico
            Operações:
            [-1] Sair do Menu
            [0]Dados Pessoais
            [1]Ler Saldo
            [2]
            [3]
            [4]
            [5]
            [6]
            [7]
            [8]
    '''))
    
    