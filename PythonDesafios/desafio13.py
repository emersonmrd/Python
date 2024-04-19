salario = float(input('Digite seu salario: '))
aumento = (15 * salario)/100
novoSalario = salario + aumento
print('Considerando o aumento de {} R$, o seu novo salario passa a ser {} R$.'.format(aumento, novoSalario))