def leiaInt(msg):
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
            print('\033[0;31mERRO: por favor, Digite um número inteiro válido.\033[m')


i = leiaInt('Digite um número Inteiro: ')
r = leiaReal('Digite um número Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')
#print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')