nome = str(input('Digite seu nome completo: '))
qtdLetras = len(nome.replace(' ',''))
letrasPrimeiroNome = len(nome.split()[0])
print('O seu nome completo em letras maisculas é {}'.format(nome.upper()))
print('O seu nome completo em letras minusculas é {}'.format(nome.lower()))
print('O seu nome possui {} letras desconsiderando o espaçamento!'.format(qtdLetras))
print('O seu primeiro nome possui {} letras!'.format(letrasPrimeiroNome))
