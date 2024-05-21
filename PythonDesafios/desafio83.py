frase = (str(input('Digite a expressão: ')))
parenteses = 0
for c in frase:
    if c == '(':
        parenteses += 1
    elif c == ')':
        parenteses += 1
if parenteses % 2 == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
#print(frase.count('('))
#print(frase.count(')'))