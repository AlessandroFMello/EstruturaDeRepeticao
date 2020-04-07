import msvcrt
while True:
    arr = []
    arrP = []
    arrI = []
    contador = 0
    arr.append(int(input('Digite um número:\n')))
    while contador < 9:
        arr.append(int(input('Digite outro número:\n')))
        contador += 1
    for x in arr:
        if x % 2 == 0:
            arrP.append(x)
        elif x % 2 != 0:
            arrI.append(x)
    print('Você escolheu os números:\n%s\n' % arr)
    print('Os pares são %s, logo temos %s pares\n' % (arrP, len(arrP)))
    print('Os ímpares são %s, logo temos %s ímpares' % (arrI, len(arrI)))

    print('\nPressione qualquer tecla para repetir ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
