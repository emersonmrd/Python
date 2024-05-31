'''def leiaInt(txt):
    valor = input(txt)
    while True:
        if valor.isnumeric():
            return int(valor)
            break
        else:
            print(f'ERRO! Digite um número inteiro válido.')
            valor = input(txt)


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')'''


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')