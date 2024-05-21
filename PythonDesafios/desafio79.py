valores = []
resposta = 'S'
while True:
    num = (int(input('Digite um número: ')))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    elif num in valores:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        resposta = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
        if resposta in 'NS':
            break
    if resposta in 'N':
        break
print('-=' * 40)
print('Os valores digitados foram: ', end=' ')
valores.sort()
for n in valores:
    print(f'{n}', end=' ')