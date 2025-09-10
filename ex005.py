num = int(input('Digite um número: '))
num_convert = list(str(num))
num_armstrong = 0

for i in range(len(num_convert)):
    num_armstrong += int(num_convert[i]) ** len(num_convert)

if num_armstrong == num:
    print(f'O número {num} é um número armstrong!')
else:
    print(f'O número {num} não é um número armstrong!')
