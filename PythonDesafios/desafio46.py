from time import sleep
print('CONTAGEM PARA OS FOGOS')
for c in range(10, 0, -1):
    if c == 1:
        print('Falta {} segundo para o show de fogos.'.format(c))
        sleep(1)
    else:
        print('Faltam {} segundos para o show de fogos.'.format(c))
        sleep(1)
print('BOOOMM!!!')
