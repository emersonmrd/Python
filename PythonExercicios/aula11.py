#STYLE 0 (None),1 (Bold),4 (Underline),7 (Negativo)
#TEXT 30 (White), 31 (Red), 32 (Green) , 33 (Yellow), 34 (Blue), 35 (Purple), 36 (LightBlue), 37 (Grey)
#BACK 40 (White), 41 (Red), 42 (Green) , 43 (Yellow), 44 (Blue), 45 (Purple), 46 (LightBlue), 47 (Grey)

#print('\033[7;33;44mOlá, Mundo!\033[m')
'''a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))'''

nome = 'Emerson'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'preto':'\033[0;30m'
         }
print('Olá!, Muito prezer em te conhecer, {}{}{}!!!'.format(cores['preto'],nome, cores['limpa']))