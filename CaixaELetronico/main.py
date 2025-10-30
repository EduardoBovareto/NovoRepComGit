#import names #temporariamente, pois a senha sera atralada a um nome
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

def DadosPessoais(): #Data people menu
    atualizacao = None

    salario = randint(1200, 20000)
    nome = 'Eduardo' #nome aleatorio
    pais = 'Brazil'
    dependentes = randint(0,5)
    residencia =  choice([True, False])

    DP = {
        'nome': nome,
        'salario': salario,
        'pais': pais,
        'dependentes': dependentes,
        'residencia': residencia
    }
    globals()['DP'] #torna DP global em todo o codigo

    atualizacao = (input('You want edit your data:[y-n]'))
    temp = 0 #DP manipulation

    if atualizacao == 'n': 
        return False
    else: #else para consulta de dados
        print('''Nome\nSalario\nPais\nDependentes\nResidencia''') 
    
    subprogram = True
    while subprogram == True:
        temp = str(input('Describe the option,Data or write "sair": ')).lower() #opção de dado a ser alterado + novo
        
        if temp == 'sair':
           subprogram = False
        
        else:
            temp = temp.split(',')
            if temp[0] not in DP.keys():
                temp = str(input('Write the option in DataBase!!,Data or write "sair": ')).lower()
                temp = temp.split(',')
            key = temp[0] #chave informada
            DP[key] = temp[1]  #guardando valor informado
    return True
    
    #elif temp == 4:
    #    key = list(DP.keys())[temp] = bool(input('Home:  '))
    #    DP[list(DP.keys())[temp]] = key #list(DP.keys())Pega as chaves de DP por keys, tem seleciona
    #    print(f"It's the change: {key}")
 
    
def VerificaSenha(senha):
    while len(senha) < 10:
        senha = str(input('Digite a sua senha de acesso:  10 caracteres!'))
    return senha

def Menu(menu):
    menu = True
    template = '' #template do banco
    senha = ''

    while menu == True:
            if len(senha) == 0:
                senha = VerificaSenha(senha)
            else:
                template = int(input('''
                Bem Vindo ao Caixa Eletronico
                Operações:
                [-1] Sair do Menu
                [0] Dados Pessoais
                [1] Ler Saldo
                [2]
                [3]
                [4]
                [5]
                [6]
                [7]
                [8]
                '''))
                if template == -1:
                    menu = False

                elif template == 0:
                    menu = DadosPessoais()
    if menu == False:
        print('Fim da Execução, Bom dia!')

Menu(True)

'''    
def debito():   
    pass

def credito():
    pass

def Saldo():
    pass
'''