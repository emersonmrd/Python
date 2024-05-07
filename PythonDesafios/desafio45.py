import random
print('VAMOS JOGAR JOKENPÔ')
nomejogador = str(input('Digite seu nome: ')).capitalize()
#Escolha do jogador
jogador1 = int(input('ESCOLHA:\n'
                     '1 - PEDRA\n'
                     '2 - PAPEL\n'
                     '3 - TESOURA\n'
                     'Digite aqui: '))

#Valida a escolha do jogador
if jogador1 < 1 or jogador1 > 3:
    print('Insira um valor válido')
    exit()

#Escolha do computador
computador = random.choice(range(1, 4))
if computador == 1:
    print('O Computador escolheu PEDRA.')
elif computador == 2:
    print('O Computador escolheu PAPEL.')
else:
    print('O Computador escolheu TESOURA.')

if jogador1 == 1 and computador == 1 or jogador1 == 2 and computador == 2 or jogador1 == 3 and computador == 3:
    print('EMPATE!')
elif jogador1 == 1 and computador == 2:
    print('O COMPUTADOR Venceu!')
elif jogador1 == 1 and computador == 3:
    print('O {} Venceu!'.format(nomejogador))
elif jogador1 == 2 and computador == 3:
    print('O COMPUTADOR Venceu!')
elif jogador1 == 2 and computador == 1:
    print('O {} Venceu!'.format(nomejogador))
elif jogador1 == 3 and computador == 2:
    print('O {} Venceu!'.format(nomejogador))
elif jogador1 == 3 and computador == 1:
    print('O COMPUTADOR Venceu!')
else:
    print('OCORREU UM ERRO TENTE NOVAMENTE.')

