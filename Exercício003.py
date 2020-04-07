import msvcrt

while True:
    while True:
        nome = input('Digite seu nome:\n')
        if len(nome) <= 3:
            print('O nome deve ser maior que 3 caracteres\n')
            True
        else:
            break

    while True:
        idade = int(input('Digite a sua idade:\n'))
        if idade < 0 or idade > 150:
            print('Idade inválida\n')
            True
        else:
            break

    while True:
        salario = float(input('Digite seu salário:\n'))
        if salario <= 0:
            print('Salário inválido\n')
            True
        else:
            break

    while True:
        Sexo = input('Qual é seu sexo? Digite (m) ou (f):\n')
        if Sexo == 'm' or Sexo == 'M':
            Sexo = 'Masculino'
            break
        elif Sexo == 'f' or Sexo == 'F':
            Sexo = 'Feminino'
            break
        else:
            True

    while True:
        EstCiv = input(
            'Você é solteiro/a(s), casado/a(c), viúvo/a(v), ou divorciado/a(d)?\n')

        if (EstCiv == 's' or EstCiv == 'S') and Sexo == 'Masculino':
            EstCiv = 'Solteiro'
            break
        elif (EstCiv == 's' or EstCiv == 'S') and Sexo == 'Feminino':
            EstCiv = 'Solteira'
            break

        if (EstCiv == 'c' or EstCiv == 'C') and Sexo == 'Masculino':
            EstCiv = 'Casado'
            break
        elif (EstCiv == 'c' or EstCiv == 'C') and Sexo == 'Feminino':
            EstCiv = 'Casada'
            break

        if (EstCiv == 'v' or EstCiv == 'V') and Sexo == 'Masculino':
            EstCiv = 'Viúvo'
            break
        elif (EstCiv == 'v' or EstCiv == 'V') and Sexo == 'Feminino':
            EstCiv = 'Viúva'
            break

        if (EstCiv == 'd' or EstCiv == 'D') and Sexo == 'Masculino':
            EstCiv = 'Divorciado'
            break
        elif (EstCiv == 'd' or EstCiv == 'D') and Sexo == 'Feminino':
            EstCiv = 'Divorciada'
            break

    print('\nNome: %s' % nome)
    print('Idade: %s Anos' % idade)
    print('Salário: R$%s' % salario)
    print('Sexo: %s' % Sexo)
    print('Estado Civil: %s\n' % EstCiv)

    print('Pressione qualquer tecla para repetir ou pressione 1 para fechar')
    key = msvcrt.getch()
    if key == b'1':
        break
