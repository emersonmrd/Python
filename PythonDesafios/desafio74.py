from random import randint
numeros = tuple(randint(0, 10) for _ in range(5))
print(numeros)

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
print(f'Os valores sorteados foram: {numeros[0]} {numeros[1]} {numeros[2]} {numeros[3]} {numeros[4]}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')