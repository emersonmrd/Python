print('SELETOR DE SEXO')
sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('DADOS INVÁLIDOS.Por favor, Informe seu sexo [M/F]: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))