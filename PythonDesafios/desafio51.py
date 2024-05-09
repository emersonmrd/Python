"""print('RESOLVENDO PAs')
a1 = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão da PA: '))
termo = int(input('Insira até que termo deseja encontrar: '))
for c in range(1,termo+1):
    an = a1 + (c-1)*r
    print('O {}º termo da PA vale {}.'.format(c,an))"""

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' ->')
print('ACABOU')
