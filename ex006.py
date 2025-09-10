from collections import Counter

frase = input('Digite uma frase: ')

frase = frase.replace(' ', '')
frase = frase.replace(',', '')
frase = frase.replace('.', '')

contador = Counter(frase)

print(contador.most_common(1))
