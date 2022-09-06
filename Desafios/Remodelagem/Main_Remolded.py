from random import randint, choice, shuffle
class Cliente():
    def __init__(self, name:str) -> True: #essa seta co True significa o retorno da função, como ele irá retornar no final
       self.name = f'{name}'
       self.Register = list(range(randint(0, 7), 9))
       self.unity = list(range(randint(1, 5), randint(6, 9)))
       self.country = 'BR'
       self.balanceInit = randint(354, 853)
    
    #muda as configurações do cliente
    def change_Config(self, config, data, leed) -> None:
        if config not in Cliente.getmembers():
            return print('Your config dont exist in we Data Base! Please request a new configuration!')
        else:
            Cliente.config = data
            return print(f'Your configuration is {leed.config}, she was changed')

    def show_config(self) -> True:
        for conf in Cliente:
            print(self.conf, '\n')
        
    def show_balance(self): #mostra saldo
        print(f'Your balance is {self.balanceInit}')
        return self.balanceInit

    def change_balance(self, value) -> True:
        pass

    def loan_get(self): #pegar empréstimo
        pass

    def show_porcent(self):
        pass

    def _buy(self):
        pass

    def _sale(self):
        pass
    
    def counter_sales(self):
        pass