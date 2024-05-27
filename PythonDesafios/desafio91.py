from random import randint
from time import sleep

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

