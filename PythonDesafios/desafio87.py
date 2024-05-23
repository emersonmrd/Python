"""matriz = []
vetor0 = []
vetor1 = []
vetor2 = []
soma_pares = soma_terceira_coluna = maior_segunda_coluna = 0
for i in range(0, 3):
    if i == 0:
        for j in range(0,3):
            vetor0.append(int(input(f'Digite um valor para [{i}, {j}]: ')))
    if i == 1:
        for j in range(0,3):
            vetor1.append(int(input(f'Digite um valor para [{i}, {j}]: ')))
    if i == 2:
        for j in range(0,3):
            vetor2.append(int(input(f'Digite um valor para [{i}, {j}]: ')))
matriz.append(vetor0)
matriz.append(vetor1)
matriz.append(vetor2)
print('-=' * 30)
for i, vetor in enumerate(matriz):
    if i == 1:
        print()
    if i == 2:
        print()
    for j, n in enumerate(vetor):
        if n % 2 == 0:
            soma_pares += n
        if j == 2:
            soma_terceira_coluna += n
        print(f'[ {n} ]', end=' ')
print()
print('-=' * 30)
print(f'A Soma de todos os valores pares vale: {soma_pares}')
print(f'A Soma de todos os valores da terceira coluna vale: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {max(vetor1)}')
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}.')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')