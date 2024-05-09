print('ANALISADOR')
somaI = 0
homemMaisVelho = ""
maiorI = 0
mmdevinte = 0
for c in range(1, 5):
    nome = str(input('Digite o nome da {}º pessoa: '.format(c)))
    idade = int(input('Digite a idade da {}º pessoa: '.format(c)))
    sexo = int(input('Escolha o sexo da {}º pessoa:\n'
                     '1 - M\n'
                     '2 - F\n'
                     'Digite aqui: '.format(c)))
    somaI += idade
    if sexo == 1:
        if maiorI < idade:
            maiorI = idade
            homemMaisVelho = nome
    if sexo == 2 and idade < 20:
        mmdevinte += 1

mediaIdade = somaI / 4
print('A Média de idade do grupo é de {} anos'.format(mediaIdade))
print('O Homem mais velho se chama {}.'.format(homemMaisVelho))
print('Existem {} mulheres com menos de 20 anos.'.format(mmdevinte))
