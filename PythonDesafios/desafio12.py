valorProduto = float(input('Digite o valor do produto: '))
desconto = (5 * valorProduto)/100
novoValorProduto = valorProduto - desconto
print('Recebendo o valor de {:.2f} R$ de desconto, o Produto saí por {:.2f} R$'.format(desconto, novoValorProduto))