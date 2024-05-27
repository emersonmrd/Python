pessoas = []
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