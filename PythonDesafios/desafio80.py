valores = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > valores[-1]:
        valores.append(num)
        print('Valor adicionado ao final da lista...')
    else:
        for n in range(len(valores)):
            if num <= valores[n]:
                valores.insert(n,num)
                print(f'Valor adicionado na posição {n} da lista...')
                break

print(f'A lista ordenada é {valores}')

