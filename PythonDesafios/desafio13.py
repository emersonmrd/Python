salario = float(input('Digite seu salario: R$'))
aumento = (15 * salario)/100
novoSalario = salario + aumento
print('Considerando o aumento de {:.2f} R$, o seu novo salario passa a ser {:.2f} R$.'.format(aumento, novoSalario))