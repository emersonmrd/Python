"""#num = (2, 5, 9, 1)
#num[2] = 3 -> não é possivel pois tuplas são imutaveis
num = [2, 5, 9, 1]
print(num)
num[2] = 3 # -> aqui funciona pois lista são mutaveis
print(num)
#num[4] = 7 -> não é possivel adicionar valores dessa forma, nesse caso basta usar o append
num.append(7)
print(num)
num.sort() #-> coloca em ordem crescente/alfabetica
print(num)
num.sort(reverse=True) #-> coloca em ordem descrescente/alfabetica
print(num)
num.insert(2, 0) # -> adiciona valores em uma posição desejada
print(num)
num.pop() # -> deleta o último valor da lista
print(num)
num.pop(2) # -> delta o elemento com indice desejado
print(num)
num.insert(2, 2) #-> adicionando um valor repetido na lista
print(num)
num.remove(2) # -> deleta a primeira ocorrencia do valor
print(num)
#num.remove(4) -> não é possivel remover um valor que não existe na lista par isso basta usar um if
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(f'Essa lista tem {len(num)} elementos.') #len(num) mostra o tamanho da lista
"""
# Lista podem ser criadas valores = [] ou valores = list()

"""
valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)

for cont in range(0,5):
    valores.append(int((input('Digite um valor:'))))

#for valor in valores:
    #print(f'{valor}...', end='')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
"""

a = [2, 3, 4, 7]
#b = a #-> cria uma ligação de listas
b = a[:] # -> cria uma copia de lista
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')