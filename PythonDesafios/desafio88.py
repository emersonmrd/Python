from time import sleep
from random import randint
print('-' * 30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-' * 30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'SORTEANDO {jogos} JOGOS')
jogo = []
c = 0
while c < jogos:
    while len(jogo) <= 6:
        num = randint(1,60)
        if num not in jogo:
            jogo.append(num)
    print(f'Jogo {c+1}: {jogo}')
    sleep(1)
    jogo.clear()
    c += 1
print(f'{'< BOA SORTE! >':^30}')