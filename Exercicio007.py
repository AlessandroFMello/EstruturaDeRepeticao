import msvcrt

while True:
    arr = []
    contador = 0
    arr.append(float(input('Digite um número:\n').replace(',', '.')))

    while contador < 4:
        arr.append(float(input('Digite outro número:\n').replace(',', '.')))
        contador += 1

    print('O array atual é: %s' % arr)
    print('Utilizando o método max() o maior valor é: %s' % max(arr))
    input('\nPressione ENTER para o próximo')
    arr.sort()
    print('\nApós o ordenamento crescente com array.sort() o array é: %s' % arr)
    print('Utilizando o método array[-1] o maior número é: %s' % arr[-1])
    print('\nPodemos também ordenar o array ao contrário')
    input('\nPressione ENTER para o próximo')
    arr.reverse()
    print('\nApós o array.reverse() o array é: %s' % arr)
    print('Então utilizamos array[0], logo o maior número é: % s' % arr[0])

    print('\nPressione qualquer tecla para repetir ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
