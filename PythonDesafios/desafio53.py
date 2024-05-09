print('ANALISADOR DE PALÍNDROMO')
frase = str(input('Digite aqui uma frase: ')).strip().lower()
palavras = frase.split()
fraseApresentacao = " ".join(palavras)
fraseSemEspacos = frase.replace(' ','')
if fraseSemEspacos == fraseSemEspacos[::-1]:
    print('A frase "{}" é um Palíndromo.'.format(fraseApresentacao.capitalize()))
else:
    print('A frase "{}" não é um Palíndromo.'.format(fraseApresentacao.capitalize()))