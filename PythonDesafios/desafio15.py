dias = int(input('Quantos dias alugados? '))
Km = float(input('Quantos Km rodados? '))
valorDias = dias * 60
valorKm = Km * 0.15
total = valorKm + valorDias
print('O total a pagar é de R${:.2f}'.format(total))
