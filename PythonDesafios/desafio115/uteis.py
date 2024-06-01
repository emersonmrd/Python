from time import sleep
def menuPrincipal():
    sleep(0.5)
    print('-' * 40)
    print(f'{"MENU PRINCIPAL":^40}')
    print('-' * 40)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do Sistema')
    print('-' * 40)

def pessoasCadastradas():
    sleep(1)
    try:
        with open('pessoas.txt', 'r') as pessoas:
            conteudo = pessoas.read().strip()
            print('-' * 40)
            print(f'{"PESSOAS CADASTRADAS":^40}')
            print('-' * 40)
            print(conteudo)
    except FileNotFoundError:
            print('-' * 40)
            print(f'{"PESSOAS CADASTRADAS":^40}')
            print('-' * 40)
            print('Nenhuma pessoa cadastrada ainda.')
            print('-' * 40)  # Adicionar linha de fechamento
def cadastrarPessoa():
    sleep(1)
    print('-' * 40)
    print(f'{"NOVO CADASTRO":^40}')
    print('-' * 40)
    nome = str(input('Nome: '))
    while True:
        print('O campo \'NOME\' não pode estar vazio.')
        nome = str(input('Nome: '))
        if nome not in '':
            break
    idade = leiaInt('Idade: ')
    formatado = f'{nome:<27} {idade:<2} anos'
    with open('pessoas.txt', 'a') as pessoas:
        pessoas.write(formatado +'\n')
    print(f'Novo registro de {nome} adicionado.')

def sairSistema():
    sleep(1)
    print('-' * 40)
    print(f'{"Saindo do sistema... Até logo!":^40}')
    print('-' * 40)

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