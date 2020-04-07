import msvcrt

while True:
    numero = int(input('Digite um número:\n'))
    num = numero
    contador = numero - 1
    res = 0

    while contador >= 1:
        res = num * (contador)
        num = res
        contador -= 1

    print('O fatorial de %s, ou seja, %s! é: %s\n' % (numero, numero, res))
    print('Pressione qualquer tecla para repetir ou 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
