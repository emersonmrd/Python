'''from random import randint

numeros = []

def sorteia():
    print(f'Sorteando 5 valores da lista: ',end='')
    for c in range(0, 5):
        numeros.append(randint(1, 10))
        print(f'{numeros[c]} ', end='')
    print(f'PRONTO!')

def somaPar():
    s = 0
    for n in numeros:
        if n % 2 == 0:
            s += n
    print(f'Somando os valores pares de {numeros}, temos {s}')

sorteia()
somaPar()
'''

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1,  10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)