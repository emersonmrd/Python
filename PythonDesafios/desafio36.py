print('='*37)
print('|' + (' '*35) + '|')
print('| SISTEMA DE FINANCIAMENTO DE CASAS |')
print('|' + (' '*35) + '|')
print('='*37+'\n')

# Solicitar informações ao usuário
precoCasa = float(input('Qual é o valor da casa que você deseja financiar? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos você deseja pagar a casa? '))

# Verificar se anos é positivo
if anos <= 0:
    print('Por favor, insira um número de anos válido.')
    exit()

# Verificar se salario é positivo
if salario <= 0:
    print('Por favor, insira um valor de salario válido.')
    exit()

# Verificar se o valor da casa é positivo
if precoCasa <= 0:
    print('Por favor, insira um valor de casa válido.')
    exit()

meses = anos * 12
prestacao = precoCasa / meses
trintasalario = salario * (30/100)

# Verificar se o valor da prestação excede 30% do salário
if prestacao > trintasalario:
    print('Financiamento NEGADO devido ao valor da prestação mensal que é de {:.2f} R$ exceder 30% do salário que é de {:.2f} R$.'.format(prestacao, trintasalario))
else:
    print('Financiamento ACEITO, você pagará {:.2f} R$ por mês durante {} anos'.format(prestacao, anos))
