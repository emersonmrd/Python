from time import sleep
print('MENUZIN')
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    opcao = int(input('>>>>>> Selecione uma opção abaixo:\n'
                      '[1]SOMAR\n'
                      '[2]MULTIPLICAR\n'
                      '[3]MAIOR\n'
                      '[4]NOVOS NÚMEROS\n'
                      '[5]SAIR DO PROGRAMA\n'
                      'Digite aqui: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} vale {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            print('O maior entre {} e {} é {}'.format(n1, n2, n1))
        elif n2 > n1:
            print('O maior entre {} e {} é {}'.format(n1, n2, n2))
        else:
            print('Os valores {} e {} são iguais.'.format(n1, n2))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Você escolheu sair do programa.Volte sempre!')