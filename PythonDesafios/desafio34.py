salario = float(input('Digite o valor do sálario: '))
if salario > 1250:
    aumento = salario * (10/100)
    novoSalario = salario + aumento
else:
    aumento = salario * (15 / 100)
    novoSalario = salario + aumento
print('Você recebeu um aumento de {:.2f} R$, sendo assim\n'
          'seu novo salário é de {:.2f} R$'.format(aumento, novoSalario))
