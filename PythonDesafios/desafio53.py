print('ANALISADOR DE PALÍNDROMO')
"""frase = str(input('Digite aqui uma frase: ')).strip().lower()
palavras = frase.split()
fraseApresentacao = " ".join(palavras)
fraseSemEspacos = frase.replace(' ','')
if fraseSemEspacos == fraseSemEspacos[::-1]:
    print('A frase "{}" é um Palíndromo.'.format(fraseApresentacao.capitalize()))
else:
    print('A frase "{}" não é um Palíndromo.'.format(fraseApresentacao.capitalize()))"""

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
'inverso = '''
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!!')
else:
    print('A frase digitada não é um palíndromo!')