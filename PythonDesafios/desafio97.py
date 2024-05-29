"""def escreva(txt):
    tam = len(txt)
    print('~' * (tam+4))
    print(f'  {txt}  ')
    print('~' * (tam + 4))

escreva('Olá, Mundo!')
escreva('Emerson Martins')
escreva('Curso de Python no Youtube')
escreva('CeV')"""

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)


#Programa princial
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')