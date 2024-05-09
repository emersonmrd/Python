print('ANALISADOR DE PESO')
"""primeiroPeso = float(input('Insira o peso em Kg da 1º pessoa:  '))
maiorP = primeiroPeso
menorP = primeiroPeso
for c in range(2, 6):
    peso = float(input('Insira o peso em Kg da {}º pessoa:  '.format(c)))
    if maiorP < peso:
        maiorP = peso
    if menorP > peso:
        menorP = peso
print('O Menor peso é {:.2f} Kg.'.format(menorP))
print('O Maior peso é {:.2f} Kg.'.format(maiorP))"""


maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
