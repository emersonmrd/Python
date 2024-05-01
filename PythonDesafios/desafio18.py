import math
ang = float(input('Insira o ângulo desejado: '))
print('O valor do Cosseno é {:.2f}\n'
      'O valor do Seno é {:.2f}\n'
      'O valor da Tangente é {:.2f}'.format(math.sin(math.radians(ang)),math.cos(math.radians(ang)), math.tan(math.radians(ang))))