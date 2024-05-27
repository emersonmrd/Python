from random import randint
from time import sleep
'''
jogadores = []
jogador = {}

for c in range(1,5):
    jogador['nome'] = f'jogador{c}'
    jogador['resultado'] = randint(1,6)
    jogadores.append(jogador.copy())
print('Valores sorteados: ')
for j in jogadores:
    sleep(1.7)
    for k, v in j.items():
        if k == 'nome':
            print(f'O {v} tirou', end=' ')
        else:
            print(f'{v}')
ranking_jogadaores = sorted(jogadores, key=lambda x: x['resultado'], reverse=True)
contador = 1
print('Ranking dos jogadores: ')
for j in ranking_jogadaores:
    sleep(1.7)
    for k, v in j.items():
        if k == 'nome':
            print(f'O {contador}º lugar: {v} com', end=' ')
            contador += 1
        else:
            print(f'{v}')
'''

from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}

ranking = list()


print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
