#print(x)
# NameError: name 'x' is not defined
    # Variável não inicilizada


#n = int(input('Número: '))
#print(f'Você digitou o número {n}')
#  ValueError: invalid literal for int() with base 10: 'oito'
    #  Erro de valor acaontece pois o programa esperava receber um int e recebeu string

#a = int(input('Numerador: '))
#b = int(input('Denominador: '))
#r = a / b
#print(f'O resultado é {r}')
# ZeroDivisionError: division by zero
    # Erro de divisão por zero


#a = int(input('Numerador: '))
#b = str(input('Denominador: '))
#r = a / b
#print(f'O resultado é {r}')
# TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # Erro causado por tipos diferentes

#lst = [3, 6, 4]
#print(lst[3])
# IndexError: list index out of range
    # Erro causado pois o indice 3 não existe

# --- try e except

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')