from datetime import date
print('SISTEMA DE ANALISE DE CATEGORIA')
anoNasc = int(input('Insira o ano de nascimento do atleta: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('ATLETA MIRIM')
elif idade <= 14:
    print('ATLETA INFANTIL')
elif idade <= 19:
    print('ATLETA JUNIOR')
elif idade <= 25:
    print('ATLETA SENIOR')
else:
    print('ATLETA MASTER')
