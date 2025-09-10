while True:
    senha = input('Digite uma senha: ')
    if senha.islower():
        print('A senha deve conter pelo menos um caractere MAIÚSCULO.')
    elif senha.isupper():
        print('A senha deve conter pelo menos um caractere MINÚSCULO.')
    elif senha.isalpha():
        print('A senha deve conter pelo menos um caractere numérico.')
    elif senha.isalnum():
        print('A senha deve conter um caractere especial(ex: `!@#$%^&*()`).')
    elif len(senha) < 8:
        print('A senha deve conter 8 ou mais caracteres.')
    else:
        break

print(f'Senha final: {senha}')
print(f'Senha final: {"*" * len(senha)}')
