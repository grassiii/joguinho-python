class Characters:

    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage


characters = list()
characters.append(Characters("Grassi", 10, 10))

print(characters[0].name)
