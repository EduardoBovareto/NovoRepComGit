from datetime import datetime
class Met:
    def __init__(self) -> None:
        pass

    def fsi(): 
#normalmente, os arquivo para retirar as constantes, devemos buscar um arquivo em pasta que tenha o nome do produto e só selecione, tipo: Molikote_fsi.txt ou Molikote_propety.txt.
	#function of the planner security
        with open('Classes\\Projeto_Classe\\fispq.txt', 'r+') as arq:
            time = datetime.today()
            time = time.strftime(' %d/%m/%Y %H:%M').split()
            company = arq.readline()

            if time[0] in arq.readlines():
                return arq, company
            else:
                arq.write(f'\n{time[0]}')


            return arq, company

    def return_l(): 
        #retorna tupla de propriedades do produto.
        with open('Classes\\Projeto_Classe\\Propety.txt', 'r' ) as a:
            return a.readlines()