import unittest
from unittest.mock import patch
from unit_2.unit_testing_2.game import Game, Player


class TestGame(unittest.TestCase):

    def setUp(self):
        self.player = Player('Person')
        self.computer = Player('Computer')
        self.game = Game(self.player, self.computer)


    @patch.object(Game, 'show_status')
    @patch('random.choice')
    @patch('random.shuffle')
    def test_game_inside(self, mock_random_shuffle, mock_random_choice, mock_show_status):
        mock_random_choice.side_effect = [Player.small_hit, Player.small_hit, Player.small_hit, Player.small_hit,
                                          Player.small_hit, Player.small_hit]
        self.game.game()
        # mock_random_shuffle.assert_called()
        mock_random_choice.assert_called()
        mock_show_status.assert_called()
















    # @patch('random.choice')
    # @patch('random.shuffle')
    # def test_game(self, mock_random_shuffle, mock_random_choice):
    #     mock_random_choice.side_effect = [Player.small_hit, Player.small_hit, Player.small_hit, Player.small_hit, Player.small_hit, Player.small_hit]
    #
    #     self.game.game()
    #
    #     death = 0
    #     self.assertLess(self.computer.health, death)




if __name__ == '__main__':
    unittest.main()