'''pessoas = []
pessoa = {}
resposta = ''


while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print("Entrada inválida! Por favor, digite 'M' ou 'F'.")
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resposta in 'SN':
            break
        print("Entrada inválida! Por favor, digite 'S' ou 'N'.")
    if resposta == 'N':
        break

print('-=' * 30)

print(f'- O grupo tem {len(pessoas)} pessoas.')

total_idade = sum(p['idade'] for p in pessoas)
media_idade = total_idade / len(pessoas)
print(f'- A média de idade é de {media_idade:.2f} anos')

print('- As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')

print()

print(f'- Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] > media_idade:
        print(f'\nNome = {p["nome"]}; Sexo = {p["sexo"]}; Idade = {p["idade"]};')
print('<< ENCERRADO >>')
'''

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp in 'N':
            break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')