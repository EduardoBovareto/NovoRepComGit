class Carro:
    def __init__(self, M, modelo, nome, ano, motor):
        self._marca = M
        self._modelo = modelo
        self._name = nome
        self._year = ano
        self._motors = motor
        self._p = None
        
    @property #decorador que cria o metodo motor como uma propriedade
    def motor(self): #metodo getter para pegar o valor de motor
        return self._motors
        #caso seja chamado carro.motor este metodo e chamado automaticamente e retorna motor

    @motor.setter #metodo que possibilita alteração do valor guardado motor emitido antes
    def motor(self, new):
        self._motors = new
        #metodo que muda o valor guardado no motor, caso solicitado

    @property
    def Tfip(self): #serve para definir o Tfip, o preco
        if self._p == None:
            self._p = float(input('Descreva o valor da FIP')) #este será caso seja vazio
        return self._p

    @Tfip.setter
    def Tfip(self, valor): #Apenas esse metodo permite alterar do lado de fora.
        self._p = valor
        return self._p   
        

Carro1 = Carro('GM', 'Celta', 'Celta VHC chevrolet',2004, 'VHC')
Carro1.motor = 'DGI' #chama @motor.setter
print(Carro1.motor)

Carro1.Tfip = 11.800
print(Carro1.Tfip)

'''
class Carro:
    def __init__(self, M, modelo, nome, ano, motor):
        self._marca = M
        self._modelo = modelo
        self._name = nome
        self._year = ano
        self.__motors = motor  # Agora o atributo é realmente privado

    @property
    def motor(self):
        return self.__motors  # Getter
    
    @motor.setter
    def motor(self, novo_motor):
        if novo_motor != "VHC":
            print("Motor não válido!")
        else:
            self.__motors = novo_motor  # Setter

# Exemplo de uso
carro1 = Carro("GM", "Celta", "Celta VHC", 2004, "VHC")

# Usando a propriedade
print(carro1.motor)  # Exibe "VHC"
carro1.motor = "VHC E"  # Altera para "VHC E"
print(carro1.motor)  # Exibe "VHC E"

# Tentando acessar diretamente __motors
# carro1.__motors  # Vai gerar um erro de atributo, porque __motors é agora privado

# No entanto, podemos acessar de forma "mangled":
print(carro1._Carro__motors)  # Isso vai funcionar, mas é altamente desaconselhado!



'''