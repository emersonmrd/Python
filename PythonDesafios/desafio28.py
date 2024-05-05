from random import choice
from time import sleep
pc = choice(range(6))
print('-=-' * 20)
print('Pensei em um número inteiro de 0 a 5, tente adivinhar!')
print('-=-' * 20)
user = int(input('Digite aqui o seu chute: '))
print('PROCESSANDO...')
sleep(2)
if user == pc:
    print('Você adivinhou e venceu. Parabéns!')
else:
    print(('Você errou e perdeu.'))