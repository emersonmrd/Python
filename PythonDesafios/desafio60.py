#from math import factorial -> utilizando biblioteca
print('FATORIAL')
#f = factorial(num) -> utilizando biblioteca
num = int(input('Digite um número para calcular seu fatorial: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))



"""fatorial = 1
contador = num
while contador > 1:
    fatorial = fatorial * contador
    contador -= 1
print('O fatorial de {} é {}'.format(num, fatorial))"""

"""Utilizando for
for c in range(num, 1, -1):
    fatorial = fatorial * c
print('O fatorial de {} é {}'.format(num, fatorial))"""