num0 = int(input('Digite um número: '))
num1 = int(input('Digite outro número: '))
num2 = int(input('Digite mais um número: '))
num3 = int(input('Digite o último número: '))
tupla = (num0, num1, num2, num3)
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if tupla.count(3) != 0:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
if tupla.count(3) == 0:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
tem_pares = False
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
        tem_pares = True
if not tem_pares:
    print('nenhum.')