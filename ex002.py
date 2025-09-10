import random

cont = 0
num = random.randint(1, 100)

while cont < 10:

    print(num)
    tentativa = int(input('Adivinhe o número: '))
    cont += 1
    
    if tentativa < num:
        print('Tentativa falha, o número digitado é menor do que o esperado.')
    elif tentativa > num:
        print('Tentativa falha, o número digitado é maior do que o esperado.')
    else:
        print(f'Parabéns! Você adivinhou o número com {cont} tentativa(s).')
        break