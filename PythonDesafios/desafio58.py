"""from random import choice
print('ADIVINHADOR')
pc = choice(range(11))
print('-=-' * 20)
print('Pensei em um número inteiro de 0 a 10, tente adivinhar!')
print('-=-' * 20)
user = ''
tentativas = 0
while pc != user:
    tentativas += 1
    user = int(input('Digite aqui o seu chute: '))
    if user == pc:
        print('Você adivinhou com {} tentativas. Parabéns!'.format(tentativas))
    else:
        print(('Você errou, tente novamente.'))
    """

from random import randint
computador = randint(0,10)
print('Sou seu computador... Acavei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
