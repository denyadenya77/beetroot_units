import random


class Game:

    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def game(self):
        while self.player.health > 0 and self.computer.health > 0:
            striker_and_victim = [self.player, self.computer]
            random.shuffle(striker_and_victim)
            striker = striker_and_victim[0]
            victim = striker_and_victim[1]
            # move = random.choice(striker.moves)

            if self.computer.health >= 35 and len(self.computer.moves) == 3:
                random.choice(striker.moves)(victim)
                # move(striker, victim)
                # getattr(striker, move.__name__).()
                self.health_borders(striker, victim)
                # self.show_status(move, striker, victim)
            elif self.computer.health >= 35 and len(self.computer.moves) == 4:
                self.computer.moves.remove(self.computer.moves[3])
                random.choice(striker.moves)(victim)
                # move(victim)
                self.health_borders(striker, victim)
                # self.show_status(move, striker, victim)
            else:
                self.computer.moves.append(Player.treatment)
                random.choice(striker.moves)(victim)
                # move(victim)
                self.health_borders(striker, victim)
                # self.show_status(move, striker, victim)

            if self.computer.health <= 0:
                print(f"{self.player.name} wins!")
            elif self.player.health <= 0:
                print(f'{self.computer.name} wins!')

    def show_status(self, move, striker, victim):
        if move.__name__ == 'treatment':
            print(f'{striker.name} treatment. Health: {striker.health}.\n')
        else:
            print(f'{striker.name} {move.__name__} {victim.name}.\n'
                  f'{victim.name} health: {victim.health}.\n')

    def health_borders(self, *players):
        for player in players:
            if player.health > 100:
                player.health = 100
            if player.health < 0:
                player.health = 0

