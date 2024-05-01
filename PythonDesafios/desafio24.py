nomeCidade = str(input('Digite o nome de uma cidade: '))
santo = 'SANTO'
nomeCidade = nomeCidade.upper().split()
print('O nome da cidade digitada começa com SANTO?',nomeCidade[0] == santo)