from random import randint

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

