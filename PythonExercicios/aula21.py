'''def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

help(contador)

def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    """

    s = a + b + c
    print(f'A soma vale {s}')

somar()
somar(2)
somar(2, 3)
somar(2,3,4)
somar(b=4, c=2)


def teste():
    x = 8 # -> variavel local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa Principal
n = 2 # -> variavel global
print(f'No progama principal, n vale {n}')
teste()
#print(f'No progama principal, x vale {x}') -> vai causar erro devido a escopo de variavel


def teste(b):
    b += 4
    c = 2
    print(f'A dentro vale {a}') #-> mostra o valor da variavel global
    print(f'B dentro vale {b}') #-> mostra o valor da variavel a que foi passada por parâmetro + o valor 4
    print(f'C dentro vale {c}') #-> mostra o valor da variavel local

a = 5
teste(a)
print(f'A fora vale {a}') #-> mostra o valor da variavel global
#print(f'B fora vale {b}') #-> vai causar erro devido a escopo de variavel
#print(f'B fora vale {c}') #-> vai causar erro devido a escopo de variavel

def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}') #-> mostra o valor da variavel local
    print(f'B dentro vale {b}') #-> mostra o valor da variavel a que foi passada por parâmetro + o valor 4
    print(f'C dentro vale {c}') #-> mostra o valor da variavel local

a = 5
teste(a)
print(f'A fora vale {a}') #-> mostra o valor da variavel global
#print(f'B fora vale {b}') #-> vai causar erro devido a escopo de variavel
#print(f'B fora vale {c}') #-> vai causar erro devido a escopo de variavel



def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 global vale {n1}')


def teste(b):
    global a # -> comando para o programa não criar uma variavel local mas sim usar a global
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}') #-> mostra o valor da variavel global devido ao comando global a
    print(f'B dentro vale {b}') #-> mostra o valor da variavel a que foi passada por parâmetro + o valor 4
    print(f'C dentro vale {c}') #-> mostra o valor da variavel local

a = 5
teste(a)
#mostra o valor da variavel global contudo com valor alterado pela funcao devido ao comando global:
print(f'A fora vale {a}')
#print(f'B fora vale {b}') #-> vai causar erro devido a escopo de variavel
#print(f'B fora vale {c}') #-> vai causar erro devido a escopo de variavel


def somar(a=0,b=0,c=0):
    s = a + b + c
    return s # -> retorno de valores

resp0 = somar(3,2,5)
resp1 = somar(2,2)
resp2 = somar(6)
print(f'Meus cálculos deram {resp0}, {resp1} e {resp2}.')


def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


#n = int(input('Digite um número: '))
#print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
'''

def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')