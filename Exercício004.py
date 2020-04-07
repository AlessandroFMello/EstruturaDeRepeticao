import msvcrt

while True:

    habA2 = int(input('Digite a população A:\n'))
    habB2 = int(input('Digite a população B:\n'))
    habA = habA2
    habB = habB2

    CresA = (
        float(input('Digite a taxa de crescimento A (em %, NÃO em decimal):\n').replace(',', '.')))/100
    CresB = (
        float(input('Digite a taxa de crescimento B (em %, NÃO em decimal):\n').replace(',', '.')))/100
    Anos = 0
    CresA2 = (CresA * 100)
    CresB2 = (CresB * 100)
    while (habA < habB):
        Anos += 1
        habA = habA + (habA * CresA)
        habB = habB + (habB * CresB)

    print('\nA com uma população inicial de %s habitantes\ne uma taxa de crescimento de %s (ou %s%%) ao ano' %
          (habA2, CresA, CresA2))
    print('\nB com uma população inicial de %s habitantes\ne uma taxa de crescimento de %s (ou %s%%) ao ano' % (
        habB2, CresB, CresB2))
    print('\nA e B Demoram %s anos para igualar suas populações\n' % Anos)

    print('Pressione qualquer tecla para repetir ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
