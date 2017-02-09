import unittest
from random_number_game import random_number_game
from unittest.mock import Mock, patch

class TestGuessing(unittest.TestCase):

    # self.assertEqual(5, user_guessing(5))
    # @patch('builtins.input', return_value=5)
    # @patch('random_number_game.random.randrange', return=5)
    @patch('random_number_game.get_random_number', return_value=5)
    @patch('random_number_game.get_input', return_value=5)
    def test_complete_game(self, mock_randrange, mock_input):
        random_number_game.main()

    @patch('random_number_game.get_input', side_effect=[5, 6, 7])
    @patch('random_number_game.get_random_number', return_value=6)
    def test_complete_game(self, mock_randrange, mock_input):
            random_number_game.main()
