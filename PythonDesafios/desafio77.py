palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')

vogais = 'aeiou'

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')