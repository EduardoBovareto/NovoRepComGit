class Cliente:
    def __init__(self, nome, idade, Email, Assinatura, telefone = False): # Definindo a função init para configuração de qualquer objeto
        self.Nome = nome # Nome do cliente instanciado
        self.Idade = idade # Idade do cliente Instanciado
        self.Email = Email # Email com nome, ponto e sobrenome e o servidor
        self.Saldo = 1000.00 #Todo cliente tem 1000 reais de incio
        self.j = False # Caracteristica de Controle.
        self.Plano = ['Basico', 'Premium'] # Planos disponíveis

        if Assinatura not in self.Plano: # Checagem de planos
            print('O plano foi escrito incorretamente!') # Comunicação com o usuario
            self.Plano = input('Digite seu plano corretamente: [Basico] ou [Premium]') # Requisiçao de mudança de caso de plano errado
            while Assinatura not in self.Plano:
                print('O plano foi escrito incorretamente!') # Comunicação com o usuario
                self.Plano = input('Digite seu plano corretamente: [Basico] ou [Premium]') # Requisiçao de mudança
            return # Fecha tudo e evita erros para executar algo além daqui.

    def Descobre_Email(self):  # Informando e manipula os integrantes do email do cliente
        #self tem que ser parametro em todas as funções, é coo se tivessemos que referenciar o proprio objeto para manipular ele, referenciar a intancia que foi feita.
        Ponto =  self.Email.find('.') # Coleta a posição do ponto

        NomeDoEmail = self.Email[:Ponto] # Pega o 1 nome do cara

        Ponto += 1 # Atualização de posição posterior ao ponto para pegar o sobrenome

        PosicaoArroba = self.Email.find('@') # Acha a posição do @

        NomeDoEmail = NomeDoEmail + ' ' + self.Email[Ponto:PosicaoArroba]  # Conclui todo o nome do cliente

        Servidor = self.Email[PosicaoArroba:] # Acha o servidor de base desse email.
        print(f'O nome do Individuo no Email é: {NomeDoEmail}, o servidor é: {Servidor}') # Comunica com o usuário seu email e formadores do endereço
        return # Fecha tudo e evita erros para executar algo além daqui.
    
    def MudaEmail(self, NovoEndereco = False): # Metodo de mudança de Email
        print('''\nO endereço deve conter:
                Nome + . + Sobrenome + @ + Servidor Origem \n 
            ''') # Explica a estrutura de Email par o usuario
        NovoEndereco = input('Escreva aqui: ') # Requisita o novo email
        self.Email = NovoEndereco # Guarda o novo Email, Ainda falta verificar o padrao desse novo endereço!!
        print(f'\nEndereço de Email Atualizado, {NovoEndereco}') # Informa o Email Atualizado
        return # Fecha tudo e evita erros para executar algo além daqui.

    def MostraSaldo(self): # Informa o saldo de usuário
        if self.j: # Atributo de controle de vezes que se passou por aqui para informar o usuario
            print(f'O seu saldo atualizado é: {self.Saldo}')
            return # Fecha tudo e evita erros para executar algo além daqui.

        else: # Caso de Primeira requisicao de amostra de Saldo
            print(f'Os seu saldo é: {self.Saldo}')
            return # Fecha tudo e evita erros para executar algo além daqui.
    
    def Comprar(self, Valor): # Metodo de fgastar o saldo do usuario
        saldoIncio = self.Saldo # Guarda o saldo inicial
        self.Saldo -= Valor  # Atualizacao de Saldo
        self.j = True # Atualização de atributo controle onde ja se pediu para comprar.
        if saldoIncio > self.Saldo: # Verfica se foi realizada a compra
            print('Foi atualizado:', self.Saldo)
            saldoIncio = self.Saldo
            return # Fecha tudo e evita erros para executar algo além daqui.

    def Retorna_Configuracoes():
        pass

cli = Cliente('Eduardo', 20, 'Eduardo.Bovareto@Outlook.com', 'Basic') # Precisa instanciar o objeto pra dps usar os metodos.
cli.Descobre_Email() # Chama cada metodo para execucao
cli.MostraSaldo() # Chama cada metodo para execucao
cli.Comprar(500) # Chama cada metodo para execucao
cli.Comprar(200) # Chama cada metodo para execucao
# cli.MudaEmail()