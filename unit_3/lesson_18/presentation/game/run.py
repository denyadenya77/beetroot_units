from game import Game
from player import Player

if __name__ == "__main__":
    player = Player('Player')
    computer = Player('Computer')
    game = Game(player, computer)
    game.game()