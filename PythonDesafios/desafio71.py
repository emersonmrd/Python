print('=' * 30)
print(f'{'BANCO PLEBES':^30}')
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO PLEBES! Tenha um bom dia!')





"""numero = int(input('Qual valor você quer sacar? R$'))
resto50 = numero // 50
valor50 = resto50 * 50
restante50 = numero - valor50
resto20 = restante50 // 20
valor20 = resto20 * 20
restante20 = restante50 - valor20
resto10 = restante20 // 10
valor10 = resto10 * 10
restante10 = restante20 - valor10
resto1 = restante10 // 1
if resto50 != 0:
    print(f'Total de {resto50} cédulas de R$50')
if resto20 != 0:
    print(f'Total de {resto20} cédulas de R$20')
if resto10 != 0:
    print(f'Total de {resto10} cédulas de R$10')
if resto1 != 0:
    print(f'Total de {resto1} cédulas de R$1')
print('=' * 30)
print('Volte sempre ao BANCO PLEBES! Tenha um bom dia!')"""
