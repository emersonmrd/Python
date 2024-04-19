valorProduto = float(input('Digite o valor do produto: '))
desconto = (5 * valorProduto)/100
novoValorProduto = valorProduto - desconto
print('Recebendo o valor de {} R$ de desconto, o Produto saí por {} R$'.format(desconto, novoValorProduto))