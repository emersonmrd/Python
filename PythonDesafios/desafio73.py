times_brasileirao = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
                     'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo',
                     'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense',
                     'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí',
                     'Ponte Preta', 'Atlético-GO')
print('-=' * 30)
print(f'Lista de times do Brasileirão: {times_brasileirao}')
print('-=' * 30)
print(f'Os 5 primeiros são: {times_brasileirao[:5]}')
print('-=' * 30)
print(f'Os 4 últimos são: {times_brasileirao[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(times_brasileirao)}')
print('-=' * 30)
print(f'O Chapecoense está na {(times_brasileirao.index('Chapecoense')+1)}ª posição')
