numeros = []
pares = []
impares = []
for c in range(1, 8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
pares.sort()
impares.sort()
numeros.append(pares)
numeros.append(impares)
print('-=' * 30)
print(f'Os valores pares digitados foram: ', end='')
for i, numero in enumerate(numeros):
    if i == 0:
        for n in numero:
            print(n, end=' ')
print(f'\nOs valores ímpares digitados foram: ', end='')
for i, numero in enumerate(numeros):
    if i == 1:
        for n in numero:
            print(n, end=' ')