valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while True:
        if r in 'SN':
            break
    if r in 'N':
        break
pares = []
impares = []
for n in valores:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('-=' * 40)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')

