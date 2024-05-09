print('CALCULADORA DE NUMEROS PARES')
s = 0
for c in range(1,7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        s += num
print('A soma dos valores pares digitados vale {}'.format(s))