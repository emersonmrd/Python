#pessoas = {'nome': 'Gustavo', 'sexo':'M', 'idade': 22}
#print(pessoas) # -> mostra o dicionario inteiro
#print(pessoas['nome']) # -> mostra o valor que esta em nome
#print(f'O {pessoas['nome']} tem {pessoas['idade']} anos') #-> exemplo de como usar
#print(pessoas.keys()) # -> mostra as keys(chaves) do dicionario
#print(pessoas.values()) # -> mostra os valores do dicionario
#print(pessoas.items()) # -> mostra as chaves e valores do dicionario

# laço for para mostrar chaves de um dicionario
#for k in pessoas.keys():
    #print(k)

# laço para mostrar os valores de um dicionario
#for k in pessoas.values():
    #print(k)

# laço para mostrar a chave e valor de um dicionario
#del pessoas['sexo'] # -> deleta a chave sexo e valores do dicionario
#pessoas['nome'] = 'Leandro' # -> coloca um novo valor em nome
#pessoas['peso'] = 98.5 #-> adiciona um novo elemento
#for k, v in pessoas.items():
    #print(f'{k} = {v}')

# cria uma lista
#brasil = []
# cria e adiciona valores em um dicionario de estado
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# cria e adiciona valores em um outro dicionario de estado
#estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# adiciona os valores na lista brasil
#brasil.append(estado1)
#brasil.append(estado2)
# mostra o dicionario do primeiro estado
#print(estado1)
# mostra o dicionario do segundo estado
#print(estado2)
# mostra a lista contendo os dicionarios
#print(brasil)
# mostra o dicionario do primeiro estado
#print(brasil[0])
# mostra o dicionario do segundo estado
#print(brasil[1])
# mostra o valor da chave uf do primeiro estado
#print(brasil[0]['uf'])
# mostra o valor da chafe sigla do segundo estado
#print(brasil[1]['sigla'])


# cria um dicinario estado
estado = {}
# cria uma lista pais brasil
brasil = []
# laço for para ler 3 estados
for c in range(0, 3):
    # lê a uf
    estado['uf'] = str(input('Unidade Federativa: '))
    # lê a sigla
    estado['sigla'] = str(input('Sigla do Estado: '))
    # adiciona o dicionario estado na lista brasil
    brasil.append(estado.copy())
# laço para ler os dicionarios(estados) na lista brasil
for e in brasil:
    # laço para ler a chave e valor de cada item do dicionario estado
    #for k, v in e.items():
        #print(f'O campo {k} tem valor {v}')
    # laço alternativa para ler os valores do dicionario
    for v in e.values():
        print(v, end=' ')
    print()