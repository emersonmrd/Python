num = total = soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        total += 1
        soma += num
print('O total de números digitados foi de {} '
      'e a soma entre os números digitados vale {}.'.format(total, soma))
