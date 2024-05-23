alunos = []
dados_alunos = []
informacao = []
resposta = 'S'
num = 0
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    dados_alunos.append(nome)
    informacao.append(nota1)
    informacao.append(nota2)
    informacao.append(media)
    dados_alunos.append(informacao[:])
    informacao.clear()
    alunos.append(dados_alunos[:])
    dados_alunos.clear()
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()
    while True:
        if resposta in 'SN':
            break
    if resposta in 'N':
        break
print('-=' * 30)
print(f'{'No.':<3}', end=' ')
print(f'{'NOME':<17}',end=' ')
print(f'{'MÉDIA':^10}')
print('-' * 30)
for i, aluno in enumerate(alunos):
    no = i
    nome = alunos[i][0]
    media = alunos[i][1][2]
    print(f'{no:<3}', end='')
    print(f'{nome:<17}', end='')
    print(f'{media:>7}')
print('-' * 30)
while True:
    num = int(input('Mostrar notas de qual aluno? (999 interrompe):  '))
    if num == 999:
        break
    print(f'Notas de {alunos[num][0]} são {alunos[num][1][0]} e {alunos[num][1][1]}')
print('FINALIZANDO...')
print(f'{'VOLTE SEMPRE'}')

