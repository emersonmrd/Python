print('Vamos verificar se 3 retas podem ou não formar um triângulo.')
reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))
#condição triângulo
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Essas 3 retas podem formar um triângulo.')
else:
    print('Essas 3 retas não podem formar um triângulo.')