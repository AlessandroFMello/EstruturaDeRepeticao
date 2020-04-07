import msvcrt

while True:
    while True:
        nota = float(
            input('Digite uma nota entre 1 e 10:\n').replace(',', '.'))
        if nota >= 0 and nota <= 10:
            False
            print('Nota: %s' % nota)
            print('Nota Válida\n')
            break
        else:
            print('Nota: %s' % nota)
            print('Nota Inválida\n')
            True

    print('Pressione qualquer tecla para repetir ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
