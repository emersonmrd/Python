print('SISTEMA DE ALISTAMENTO')
anoNasc = int(input('Insira o ano do seu nascimento: '))

#Verifica se o ano de nascimento é válido
if anoNasc <= 1920 or anoNasc > 2024:
    print('Insira um valor válido.')
    exit()

idade = 2024 - anoNasc
if idade < 18:
    print('Você ainda vai se alistar ao serviço militar\n'
          'Falta {} anos para você se alistar'.format(18-idade))
elif idade == 18:
    print('Você deve se alistar esse ano ao serviço militar\n')
else:
    print('Já passou o tempo do alistamento\n'
          'Você esta {} anos fora do prazo'.format(idade - 18))