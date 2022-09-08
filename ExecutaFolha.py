from datetime import datetime
def converte_Folha(H):
    with open('datas.txt', 'a') as arq:
      #Escrever o horario e converter em pandas depois ou só copiar e colocar para um txt que o trabalho é manual, depois colocar esse código como executável só.
      arq.write(H)
      arq.write('\n')
    
data = datetime.now()
data = data.strftime("%d/%m/%y %H:%M")
converte_Folha(data)