def leiaInt(txt):
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
print(f'Você acabou de digitar o número {n}')

