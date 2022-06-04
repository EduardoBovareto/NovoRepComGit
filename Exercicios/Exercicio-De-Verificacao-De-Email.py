# Modificar esse algorítimo para gerar emails diferentes quanto a modelos, depois gerar o resultado em arquivo txt, xls, e printar em forma de dicionário ou dicionário de tuplas.

def MostraPossiveisEmails():
    pass
print(''' O Email que será fornecido deve conter: 
    - Seu nome;
    - Seu Sobrenome;
    - Caracteres Especiais (@, .);
    - Deve ter entre 20 e 30 Caracteres
''') # Emissão de funcionalidade

j = 1 # Variavel de controle
while j != 0:
    Modelo = input('Qual modelo de Emnal deseja gerar: ')
    Email = input('Informe seu primeiro Nome e sobrenome:').split()
    
    if (len(Email) < 20 or (len(Email) < 35)): # Condição de existencia de um email
        print('\nO seu Email está muito pequeno! Procure colocar seu NOME no meio dele!\n')
        j = 0
    else: # Subordinação do programa principal
        ComplementoEmail = Email.find(".com")
        if Email.find("@") == -1:
            print('''\nPor favor emitir novamente seu email.
                    Qualquer email precisa do caracter "@" !
            \n''')
            Email = input('\n\nDigite seu Email:')

        pos = Email.find('@')
        Email2 = Email[:ComplementoEmail]

        if Email2.find('.') != -1: #Pegando o ponto do .com se for Email[]
            PosicaoDoPonto = Email2.find('.') # Agora nao considera o ponto do .com mais
            print('Nome do cara:', Email2[:PosicaoDoPonto]) # NOME DO INDIVIDUO
            PosicaoDepoisPonto = PosicaoDoPonto + 1
            print('Sobrenome do cara: {} '.format(Email2[PosicaoDepoisPonto:pos])) # SOBRE NOME DELE
            # Pegar intituição de emdereço de email alocado!
        else:
            NomeDoCara = Email[:pos]
            pos2 = pos + 1
            instituicao = Email[pos2:ComplementoEmail] # Pega a instituição escrita
            print('O seu nome é: {} e sua instituição de endereço é: {}'.format(NomeDoCara, instituicao))

        # podemos usar elif dentro de if ou em seguida para casos errados!
        if (Email.find('#') != -1):
            # Verificação de irregularidade no email necessária!
            print('O "#" não pode ser colocado no email, favor emitir outro modelo') 
            while (Email.find('#') != -1):
                print('O "#" não pode ser colocado no email, favor emitir outro modelo') 
                Email = input('Informe seu Email!')
                # Ele irá sempre pedir para colocar seun email.


# senha = input('Informe sua senha')
# if senha.find('?') != -1:
#     while senha.find('.' or '#' or '?' or '""') != -1:
#         senha = input('Sua senha estava no padrão Errado:')

# Tem erro, ele não lê qualquer email, e se lê fora do pradrão ele repete 2 vezes.