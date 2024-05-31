def leiaDinheiro(msg):
        while True:
            resposta = input(msg).strip().replace(',','.')
            if resposta.replace('.','',1).isdigit():
                break
            else:
                print(f'ERRO: "{resposta}" é um preço inválido!')
        resposta = float(resposta)
        return resposta

