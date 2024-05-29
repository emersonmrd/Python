from datetime import datetime

ano_Atual = datetime.now().year
def voto(nascimento):
    idade = ano_Atual - nascimento
    if idade >= 18 and idade <= 64:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    elif idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        print(f'Com {idade} anos: NÃO VOTA.')


print('-' * 30)
ano_nasc = int(input('Em que ano você nasceu? '))
voto(ano_nasc)