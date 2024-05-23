"""from time import sleep
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
"""

from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('       JOGA NA MEGA SENA      ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
