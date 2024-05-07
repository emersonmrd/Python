print('SISTEMA DE ANALISE DE CATEGORIA')
anoNasc = int(input('Insira o ano de nascimento do atleta: '))
anoAtual = 2024
idade = anoAtual - anoNasc
if idade <= 9:
    print('ATLETA MIRIM')
elif idade <= 14:
    print('ATLETA INFANTIL')
elif idade <= 19:
    print('ATLETA JUNIOR')
elif idade <= 20:
    print('ATLETA JUNIOR')
else:
    print('ATLETA MASTER')
