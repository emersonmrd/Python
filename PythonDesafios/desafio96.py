"""def area(l, c):
    a = l * c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {a:.1f}m².')

print(f'{" Controle de Terrenos ":^30}')
print('-' * 32)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)"""

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg:.1f}x{comp:.1f} é de {a:.1f}m².')

#Programa Principal
print(' Controle de Terrenos ')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
