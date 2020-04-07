import msvcrt

while True:
    numero = int(input('De qual número você deseja ver a tabuada?\n'))

    print('Tabuada de %s:' % numero)
    contador = 1

    while contador <= 10:
        mult = numero * contador
        print('%s X %s = %s' % (numero, contador, mult))
        contador += 1

    print('\nPressione qualquer tecla para repetir ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
