"""pessoas = []
dados = []
resposta = 'S'
totpessoas = 0
maiorp = menorp = 0
pessoas_pesadas = []
pessoas_leves = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    totpessoas += 1
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while True:
        if resposta in 'SN':
            break
    if resposta in 'N':
        break
for i, pessoa in enumerate(pessoas):
    for j, dado in enumerate(pessoa):
        if i == 0 and j == 1:
            maiorp = dado
            menorp = dado
        if j % 2 != 0:
            if dado > maiorp:
                maiorp = dado
                pessoas_pesadas.clear()
            if dado < menorp:
                menorp = dado
                pessoas_leves.clear()
        if dado == maiorp:
            j = j - 1
            pessoas_pesadas.append(pessoas[i][j])
            j = j + 1
        if dado == menorp:
            j = j - 1
            pessoas_leves.append(pessoas[i][j])
            j = j + 1

print('-=' * 30)
print(f'Foram cadastradas o total de {totpessoas} pessoas.')
print(f'O maior peso foi {maiorp:.2f}Kg. Sendo o peso de: ', end='')
for p in pessoas_pesadas:
    print(p, end=' ')
print(f'\nO menor peso foi {menorp:.2f}Kg. Sendo o peso de: ', end='')
for p in pessoas_leves:
    print(p, end=' ')
"""

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
