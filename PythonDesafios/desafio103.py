def ficha(nome='<desconhecido>', gols=0):
    expressao = f'O jogador {nome} fez {gols} gol(s) no campeonato.'
    return expressao


print('-' * 30)
nome_jogador = input('Nome do jogador: ')
numero_gols = input('Números de Gols: ')
if nome_jogador == '':
    nome_jogador = '<desconhecido>'
if numero_gols == '':
    numero_gols = 0
else:
    numero_gols = int(numero_gols)
print(ficha(nome_jogador, numero_gols))