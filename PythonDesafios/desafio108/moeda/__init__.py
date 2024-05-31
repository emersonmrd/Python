def metade(numero):
    return numero / 2


def dobro(numero):
    return numero * 2


def aumentar(numero, porcentagem):
    aumento = numero * (porcentagem/100)
    return aumento + numero

def diminuir(numero, porcentagem):
    reducao = numero * (porcentagem/100)
    return numero - reducao

def moeda(numero):
    return f'R${numero:.2f}'.replace('.',',')
