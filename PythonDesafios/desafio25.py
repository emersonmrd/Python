nome = str(input('Digite seu nome: '))
nome = nome.upper().strip()

print('Você possui o nome silva?\n'
      '{}'.format('SILVA' in nome))