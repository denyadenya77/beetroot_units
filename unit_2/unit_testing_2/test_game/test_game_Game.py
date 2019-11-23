import unittest
from unittest.mock import patch
from unit_2.unit_testing_2.game import Game, Player


class TestGame(unittest.TestCase):

    def setUp(self):
        self.player = Player('Person')
        self.computer = Player('Computer')
        self.game = Game


    @patch('unit_2.unit_testing_2.game.big_hit.random.randint')
    @patch('random.choice')
    @patch('random.shuffle')
    def test_game(self, mock_random_shuffle, mock_random_choice, mock_Player_big_hit_random_randint):
        mock_Player_big_hit_random_randint.return_value = 20
        mock_random_choice.side_effect = [Player.big_hit, Player.big_hit, Player.big_hit, Player.big_hit, Player.big_hit]
        self.assertEqual(self.computer.health, 0)


if __name__ == '__main__':
    unittest.main()