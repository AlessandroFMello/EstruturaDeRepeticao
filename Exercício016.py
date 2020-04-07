import msvcrt

while True:
    arr = []
    contadorin = 1
    num1 = 0
    num2 = 1
    arr.append(num1)
    while contadorin < 500:
        arr.append(contadorin)
        contadorin = num1 + num2
        num1 = num2
        num2 = contadorin

        if arr[-1] < 500:
            arr.append(contadorin)
            contadorin = num1 + num2
            num1 = num2
            num1 = contadorin

    print(arr)

    print('Pressione qualquer tecla para repetir ou 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
