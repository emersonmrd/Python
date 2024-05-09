import datetime
anoAtual = datetime.datetime.now().year
print('ANALISADOR DE MAIORIDADE')
menor = 0
maior = 0
for c in range(1, 8):
    anoNasc = int(input('Insira o ano de nascimento da {}º pessoa : '.format(c)))
    idade = anoAtual - anoNasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas são maiores de idade e {} pessoas são menores'.format(maior,menor))