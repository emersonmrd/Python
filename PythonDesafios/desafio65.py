maior = menor =totalnum = soma = 0
continuar = 'S'
while continuar in 'Ss':
    num = int(input('Digite um número: '))
    if totalnum == 1:
        maior = menor = num
    totalnum += 1
    soma += num
    if maior < num:
        maior = num
    if menor > num:
        menor = num
    continuar = str(input('Você deseja continuar? [S/N]')).upper().strip()[0]
media = soma/totalnum
print('Você digitou {} números e a média entre todos os valores digitados é de {}\n'
      'O maior valor digitado foi {} '
      'e o menor valor digitado foi {}'.format(totalnum,media,maior,menor))

