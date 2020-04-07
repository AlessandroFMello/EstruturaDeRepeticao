import msvcrt

while True:
    arr = []
    print('Números divisíveis apenas por 1 e eles mesmos são primos')
    numero = int(input('Digite um número para saber se ele é ou não primo:\n'))
    contador = 1
    A = ('O número %s é primo' % numero)
    B = ('O número %s NÃO é primo' % numero)

    while contador <= numero:
        if numero == 1 and contador == 1:
            arr.append(
                'O número 1 não é primo, pois ele mesmo e 1 são o mesmo número')
            break
        if numero % contador == 0 and contador == 1 or contador == numero:
            arr.append(A)
            print('O número %s é divisível por: %s' % (numero, contador))
        elif numero % contador == 0 and contador != 1 and contador != numero:
            arr.append(B)
            print('O número %s é divisível por: %s' % (numero, contador))

        contador += 1
    arr.sort()
    print(arr[0])

    print('\nPressione qualquer tecla para repetir ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
