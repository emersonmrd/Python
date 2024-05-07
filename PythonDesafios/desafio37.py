print('SISTEMA DE CONVERSÃO DE BASES\n')
num = int(input('Digite o número que deseja converter.\n'
                'Número:'))
base = int(input('Escolha para qual base deseja a conversão:\n'
                 '1 - Binário\n'
                 '2 - Octal\n'
                 '3 - Hexadecimal\n'
                 'Digite aqui:'))
print(base)

#Verifica se o valor de base é válido
if base != 1 and base != 2 and base != 3:
    print('Valor digitado inválido tente novamente.')
    exit()

if base == 1:
    binario = bin(num)
    print('O número {} em binário é: {}'.format(num, binario[2:]))
elif base == 2:
    octal = oct(num)
    print('O número {} em binário é: {}'.format(num, octal[2:]))
elif base == 3:
    hexadicimal = hex(num)
    print('O número {} em binário é: {}'.format(num, hexadicimal[2:]))
else:
    print('Ocorreu um erro tente novamente.')

