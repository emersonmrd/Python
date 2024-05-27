from datetime import datetime

contribuinte = {}
ano_atual = datetime.now().year


contribuinte['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
contribuinte['idade'] = ano_atual - ano_nasc
contribuinte['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if contribuinte['ctps'] != 0:
    contribuinte['contratação'] = int(input('Ano de contratação: '))
    contribuinte['salário'] = float(input('Salário: R$  '))
    contribuinte['aposentadoria'] = (contribuinte['contratação'] + 35) - ano_nasc
print('-=' * 30)
print(contribuinte)
for k, v in contribuinte.items():
    print(f'{k} tem o valor {v}')