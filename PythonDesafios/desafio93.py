'''
aproveitamento = {}
lista_de_gols = []
total_de_gols = 0
aproveitamento['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {aproveitamento['nome']} jogou? '))
for c in range(1,(partidas+1)):
    gol = int(input(f'Quantos gols na partida {c}? '))
    lista_de_gols.append(gol)
    total_de_gols += gol
aproveitamento['gols'] = lista_de_gols.copy()
aproveitamento['total'] = total_de_gols
print('-=' * 30)
print(aproveitamento)
print('-=' * 30)
for k, v in aproveitamento.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {aproveitamento['nome']} jogou {partidas} partidas.')
for i, gols in enumerate(aproveitamento['gols']):
    print(f'    =>  Na partida {i + 1}, fez {gols} gols.')
print(f'Foi um total de {total_de_gols} gols.')
'''

jogador = dict()
partidas = []
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')
