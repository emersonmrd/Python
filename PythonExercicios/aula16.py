#lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tuplas são imutáveis
# Formas de fatiamento de tuplas:
#print(lanche[1]) -> Mostra com valor positivo
#print(lanche[-3]) -> Mostra com valor negativo
#print(lanche[1:3]) -> Mostra do primeiro valor até o segundo valor
#print(lanche[2:]) -> Mostra do segundo elemento até o final
#print(lanche[:2]) -> Mostra do primeiro elemento até o primeiro elemento, da pra usar com valores negativos
#print(len(lanche)) -> Mostra o tamanho da tupla

# Forma de varrer a tupla:
#for comida in lanche:
    #print(f'Eu vou comer {comida}')
#print('Comi pra caramba!')

# outra forma de varrer a tupla é:
#for cont in range(0, len(lanche)):
    #print(f'Eu vou comer {lanche[cont]} na posição {cont}')
#print('Comi pra caramba!')

# Forma de varrer a tupla mostrando a posição:
#for pos, comida in enumerate(lanche):
    #print(f'Eu vou comer {comida} e na posição {pos}')
#print('Comi pra caramba!')

#print(sorted(lanche)) -> coloca em ordem

#a = (2, 5, 4)
#b = (5, 8, 1, 2)
#c = a + b # Essa operação resulta em -> (2, 5, 4, 5, 8, 1, 2)
#c = b + a # Essa operação resulta em -> (5, 8, 1, 2, 2, 5, 4) pois a ordem afeta
# metodo print(c.count(5)) -> conta quantas vezes um evento acontece
# metodo print(c.index(5)) -> mostra em que posição um elemento esta
# metodo print(c.index(5, 1)) -> mostra em que posição um elemento esta a partir de uma determinada posição
#print(c)

# Tuplas armazenam mais de um tipo de valor como str,int e float
pessoa = ('Gustavo', 39, 'M', 99.88)
# metodo del(pessoa) -> apaga uma tupla
print(pessoa)