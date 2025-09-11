media = 0
for i in range(3):
    media += float(input(f'Digite a {i}ª nota do aluno: '))

media = media / 3
print(media)

if media < 5:
    print('REPROVADO')
elif 5 <= media < 7:
    print('EM RECUPERAÇÃO')
else:
    print('APROVADO')
