jogadores = []
aproveitamento = {}
resposta = ''
lista_de_gols = []
total_de_gols = 0
while True:

    print('-' * 30)
    aproveitamento['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {aproveitamento['nome']} jogou? '))
    for c in range(1,(partidas+1)):
        gol = int(input(f'Quantos gols na partida {c}? '))
        lista_de_gols.append(gol)
        total_de_gols += gol
    aproveitamento['gols'] = lista_de_gols.copy()
    aproveitamento['total'] = total_de_gols
    lista_de_gols.clear()
    total_de_gols = 0
    jogadores.append(aproveitamento.copy())
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta in 'N':
        break
print('-=' * 30)
print(f'{"cod":<4} {"nome":<16} {"gols":<15} {"total":<5}')
print('--' * 30)
for c, j in enumerate(jogadores):
    print(f'{c:<4} {j["nome"]:<16} {str(j["gols"]):<15} {j["total"]:<5}')

while True:
    print('--' * 30)
    num = int(input('Mostrar dados de qual jogador? (999 Encerra) '))
    if num not in jogadores:
        print(f'ERRO! Não existe jogador com código 5! Tente novamente')
    for c, j in enumerate(jogadores):
        if c == num:
            print(f'-- LEVANTAMENTO DO JOGADOR {j['nome']}')
            for i, gols in enumerate(j['gols']):
                print(f'No jogo {i + 1}, fez {gols} gols.')
    if num == 999:
        break
print('<< VOLTE SEMPRE >>')