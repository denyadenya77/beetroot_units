import random


class Player:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.moves = [self.small_hit, self.big_hit, self.treatment]

    def small_hit(self, enemy):
        power = random.randint(18, 25)
        enemy.health = enemy.health - power

    def big_hit(self, enemy):
        power = random.randint(10, 35)
        enemy.health = enemy.health - power

    def treatment(self, *enemy):
        treatment = random.randint(18, 25)
        self.health = self.health + treatment