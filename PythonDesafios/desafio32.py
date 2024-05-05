#Um ano é bissexto se for divisível por 4.
# No entanto, se o ano for divisível por 100, não é bissexto,
# a menos que também seja divisível por 400.
from datetime import  date
ano = int(input('Digite um ano que deseja analisar\n'
                'caso queira analisar o ano atual digite 0.'
                'Ano:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400  == 0:
    print('O ano {} é Bissexto!'.format(ano))
else:
    print('O ano {} não é Bissexto!'.format(ano))

