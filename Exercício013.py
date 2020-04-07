import msvcrt

while True:
    base = float(input('Digite um número base:\n'))
    exp = float(input('Digite um número expoente:\n'))
    base2 = base
    contador = 1
    while contador < exp:
        base2 = base2 * base
        contador += 1

    print('O número %s elevado ao expoente %s é igual a : %s' %
          (base, exp, base2))

    print('\nPressione qualquer tecla para repetir ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
