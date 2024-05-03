velocidade = int(input('Qual foi a velocidade detectada do veiculo? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Sua velocidade foi de {} Km/h\n'
          'Você foi multado em {:.2f}R$\n'
          'Dirija com cuidado!'. format(velocidade, multa))
else:
    print('Sua velocidade foi de {} Km/h\n'
          'Você não ultrapassou os 80 Km/h\n'
          'Dirija com  cuidado!'.format(velocidade))
