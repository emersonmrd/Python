def metade(numero, formatado=True):
    metade = numero / 2
    if formatado:
        return f'R${metade:.2f}'.replace('.', ',')
    else:
        return metade


def dobro(numero, formatado=True):
    dobro = numero * 2
    if formatado:
        return f'R${dobro:.2f}'.replace('.', ',')
    else:
        return dobro


def aumentar(numero, porcentagem_Aumento, formatado=True):
    aumento_percentual = numero * (porcentagem_Aumento/100)
    aumento = aumento_percentual + numero
    if formatado:
        return f'R${aumento:.2f}'.replace('.', ',')
    else:
        return aumento

def diminuir(numero, porcentagem_Reducao, formatado=True):
    reducao_percentual = numero * (porcentagem_Reducao/100)
    reducao = numero - reducao_percentual
    if formatado:
        return f'R${reducao:.2f}'.replace('.', ',')
    else:
        return reducao

def moeda(numero):
    return f'R${numero:.2f}'.replace('.',',')


def resumo(numero, porcentagem_Aumento,porcentagem_Reducao):
    txt = f'RESUMO DO VALOR'
    print('-' * 30)
    print(f'{txt:^30}')
    print('-' * 30)
    txt = f'Preço analisado:'
    print(f'{txt:<16} {moeda(numero):^15}')
    txt ='Dobro do preço:'
    print(f'{txt:<16} {dobro(numero):^15}')
    txt = 'Metade do preço:'
    print(f'{txt:<16} {metade(numero):^15}')
    txt = f'{porcentagem_Aumento}% de aumento:'
    print(f'{txt:<16} {aumentar(numero,porcentagem_Aumento):^15}')
    txt = f'{porcentagem_Reducao}% de redução:'
    print(f'{txt:<16} {diminuir(numero,porcentagem_Reducao):^15}')
    print('-' * 30)