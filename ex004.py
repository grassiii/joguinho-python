def menu():
    print('\n[1] Depositar')
    print('[2] Sacar')
    print('[3] Ver Saldo')
    print('[4] Sair')

    return int(input('Digite uma opção: '))


def deposito():
    while True:
        deposit = float(input('\nDigite a quantia que deseja depositar: R$'))
        if deposit <= 0:
            print('\nDepósito inválido, digite uma quantia válida.')
        else:
            return deposit


def sacar(sal):
    while True:
        saque = float(input('\nDigite a quantia que deseja sacar: R$'))
        if saque > sal:
            print('\nSaque inválido, digite uma quantia válida.')
        else:
            return saque


saldo = 0

while True:
    opc = menu()

    match opc:

        case 1:
            saldo += deposito()
        case 2:
            saldo -= sacar(saldo)
        case 3:
            print(f'\nSaldo: R${saldo:.2f}')
        case 4:
            break
        case _:
            print('Opção inválida!')
