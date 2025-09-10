largura = int(input('Digite um númeor ímpar: '))
cont = 0

print(f'\n {"*" * (largura - 2)}')
while largura > 0:
    print(f'{" " * cont}{"*" * largura}')
    cont += 1
    largura -= 2
