import msvcrt

while True:
    arr = []
    print('ADICIONE NÚMEROS ENTRE 0 E 1000 À LISTA')

    while True:
        lista1 = int(input('Digite um número para adicionar à lista:\n'))
        if lista1 >= 0 and lista1 <= 1000:
            arr.append(lista1)
            break
        else:
            print('Número inválido, tente outro')
            continue
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

            while True:
                lista2 = int(
                    input('Digite um número para adicionar à lista:\n'))
                if lista2 >= 0 and lista2 <= 1000:
                    arr.append(lista2)
                    break
                else:
                    print('Número inválido, tente outro')
                    continue
                continue

    print('\nPressione qualquer tecla para repetir ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
