n = str(input('Digite um valor: '))
n1 = int(n)
n2 = float(n1)
n3 = bool(n2)
print(type(n))
print(type(n1))
print(type(n2))
print(type(n3))

n4 = input('Digite algo: ')
print(n4.isnumeric())

n5 = input('Digite algo: ')
print(n5.isalpha())

n6 = input('Digite algo: ')
print(n6.isalnum())
