"""teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #-> aqui se fizer sem [:] irá criar uma ligação
print(galera)
teste[0] = 'Maria'
teste[1] = 22
print(teste)
galera.append(teste[:]) #-> aqui se fizer sem [:] irá criar uma ligação
print(galera)"""

#galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera) #-> mostra a lista composta toda
#print(galera[0]) #-> mostra a lista interior toda baseado na posição
#print(galera[0][0]) # -> mostra um dado da lista interior baseado na posição
#for p in galera:
   # print(p) #-> mostra a lista interior toda baseado na posição
   # print(p[0]) # -> mostra um dado da lista interior baseado na posição
#for p in galera:
    #print(f'{p[0]} tem {p[1]} anos de idade.')

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3): #-> for para repetir a estrutura de solicitação de dados
    dado.append(str(input('Nome: '))) # -> solicita o nome e joga na lista dado
    dado.append(int(input('Idade: '))) # -> solicita a idade e joga na lista dad
    galera.append(dado[:]) # -> coloca uma copia da lista dado na lista galera
    dado.clear() # -> limpa a estrutura para a proxima repetição
print(galera) #-> mostra a lista

for p in galera: #-> for para repetir a estrutura de verificação de idade
    if p[1] >= 21: # -> valida se a pessoa da lista é maior de idade
        print(f'{p[0]} é maior de idade.') #-> mostra a pessoa que é maior de idade
        totmai += 1 #-> soma mais um no total de maiores
    else:
        print(f'{p[0]} é menor de idade.')#-> mostra a pessoa que é menor de idade
        totmen += 1 #-> soma mais um no total de menores
# mostra o total de maiores e menores:
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
