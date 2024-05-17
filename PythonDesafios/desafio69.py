pessoas = homens = maior18 = mulheres_abaixo_vinte = 0
while True:
    print('-' * 30)
    titulo = 'CADASTRE UMA PESSOA'
    print(f'|{titulo:^28}|')
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade >= 18:
        maior18 += 1
    sexo = str(input('Sexo [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F] ')).strip().upper()[0]
    pessoas += 1
    if sexo == 'F' and idade < 20:
        mulheres_abaixo_vinte += 1
    if sexo == 'M':
        homens += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{' FIM DO PROGRAMA ':=^31}')
print(f'Foram cadastradas {pessoas} pessoas no total,')
print(f'Sendo {maior18} maiores de 18,')
print(f'com {homens} homens no total,')
print(f'e com {mulheres_abaixo_vinte} mulheres abaixo de 20 anos.')