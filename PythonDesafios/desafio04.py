valor = input('Digite algo para extrairmos as informações: ')
print('O seu tipo é:', type(valor))
print('Esse input é um número?', valor.isnumeric())
print('Esse input é alfabetico?', valor.isalpha())
print('Esse input é alfanúmerico?', valor.isalnum())
print('Esse input esta em maisculo?', valor.isupper())
print('Esse input esta em  minusculo?', valor.islower())
print('Esse input esta é um espaço?', valor.isspace())
print('Esse input é um decimal?', valor.isdecimal())
print('Esse input é mostravel?', valor.isprintable())
