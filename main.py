import random


def charactersinfo(char):
    print(f'\nName: {char.name} {"★" * char.stars}')
    print(f'Weapon: {char.weap_type}')


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


class Characters:

    def __init__(self, name, hp, damage, weap_type, stars):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.weap_type = weap_type
        self.stars = stars


class Enemies:

    def __init__(self, name, hp, damage, stars):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.stars = stars


characters = list()
characters.append(Characters('Grassi', 10, 10, 'Scythe', 5))
characters.append(Characters('Stacoviaki', 15, 15, 'Pistols', 4))

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

                        summon = random.randint(1, 100)
                        if cont == 99:
                            print('\n5 estrelas')
                            cont = 0
                        elif 1 <= summon <= 79:
                            print('\n3 estrelas')
                            cont += 1
                        elif 80 <= summon <= 99:
                            print('\n4 estrelas')
                            cont += 1
                        elif summon == 100:
                            print('\n5 estrelas')
                            cont = 0
                    case 2:
                        print('')
                        for i in range(10):
                            summon = random.randint(1, 100)
                            if cont == 99:
                                print('5 estrelas')
                                cont = 0
                            elif 1 <= summon <= 79:
                                print('3 estrelas')
                                cont += 1
                            elif 80 <= summon <= 99:
                                print('4 estrelas')
                                cont += 1
                            elif summon == 100:
                                print('5 estrelas')
                                cont = 0
                    case 3:
                        break
                    case _:
                        print('\nOpção inválida, digite novamente!')
        case 3:
            print('\nO jogo está fechando...')
            break
        case _:
            print('\nOpção inválida, digite novamente!')
