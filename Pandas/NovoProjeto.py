import pandas as pd
Vendas = {
    'Data' : ('12/04/2022', '23/04/2021'),
    'Valor Unitário': (34, 55),
    'Quantidade': [ 344, 55],
    'Valor Total' : [344 * 34, 55 ** 2],
}
venda_df = pd.DataFrame(Vendas) #Cria um DataFrame ou uma tabela dentro da classe do python
# print(venda_df)
venda_df2 = pd.read_excel("C:\\Users\\WINDOWS\\Desktop\\JS\\Python-temporário\\PlanilhaProjeto.xlsx")
# print(vendas_df2)
# print(venda_df2.shape)#Mostra a quantidade de linhas
print(venda_df2.describe())  
'''Metodo de return de resumo de estatistica das colunas numéricas'''