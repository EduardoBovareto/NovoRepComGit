class ControleRemoto: # Inicia a criação de um objeto
    def __init__(self, ValorCor='', Vtamanho='', Pequeno=''): # Função inicializadora que cria os atributos
        self.cor = ValorCor # Tudo que tem Self é um atributo do objeto
        self.Tamanho = Vtamanho # Tudo que tem Self é um atributo do objeto
        self.Caracteristica = bool(Pequeno) # Tudo que tem Self é um atributo do objeto

controleremoto = ControleRemoto("Preto", '', True) # Podemos replicar a intancia do objeto varias vezes
print(controleremoto.Caracteristica)
# Self significa ele mesmo, o objeto mesmo
'''
class cria um objeto e nos permite gerar atributos == caracteristica e gerar propriedades == valores dos atributos

Com os objetos podemos pegar qualquer informação dentro de um contexto e aplicar e gerar um objeto que faça o que queremos. 

    Por exemplo um cliente, pode ser um objeto e que tem (nome, idade, numero de cartao, identificação) e por ai vai, e para cada cliente de um empresa não da para usar variaveis para cada um.
'''