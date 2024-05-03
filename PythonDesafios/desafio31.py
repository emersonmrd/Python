distancia = int(input('Qual é a distancia em Km da sua viajem?'))
if distancia <= 200:
    passagem = distancia * 0.5
    print('Devido a distancia {} Km, sua passagem custa {:.2f} R$'.format(distancia, passagem))
else:
    passagem = distancia * 0.45
    print('Devido a distancia {} Km, sua passagem custa {:.2f} R$'.format(distancia, passagem))