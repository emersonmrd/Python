import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hp = math.hypot(co,ca)
print('O valor da hipotenusa desse triangulo é {:.2f}'.format(hp))

'''co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hp = (co**2 + ca**2)**(1/2)
print('O valor da hipotenusa desse triangulo é {:.2f}'.format(hp))'''