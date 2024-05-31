def metade(numero, formatado=False):
    metade = numero / 2
    if formatado:
        return f'R${metade:.2f}'.replace('.', ',')
    else:
        return metade


def dobro(numero, formatado=False):
    dobro = numero * 2
    if formatado:
        return f'R${dobro:.2f}'.replace('.', ',')
    else:
        return dobro


def aumentar(numero, porcentagem, formatado=False):
    aumento_percentual = numero * (porcentagem/100)
    aumento = aumento_percentual + numero
    if formatado:
        return f'R${aumento:.2f}'.replace('.', ',')
    else:
        return aumento

def diminuir(numero, porcentagem, formatado=False):
    reducao_percentual = numero * (porcentagem/100)
    reducao = numero - reducao_percentual
    if formatado:
        return f'R${reducao:.2f}'.replace('.', ',')
    else:
        return reducao

def moeda(numero):
    return f'R${numero:.2f}'.replace('.',',')
