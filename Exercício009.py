import msvcrt

while True:
    arr = []
    contador = 0
    print('Números ímpares entre 0 e 50:')
    while contador < 50:
        if contador % 2 != 0:
            arr.append(contador)
        contador += 1
    print(arr)

    print('\nPressione qualquer tecla para repetir ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
