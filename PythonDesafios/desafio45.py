import random
from time import sleep
print('VAMOS JOGAR JOKENPÔ')
nomejogador = str(input('Digite seu nome: ')).capitalize()
#Escolha do jogador
jogador1 = int(input('1 - PEDRA\n'
                     '2 - PAPEL\n'
                     '3 - TESOURA\n'
                     'FAÇA SUA JOGADA:'))

#Valida a escolha do jogador
if jogador1 < 1 or jogador1 > 3:
    print('Insira um valor válido')
    exit()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

#Escolha do computador
computador = random.choice(range(1, 4))
print('-='*15)
if computador == 1:
    print('O COMPUTADOR jogou PEDRA.')
elif computador == 2:
    print('O COMPUTADOR jogou PAPEL.')
else:
    print('O COMPUTADOR jogou TESOURA.')
if jogador1 == 1:
    print('O {} jogou PEDRA.'.format(nomejogador))
elif jogador1 == 2:
    print('O {} jogou PAPEL.'.format(nomejogador))
else:
    print('O {} jogou TESOURA.'.format(nomejogador))
print('-='*15)

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

