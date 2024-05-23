matriz = []
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