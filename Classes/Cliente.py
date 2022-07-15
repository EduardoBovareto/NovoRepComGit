#Cria clientes de  um negócio
import datetime as dt
from random import choice
class Cliente:
    def __init__(self, Nome, NI):
        self.identi = Nome
        self.Numeber = NI
        self.data = dt.date.today()
        self.Bandeira = choice(['Visa', 'MasterCard']) #Ou random.choice(lista) ou choice(lista)
        self.Saldo = 500
        self.Pagamento = self.data + dt.timedelta(int(input('Digite um valor para pagamento'))) #Transforma 30 em 30 dias do tipo time delta, ou seja, 30 dias coridos
    
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
    
    def mudar_fatura(self, diaP):
        self.Pagamento += dt.timedelta(diaP)
        pass
Eduardo = Cliente('Edaurdo B', (0, 0, 0, 1, 1, 3, 4))
# Eduardo.confere_saldo()
# Eduardo.retira_valor(500)
# Eduardo.confere_saldo()
print(Eduardo.data, Eduardo.Pagamento)
Eduardo.mudar_fatura(25)
print(Eduardo.Pagamento)