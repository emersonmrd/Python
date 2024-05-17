"""cont = 1
while cont <= 10: #-> while True:
    print(cont, "-> ", end='')
    cont += 1
print('ACABOU')"""

"""n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
print('A soma vale {}'.format(s))"""

"""n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}')"""

nome = 'José'
idade = 33
salario = 987.35
print(f'O {nome:^20} tem {idade} anos e ganha R${salario:.2f}.') # Python 3.6+
print('O {} tem {} anos.'.format(nome,idade)) # Python 3
# Formatações
# {:20} Para usar 20 espaços
# {:^20} Para centralizar em 20 espaços
# {:-^20} Para centralizar em 20 tracinhos
# {:->20} Para colocar a direita em 20 tracinhos
# {:-<20} Para colocar a esquerda em 20 tracinhos