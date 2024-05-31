# Modularização
    # Surgiou no início da década de 60
    # Sistemas ficando cada vez maiores
    # Foco: dividir um programa grande
    # Foco: aumentar a legibilidade
    # Foco: facilitar a manutenção

# Vantagens
    # Organização do código
    # Facilidade na manutenção
    # Ocultação de código detalhado
    # Reutilização em outros projetos


from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')