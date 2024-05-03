#Um ano é bissexto se for divisível por 4.
# No entanto, se o ano for divisível por 100, não é bissexto,
# a menos que também seja divisível por 400.

ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('O ano {} é um ano Bissexto!'.format(ano))
        else:
            print('O ano {} não é um ano Bissexto!'.format(ano))
    else:
        print('O ano {} é um ano Bissexto!'.format(ano))
else:
    print('O ano {} é não um ano Bissexto!'.format(ano))
