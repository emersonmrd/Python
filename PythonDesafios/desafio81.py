valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    while True:
        r = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
        if r in 'NS':
            break
    if r in 'N':
        break
print('Foram digitados os valores ', end=' ')
for n in valores:
    print(n, end=' ')
print(f'\nSendo que foram digitados {len(valores)} elementos')
valores.sort(reverse=True)
print('Os valores em ordem descrecente são ', end=' ')
for n in valores:
    print(n, end=' ')
if 5 in valores:
    print(f'\nO valor 5 faz parte da lista e se encontra na posição {valores.index(5)}')
if 5 not in valores:
    print(f'\nO valor 5 não faz parte da lista.')