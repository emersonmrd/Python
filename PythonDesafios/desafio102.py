'''def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    expressao = ''
    print('-' * 30)
    if show == False:
        for c in range(n, 0, -1):
            f *= c
        return f
    elif show == True:
        for c in range(n, 0, -1):
            f *= c
            if c != 1:
               expressao += f'{c} x '
            else:
                expressao += f'{c} = '
        return expressao + str(f)


print(fatorial(6, show=False))
print(fatorial(6, show=True))
help(fatorial)
'''


def fatorial(n, show=False):
    '''
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
print(fatorial(5, show=False))
help(fatorial)