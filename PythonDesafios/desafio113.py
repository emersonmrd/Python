'''def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg).strip())
            return valor
        except KeyboardInterrupt:
            print()
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            valor = 0
            return valor
        except:
            print('\033[0;31mERRO: por favor, Digite um número inteiro válido.\033[m')

def leiaReal(msg):
    while True:
        try:
            valor = float(input(msg).strip().replace(',', '.'))
            return valor
        except KeyboardInterrupt:
            print()
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            valor = 0
            return valor
        except:
            print('\033[0;31mERRO: por favor, Digite um número real válido.\033[m')


i = leiaInt('Digite um número Inteiro: ')
r = leiaReal('Digite um número Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')
#print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

n1 = leiaInt('Digite um número Inteiro: ')
n2 = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')