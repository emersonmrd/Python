from time import sleep
def contador(i, f, p):
    print('-=' * 30)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i > f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        while f <= i:
            print(f'{i} ', end='')
            i -= p
            sleep(0.5)
        print('FIM!')
        print('-=' * 30)

    else:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        while i <= f:
            print(f'{i} ', end='')
            i += p
            sleep(0.5)
        print('FIM!')
        print('-=' * 30)



inicio = 1
fim = 10
passo = 1
contador(inicio, fim, passo)
inicio = 10
fim = 0
passo = 2
contador(inicio, fim, passo)
print('Agora é sua vez de persnalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)