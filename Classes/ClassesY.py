class Cliente:
    def __init__(self, nome, idade, Email, Assinatura, telefone = False):
        self.Nome = nome
        self.Idade = idade
        self.Email = Email # Email com nome, ponto e sobrenome e o servidor
        self.Saldo = 1000.00 #Todo cliente tem 1000 reais de incio
        self.j = False
        self.Plano = ['Basico', 'Premium']

        if Assinatura not in self.Plano:
            print('O plano foi escrito incorretamente!')
            self.Plano = input('Digite seu plano corretamente: [Basico] ou [Premium]')
            while Assinatura not in self.Plano:
                print('O plano foi escrito incorretamente!')
                self.Plano = input('Digite seu plano corretamente: [Basico] ou [Premium]')
            return

    def Descobre_Email(self): 
        #self tem que ser parametro em todas as funções, é coo se tivessemos que referenciar o proprio objeto para manipular ele, referenciar a intancia que foi feita.
        Ponto =  self.Email.find('.')
        NomeDoEmail = self.Email[:Ponto]
        Ponto += 1
        PosicaoArroba = self.Email.find('@')
        NomeDoEmail = NomeDoEmail + ' ' + self.Email[Ponto:PosicaoArroba] 
        Servidor = self.Email[PosicaoArroba:]
        print(f'O nome do Individuo no Email é: {NomeDoEmail}, o servidor é: {Servidor}')
        return

    def MudaEmail(self, NovoEndereco = False):
        print('''\nO endereço deve conter:
                Nome + . + Sobrenome + @ + Servidor Origem \n
            ''')
        NovoEndereco = input('Escreva aqui: ')
        self.Email = NovoEndereco
        print(f'\nEndereço de Email Atualizado, {NovoEndereco}')
        return

    def MostraSaldo(self):
        if self.j:
            print(f'O seu saldo atualizado é: {self.Saldo}')
            return

        else:
            print(f'Os seu saldo é: {self.Saldo}')
            return
    
    def Comprar(self, Valor):
        saldoIncio = self.Saldo
        self.Saldo -= Valor
        self.j = True
        if saldoIncio > self.Saldo:
            print('Foi atualizado:', self.Saldo)
            saldoIncio = self.Saldo
            return

    def Retorna_Configuracoes():
        pass



cli = Cliente('Eduardo', 20, 'Eduardo.Bovareto@Outlook.com', 'Basic')
cli.Descobre_Email()
cli.MostraSaldo()
cli.Comprar(500)
cli.Comprar(200)
# cli.MudaEmail()