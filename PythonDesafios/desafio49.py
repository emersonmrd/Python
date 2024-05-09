"""print('='*20)
print('|{:^18}|'.format('TABULADOR'))
print('='*20)
tabulador = int(input('Digite um número que deseja saber a tabuada: '))
print('-'*20)
print('| {:^8} {:^5} |'.format('TABUADA DE',tabulador))
print('-'*20)
for c in range(1,11):
    print('| {:2} x {:2} = {:6} |'.format(tabulador, c, c * tabulador).center(18))
print('-'*20)"""

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {:2}'.format(num, c, num*c))


