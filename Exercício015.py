import msvcrt

while True:
    arr = []
    contadorfin = int(input('Digite um número final:\n'))
    contadorin = 1
    num1 = 0
    num2 = 1
    arr.append(0)

    while contadorin <= contadorfin:
        arr.append(contadorin)
        contadorin = num1 + num2
        num1 = num2
        num2 = contadorin

    print(arr)

    print('Pressione qualquer tecla para repetir ou 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
