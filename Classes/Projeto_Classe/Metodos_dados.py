from datetime import datetime

class Met:
    def __init__(self) -> None:
        pass

    def fsi():
	#function of the planner security
        with open('fispq.txt', 'r') as arq:
            time = datetime.today()
            time = time.strftime(' %d/%m/%Y %H:%M')
            arq.write(time)
            return arq
    
    def return_l(): 
        #retorna tupla de propriedades do produto.
        with open('propety.txt', 'r' ) as a:
            return a.readlines()