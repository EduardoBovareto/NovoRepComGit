'''
Vê se a cidade em que nasceu começa com "santo" se não começar emite False
'''
local = input('Onde você Nasceu? ').strip()
local = local.capitalize()
pesquisa = local.find("Santo")
if pesquisa != -1:
    print(True)
else:
    print(False)
