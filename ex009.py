num = list()

while True:
    entrada = input('Digite um número(fim para fazer média): ')

    if entrada.isnumeric():
        num.append(int(entrada))
    elif entrada == 'fim':
        break

media = 0

for i in range(len(num)):
    media += num[i]

media = media / len(num)
print(f'A média é: {media}')
