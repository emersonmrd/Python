nomeCompleto = str(input('Digite o seu nome completo: '))
nomeSeparado = nomeCompleto.split()
print('Seu primeiro nome é {}\n'
      'Seu último nome é {}'.format(nomeSeparado[0], nomeSeparado[-1]))