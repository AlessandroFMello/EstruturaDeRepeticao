import msvcrt

while True:
    nome = input('Digite seu nome:\n')
    while True:
        senha = input('escolha uma senha:\n')

        if senha == nome.upper() or senha == nome.lower():
            print('Senha inválida')
            print('A senha escolhida deve ser diferente de seu nome\n')
            True
        elif senha != nome:
            False
            break
        else:
            print('Senha inválida')
            print('A senha escolhida deve ser diferente de seu nome\n')
            True

    print('Pressione qualquer tecla para repetir ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
