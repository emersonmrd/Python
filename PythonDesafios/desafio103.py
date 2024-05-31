'''def ficha(nome='<desconhecido>', gols=0):
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
print(ficha(nome_jogador, numero_gols))'''


def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols(s) no campeonato.')



# Programa Principal
n = str(input("Nome do Jogador: "))
g = str(input("Número de Gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)