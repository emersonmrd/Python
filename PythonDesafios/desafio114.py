'''import socket

def verificar_host(host, port=443):
    try:
        socket.create_connection((host, port), timeout=5)
        print(f'Consegui acesasr o site Pudim com sucesso!.')
    except (socket.timeout, socket.error):
        print(f'O site Pudim não está acessível no momento.')

# Testando a função
verificar_host('www.pudim.com.br')'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    #print(site.read())