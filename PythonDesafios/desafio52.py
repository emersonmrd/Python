print('DESVENDADOR DE NÚMERO PRIMO')
num = int(input('Insira um número: '))
if num < 2:
    print('{} Não é um número primo.'.format(num))
else:
    primo = True
    for c in range(2, int(num ** (1 / 2)) + 1):
        if num % c == 0:
            primo = False
            break
if primo:
    print('{} é um número primo.'.format(num))
else:
    print('{} não é um número primo.'.format(num))