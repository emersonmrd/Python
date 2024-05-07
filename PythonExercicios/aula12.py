nome = str(input('Qual é seu nome? ')).upper()
if nome == 'EMERSON':
    print('Que nome bonito! Igual ao dono.')
elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'PAULO':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'ANA CLÁUDIA JÉSSICA JULIANA':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome.capitalize()))