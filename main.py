import random


def set_characters_list(chars):
    for char in chars:
        if char.stars == 3:
            three_stars_characters.append(char)
        elif char.stars == 4:
            four_stars_characters.append(char)
        elif char.stars == 5:
            five_stars_characters.append(char)


def charactersinfo(char):
    print(f'\nName: {char.name} {"★" * char.stars}')


def menuopc():
    print('\n[1] Lista de personagens')
    print('[2] Banners de invocação')
    print('[3] Sair')
    return int(input('Digite a opção que deseja: '))


def summonmenu():
    print(f'\n[1] 1x invocação (Pity: {cont}/100)')
    print(f'[2] 10x invocação (Pity: {cont}/100)')
    print('[3] Sair')
    return int(input('Digite a opção que deseja: '))


def summon_banners(pity, opc1):

    match opc1:

        case 1:

            summon = random.randint(1, 100)
            if pity == 99:
                char = random.choice(five_stars_characters)
                print(f'{char.name} {"★" * 5}')
                pity = 0
            elif 1 <= summon <= 79:
                char = random.choice(three_stars_characters)
                print(f'{char.name} {"★" * 3}')
                pity += 1
            elif 80 <= summon <= 99:
                char = random.choice(four_stars_characters)
                print(f'{char.name} {"★" * 4}')
                pity += 1
            elif summon == 100:
                char = random.choice(five_stars_characters)
                print(f'{char.name} {"★" * 5}')
                pity = 0

            return pity

        case 2:

            print('')
            for i in range(10):
                summon = random.randint(1, 100)
                if pity == 99:
                    char = random.choice(five_stars_characters)
                    print(f'{char.name} {"★" * 5}')
                    pity = 0
                elif 1 <= summon <= 79:
                    char = random.choice(three_stars_characters)
                    print(f'{char.name} {"★" * 3}')
                    pity += 1
                elif 80 <= summon <= 99:
                    char = random.choice(four_stars_characters)
                    print(f'{char.name} {"★" * 4}')
                    pity += 1
                elif summon == 100:
                    char = random.choice(five_stars_characters)
                    print(f'{char.name} {"★" * 5}')
                    pity = 0

            return pity


class Characters:

    def __init__(self, name, hp, damage, stars):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.stars = stars


class Enemies:

    def __init__(self, name, hp, damage, stars):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.stars = stars


characters = list()
three_stars_characters = list()
four_stars_characters = list()
five_stars_characters = list()
characters.append(Characters('Stark', 20, 20, 5))
characters.append(Characters('Ichigo', 25, 15, 5))
characters.append(Characters('Dio', 10, 10, 4))
characters.append(Characters('Killua', 15, 7, 4))
characters.append(Characters('Luffy', 5, 5, 3))
characters.append(Characters('Orihime', 3, 3, 3))

set_characters_list(characters)


enemies = list()
enemies.append(Enemies('Goblin', 100, 5, 3))
enemies.append(Enemies('Bat', 50, 3, 2))

cont = 0

while True:
    opc = menuopc()

    match opc:

        case 1:
            for character in characters:
                charactersinfo(character)
        case 2:
            while True:
                opc_banner = summonmenu()

                match opc_banner:

                    case 1:

                        cont = summon_banners(cont, opc_banner)

                    case 2:

                        cont = summon_banners(cont, opc_banner)

                    case 3:
                        break
                    case _:
                        print('\nOpção inválida, digite novamente!')
        case 3:
            print('\nO jogo está fechando...')
            break
        case _:
            print('\nOpção inválida, digite novamente!')
