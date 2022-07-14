#Cria clientes de  um negócio
from time import time
class Cliente:
    def __init__(self, Nome, NI):
        self.identi = Nome
        self.Numeber = NI
        # self.data
        self.Bandeira = input('Digite a bandeira')
        self.Saldo = 500
        self.Pagamento = int(input('Digite o dia do pagamento'))
    
    def confere_saldo(self):
        Ms = self.Saldo
        return print(f'O seu saldo é {Ms}')    
    
    def retira_valor(self, Compra):
        self.Saldo -= Compra
        if self.Saldo < 100:
            return self.Saldo, print('SEU SALDO ESTA ACABANDO!')
        
        elif self.Saldo == 0:
            return self.Saldo, print('Seu saldo acabou')
          
        return print(f'Valor de Saldo Atual: {self.Saldo}')

    def alterar_nome(self, novoname):
        self.identi = novoname
        return self.identi, print('Nome Atualizado !')
Eduardo = Cliente('Edaurdo B', (0, 0, 0, 1, 1, 3, 4))
# Eduardo.confere_saldo()
# Eduardo.retira_valor(500)
# Eduardo.confere_saldo()
print(Eduardo.data)