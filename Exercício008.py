import msvcrt

while True:
    arr = []
    contador = 0
    arr.append(float(input('Digite um número:\n')))
    while contador < 4:
        arr.append(float(input('Digite outro número\n')))
        contador += 1

    print('A soma dos números %s é: %s' % (arr, sum(arr)))
    media = sum(arr)/len(arr)
    print('\nA média dos números %s é: %s' % (arr, media))

    print('Pressione qualquer tecla para repetir ou ESPAÇO para sair')
    key = msvcrt.getch()
    if key == b' ':
        break
