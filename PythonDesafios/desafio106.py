def tituloP():
    txt = 'SISTEMA DE AJUDA PyHELP'
    print('~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))

def tituloS():
    txt = 'ATÉ LOGO!'
    print('~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))

def tituloM(c):
    txt = f"Acessando o manual do comando '{c}'"
    print('~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))

def pyHelp():
    comando = ''
    while comando.lower() != 'fim':
        tituloP()
        comando = input('Função ou Biblioteca > ').strip()
        if comando.lower() == 'fim':
            tituloS()
            break
        tituloM(comando)
        help(comando)

# Programa principal
pyHelp()
