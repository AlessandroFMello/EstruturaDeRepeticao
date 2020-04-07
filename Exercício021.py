import msvcrt

while True:
    arr = []
    print('Números divisíveis apenas por 1 e eles mesmos são primos')
    numero = int(input('Digite um número para saber se ele é ou não primo:\n'))
    contador = 1

    while contador <= numero:
        if numero == 1 and contador == 1:
            arr.append(
                'O número 1 não é primo, pois ele mesmo e 1 são o mesmo número')
            break
        if numero % contador == 0 and contador == 1 or contador == numero:
            arr.append('O número %s é primo' % numero)
        elif numero % contador == 0 and contador != 1 and contador != numero:
            arr.append('O número %s NÃO é primo' % numero)
            break
        contador += 1

    print(arr[-1])

    print('\nPressione qualquer tecla para repetir ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
