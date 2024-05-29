from time import sleep
def maior(* valores):
    m = 0
    c = 0
    print('-=' * 30)
    print(f'Analisando os valores passados...')
    while c < len(valores):
        if c == 0:
            m = valores[c]
        if valores[c] > m:
            m = valores[c]
        print(f'{valores[c]} ', end='')
        c += 1
        sleep(0.5)
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {m}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
