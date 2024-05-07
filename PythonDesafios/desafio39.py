from datetime import date
atual = date.today().year
print('SISTEMA DE ALISTAMENTO')
sexo = input('Qual é o seu sexo?\n'
             'M - Masculino\n'
             'F - Feminino\n'
             'Insira aqui: ').upper()

if sexo == 'F':
    print('Você não precisa participar do alistamento obrigatorio.')
    exit()
elif sexo != 'M':
    print('Valor invalido tente novamente.')
    exit()

anoNasc = int(input('Insira o ano do seu nascimento: '))

#Verifica se o ano de nascimento é válido
if anoNasc <= 1920 or anoNasc > 2024:
    print('Insira um valor válido.')
    exit()

idade = atual - anoNasc
if idade < 18:
    print('Você ainda vai se alistar ao serviço militar\n'
          'Falta {} anos para você se alistar'.format(18-idade))
    anoAlistamento = atual + (18-idade)
    print('Seu alistamento será em {}'.format(anoAlistamento))
elif idade == 18:
    print('Você deve se alistar esse ano ao serviço militar\n')
else:
    print('Você já deveria ter se alistado,\n'
          'Você esta {} anos fora do prazo'.format(idade - 18))
    anoAlistamento = atual - (idade - 18)
    print('Seu alistamento foi em {}'.format(anoAlistamento))