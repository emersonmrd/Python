nome = str(input('Digite seu nome completo: '))
print('Seu nome com todas letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome com todas letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome.replace(' ','').strip())))
primeiroNome = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(primeiroNome[0].strip())))