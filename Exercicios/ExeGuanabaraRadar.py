Velocidade = int(input('Velocidade agora: '))
if Velocidade > 80:
    print('VOCÊ FOI MULTADO EM R$ {}'.format((Velocidade - 80) * 7))
    print('Diminua sua velocidade')
else:
    print('PARABÉNS, você nao ultrapassou o limite')
