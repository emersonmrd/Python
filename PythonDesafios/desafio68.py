from random import randint

print('=-' * 15)
titulo = 'VAMOS JOGAR PAR OU ÍMPAR'
print(f'|{titulo:^28}|')
print('=-' * 15)

vitorias = 0
while True:
    num = int(input('Diga um valor: '))
    escolha = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
        print('-' * 30)

    comp = randint(0,10)
    soma = comp + num
    resultado = 'PAR' if soma % 2 == 0 else 'ÍMPAR'

    print('-' * 30)
    print(f'Você jogou {num} e o computador {comp}. Total deu {soma} DEU {resultado}')
    print('-' * 30)

    if (escolha == 'P' and resultado == 'PAR') or (escolha == 'I' and resultado == 'ÍMPAR'):
        print('Você VENCEU!')
        vitorias += 1
        print('Vamos jogar novamente...')
        print('=-' * 15)
    else:
        print('Você PERDEU!')
        print('=-' * 15)
        print(f'GAME OVER! Você venceu {vitorias} vezes!')
        break
