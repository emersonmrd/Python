print('-' * 30)
print(f'|{'LOJAS SUPER BARATÃO':^28}|')
print('-' * 30)
total_gasto = 0
maior_mil = 0
mais_barato = 0
nome_mais_barato = ''
while True:
    nome_produto = str(input('Nome do Produto: '))
    preco_produto = float(input('Preço: R$'))
    if mais_barato == 0:
        mais_barato = preco_produto
    if preco_produto < mais_barato:
        mais_barato = preco_produto
        nome_mais_barato = nome_produto
    total_gasto += preco_produto
    if preco_produto > 1000:
        maior_mil += 1
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{'FIM DO PROGRAMA':-^30}')
print(f'O total da compra foi R${total_gasto:.2f}')
print(f'Temos {maior_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_mais_barato} que custa R${mais_barato:.2f}')