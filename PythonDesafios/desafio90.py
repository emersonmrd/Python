"""alunos = {}
alunos['Nome'] = str(input('Nome: '))
alunos['Média'] = float(input(f'Média de {alunos['Nome']}: '))
if alunos['Média'] <= 6:
    alunos['Situação'] = 'Reprovado(a).'
else:
    alunos['Situação'] = 'Aprovado(a)!'
for k, v in alunos.items():
    print(f'{k} é igual a {v}')"""

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')