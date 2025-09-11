while True:
    cpf = input('Digite o seu CPF: ')
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')

    verificador = None

    for i in range(len(cpf)):
        if cpf[0] != cpf[i]:
            verificador = True
            break

    if len(cpf) == 11 and verificador:
        print('O CPF inserido é verdadeiro.')
        break
    else:
        print('O CPF inserido é falso, digite novamente.')
