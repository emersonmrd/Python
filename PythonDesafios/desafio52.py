print('DESVENDADOR DE NÚMERO PRIMO')
"""num = int(input('Insira um número: '))
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
    print('{} não é um número primo.'.format(num))"""

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num,tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print(('E por isso ele NÃO É PRIMO!'))
