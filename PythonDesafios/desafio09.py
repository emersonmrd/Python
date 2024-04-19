valor = int(input('Digite um valor: '))
print('='*17)
print('| TABUADA DO {} |'.format(valor))
print(
    '| {} x  1 = {}  |\n'
    '| {} x  2 = {}  |\n'
    '| {} x  3 = {}  |\n'
    '| {} x  4 = {}  |\n'
    '| {} x  5 = {}  |\n'
    '| {} x  6 = {}  |\n'
    '| {} x  7 = {}  |\n'
    '| {} x  8 = {}  |\n'
    '| {} x  9 = {}  |\n'
    '| {} x 10 = {} |'
    .format(valor, valor *1,valor, valor *2,valor, valor *3
            ,valor, valor *4,valor, valor *5,valor, valor *6,valor, valor *7,
            valor, valor *8,valor, valor *9,valor, valor *10,))
print('='*17)