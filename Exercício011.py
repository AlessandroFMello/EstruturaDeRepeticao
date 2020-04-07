import msvcrt

while True:
    arr = []
    num1 = float(input('Digite um número:\n'))
    num2 = float(input('Digite outro número:\n'))
    if num2 > num1:
        while num1 <= num2:
            arr.append(num1)
            num1 += 1
    elif num1 > num2:
        while num2 <= num1:
            arr.append(num2)
            num2 += 1
    print(arr)

    print('\nA soma entre os números da lista é: %s' % sum(arr))

    print('\nPressione qualquer tecla para repetir ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
