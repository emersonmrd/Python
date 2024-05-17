
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 20)
    if num < 0:
        break
    c = 1
    while c <= 10:
        print(f'{num} x {c} = {(num*c)}')
        c += 1
    print('-' * 20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')