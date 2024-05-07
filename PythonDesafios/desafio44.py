print('SISTEMA DE PAGAMENTO')
precoProduto = float(input('Insira o valor do produto: '))
opcao = int(input('SELECIONE A FORMA DE PAGAMENTO\n'
      '0 - Cancelar Compra\n'
      '1 - Á vista Dinheiro/Chque 10% de desconto\n'
      '2 - Á vista Cartão 5% de desconto\n'
      '3 - Em até 2x no cartão sem desconto\n'
      '4 - 3x ou mais no cartão 20% de juros\n'
      'Digite aqui: '))

if opcao < 0 or opcao > 4:
    print('Forma de pagamento inválida, tente novamente.')
    exit()
elif opcao == 0:
    print('Volte sempre!')
elif opcao == 1:
    desconto = precoProduto * (10/100)
    print('O valor do produto é de {:.2f} R$, você recebeu {:.2f} R$ de desconto.\n'
          'O produto sairá por {:.2f} R$.'.format(precoProduto, desconto, precoProduto-desconto))
elif opcao == 2:
    desconto = precoProduto * (5 / 100)
    print('O valor do produto é de {:.2f} R$, você recebeu {:.2f} R$ de desconto.\n'
          'O produto sairá por {:.2f} R$.'.format(precoProduto, desconto, precoProduto - desconto))
elif opcao == 3:
    print('O produto sairá por {:.2f} R$.\n'
          'Cada parcela sairá por {:.2f} R$'.format(precoProduto, precoProduto / 2))
elif opcao == 4:
    parcelas = int(input('Insira o número de parcelas: '))
    juros = precoProduto * (20 / 100)
    precoProdutoJur = precoProduto + juros
    print('O valor do produto é de {:.2f} R$ contudo devido a forma de pagamento,\n'
          'O produto sairá por {:.2f} R$.\n'
          'Cada parcela sairá por {:.2f} R$'.format(precoProduto, precoProdutoJur, precoProdutoJur / parcelas))
else:
    print('Ocorreu um erro tente novamente!')