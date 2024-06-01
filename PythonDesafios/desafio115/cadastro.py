import uteis

while True:
    try:
        uteis.menuPrincipal()
        try:
            opcao = int(input('Sua opção: '))
            if opcao == 1:
                uteis.pessoasCadastradas()
            elif opcao == 2:
                uteis.cadastrarPessoa()
            elif opcao == 3:
                uteis.sairSistema()
                break
            else:
                print(f'ERROR. Digite uma opção válida!')
        except ValueError:
            print(f'ERROR. Digite uma opção válida!')
    except KeyboardInterrupt:
            print()
            print('O usuário decidiu encerrar o sistema.')
            uteis.sairSistema()
            break
    except Exception as e:
            print(f'ERROR. TENTE NOVAMENTE! {e}')