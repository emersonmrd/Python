"""import datetime
anoAtual = datetime.datetime.now().year
print('ANALISADOR DE MAIORIDADE')
menor = 0
maior = 0
for c in range(1, 8):
    anoNasc = int(input('Insira o ano de nascimento da {}ª pessoa : '.format(c)))
    idade = anoAtual - anoNasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas são maiores de idade e {} pessoas são menores'.format(maior,menor))"""

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('e também tivemos {} pessoas menores de idade'.format(totmenor))