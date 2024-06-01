import socket

def verificar_host(host, port=443):
    try:
        socket.create_connection((host, port), timeout=5)
        print(f'Consegui acesasr o site Pudim com sucesso!.')
    except (socket.timeout, socket.error):
        print(f'O site Pudim não está acessível no momento.')

# Testando a função
verificar_host('www.pudim.com.br')
