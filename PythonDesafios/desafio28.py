import random
pc = random.choice(range(6))
print('Pensei em um número inteiro de 0 a 5, tente adivinhar!')
user = int(input('Digite aqui o seu chute: '))
if user == pc:
    print('Você adivinhou e venceu. Parabéns!')
else:
    print(('Você errou e perdeu.'))