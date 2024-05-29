'''
# Criação das funções
def linha():
    print('-' * 30)

def mensagem(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)

def titulo(txt):
    print('-' * 30)
    print(f'{txt:^30}')
    print('-' * 30)

# Programa principal

# Sem usar a função linha()
print('-' * 30)
print(f'{"CURSO EM VÍDEO":^30}')
print('-' * 30)
print('-' * 30)
print(f'{"APRENDA PYTHON":^30}')
print('-' * 30)
print('-' * 30)
print(f'{"EMERSON RODRIGUES":^30}')
print('-' * 30)

# Usando a função linha()
linha()
print(f'{"CURSO EM VÍDEO":^30}')
linha()
linha()
print(f'{"APRENDA PYTHON":^30}')
linha()
linha()
print(f'{"EMERSON RODRIGUES":^30}')
linha()

# Sem usar a função mensagem()
linha()
print(f'{"SISTEMA DE ALUNOS":^30}')
linha()

# Usando a função mensagem()
mensagem("SISTEMA DE ALUNOS")

# Sem usar a função titulo()
linha()
print(f'{"CURSO EM VÍDEO":^30}')
linha()
linha()
print(f'{"APRENDA PYTHON":^30}')
linha()
linha()
print(f'{"EMERSON RODRIGUES":^30}')
linha()


# Usando a função titulo
titulo("CURSO EM VÍDEO")
titulo("APRENDA PYTHON")
titulo("EMERSON RODRIGUES")



# Sem função
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

print('-=' * 30)

# Com função
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

soma(4, 5)
print()
soma(8, 9)
print()
soma(2, 1)
print()
#soma(4) -> se ocorrer se passar parâmetros de forma incorreta, ocorre erros
# é possivel passar parâmetros de forma explicita:
soma(a=4,b=6)
print()
soma(b=4,a=6)
# soma(a=4, 6) -> algo assim não funciona
# soma(3, 9, 5) -> algo assim também não funciona


def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')
    #for valor in num:
        #print(f'{valor} ', end='')
    #print('FIM')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)
'''

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)