print('COMPARADOR DE NÚMEROS\n')
num1 = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo número: '))

if num1 > num2:
    print('O primeiro valor é MAIOR!')
elif num1 < num2:
    print('O segundo valor é MAIOR!')
elif num1 == num2:
    print('Não existe valor maior, os dois são IGUAIS.')

