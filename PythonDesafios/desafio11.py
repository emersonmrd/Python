largura = float(input('Insira a largura da parede em (m): '))
altura = float(input('Insira a altura da parede em (m): '))
area = largura * altura
litrosTinta = area/2
print('Considerando que a área é {} m², Para pintar essa parede será necessario {} (l) de tinta.'.format(area, litrosTinta))