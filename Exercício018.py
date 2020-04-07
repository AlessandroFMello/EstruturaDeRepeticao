import msvcrt

while True:
    arr = []
    print('ADICIONE NÚMEROS À LISTA\n')
    arr.append(int(input('Digite um número para adicionar à lista:\n')))
    while True:
        print('Pressione 1 para adicionar um número, pressione 2 para prosseguir')
        key2 = msvcrt.getch()
        if key2 == b'2':
            print('\nA sua lista é:\n%s' % arr)
            print('O menor número da lista é: %s' % min(arr))
            print('O maior número da lista é: %s' % max(arr))
            print('A soma de todos os números da lista é: %s' % sum(arr))
            break
        elif key2 == b'1':
            arr.append(int(
                input('\nDigite um novo número para adicionar à lista:\n')))
            continue

    print('\nPressione qualquer tecla para repetir ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
