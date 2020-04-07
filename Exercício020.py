import msvcrt

while True:
    while True:
        numero = int(input('Digite um número entre 1 e 15:\n'))
        num = numero
        contador = numero - 1
        res = 0
        if numero < 16 and numero > 0:
            break
        else:
            print('Número inválido, tente outro\n')
            continue
    while contador >= 1:
        res = num * (contador)
        num = res
        contador -= 1

    print('O fatorial de %s, ou seja, %s! é: %s' % (numero, numero, res))
    print('\nPressione qualquer tecla para repetir ou 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
