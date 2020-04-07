import msvcrt

while True:
    numero = int(input("\nDigite um número:\n"))
    arr = []
    divisoes = 0

    for i in range(numero + 1):
        if i % 2 == 1 and i != 2:
            arr.append(i)
            divisoes += 1
        else:
            divisoes += 1
    print("Números primos: %s" % arr)
    print("Número de divisões: %s" % divisoes)

    print('\nPressione qualquer tecla para repetir ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
