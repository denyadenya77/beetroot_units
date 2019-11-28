import random


class Player:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.moves = ['small_hit', 'big_hit', 'treatment']

    def small_hit(self, enemy):
        power = random.randint(18, 25)
        enemy.health = enemy.health - power

    def big_hit(self, enemy):
        power = random.randint(10, 35)
        enemy.health = enemy.health - power

    def treatment(self, *enemy):
        treatment = random.randint(18, 25)
        self.health = self.health + treatment

    def move(self, victim):
        move = random.choice(self.moves)
        getattr(self, move)(victim)
