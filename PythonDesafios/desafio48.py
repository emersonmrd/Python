print('CALCULADORA DE NÚMERO IMPARES MULTIPLOS DE 3')
"""s = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        s += c
print('A soma entre todos os números impares e múltiplos de 3 de 1 a 500 é {}'.format(s))"""

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos os {} valores solicitados é {}.'.format(cont,soma))
