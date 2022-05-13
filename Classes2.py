# Como se consseguissimos ser o criador e definir que aquilo que criamos é um tipo de alguma coisa que se aplica.
'''
    É como se consseguissimos definir um tipo específico para aquele dado.
    Tipos de dados personaliazados que pode ser criado.
    E essa criação se baseia em objetos, ou seja, todo dado novo personalizado e que irá ser ultilizado será usado para criar um objeto como na vida real.

    Ou seja, os tipos personalisados criam objetos, criam algo qeu na nossa cabeça é material, é uma coisa mesmo, como um lápis.

    é como se você quisesse criar seu lápiz e ele é diferente, porque você criou ele redondo, logo, você criou, n deixa de ser um lapis.

    Todo objeto não tem sua especificação e é diferente de alguma forma? o que você cria também será.
'''
from ctypes.wintypes import PCHAR


class CriaUmPc:
    ''' Cria um conjunto de strings emitidas pelo usuário que
        representam um PC
    '''
    def __init__(self, Valor):
        self.membro = Valor # Pré-define a marca do PC
        self.cerebro = 'i5-3320M' 
        self.durabilidade = 15 # Define a quantidade de anos de um PC, em média
        print('A marca escolhida foi: ', self.membro)
computer = CriaUmPc('Intel')