"""matriz = []
vetor0 = []
vetor1 = []
vetor2 = []
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
        print(f'[ {n} ]', end=' ')
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
