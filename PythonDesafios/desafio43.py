print('CALCULADORA DE IMC')
peso = float(input('Insira o seu peso (Kg): '))
altura = float(input('Insira a sua altura (m): '))
imc = peso / (altura**2)

print('Seu IMC é de {:.2f}.'.format(imc))
if imc < 18.5:
     print('Abaixo do Peso.')
elif imc < 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')