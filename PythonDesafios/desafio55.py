print('ANALISADOR DE PESO')
primeiroPeso = float(input('Insira o peso em Kg da 1º pessoa:  '))
maiorP = primeiroPeso
menorP = primeiroPeso
for c in range(2, 6):
    peso = float(input('Insira o peso em Kg da {}º pessoa:  '.format(c)))
    if maiorP < peso:
        maiorP = peso
    if menorP > peso:
        menorP = peso
print('O Menor peso é {:.2f} Kg.'.format(menorP))
print('O Maior peso é {:.2f} Kg.'.format(maiorP))