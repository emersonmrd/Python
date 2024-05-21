from random import randint
numeros = tuple(randint(0, 10) for _ in range(5))

"""
maior = 0
menor = 0
for c in range(0, len(numeros)):
    if c == 0:
        maior = numeros[c]
        menor = numeros[c]
    else:
        if maior < numeros[c]:
            maior = numeros[c]
        if menor > numeros[c]:
            menor = numeros[c]
    c += 1
"""
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')