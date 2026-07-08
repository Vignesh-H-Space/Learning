class Hero:
    def __init__(self):
        self.health = 100

player = Hero()

print(getattr(player, 'mana', 50))

print(player.mana)