alunos = {}
alunos['Nome'] = str(input('Nome: '))
alunos['Média'] = float(input(f'Média de {alunos['Nome']}: '))
if alunos['Média'] <= 6:
    alunos['Situação'] = 'Reprovado(a).'
else:
    alunos['Situação'] = 'Aprovado(a)!'
for k, v in alunos.items():
    print(f'{k} é igual a {v}')
