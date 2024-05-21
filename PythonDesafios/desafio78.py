valores = []
for cont in range(5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('=-' * 40)
print(f'Os valores digitados foram {valores}')

maior = max(valores)
menor = min(valores)
posicaomaior = []
posicaomenor = []
for c, v in enumerate(valores):
    if maior == v:
        posicaomaior.append(c)
    if menor == v:
            posicaomenor.append(c)
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for n in posicaomaior:
    print(f'{n}...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for n in posicaomenor:
    print(f'{n}...', end=' ')