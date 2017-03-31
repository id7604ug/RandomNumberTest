import unittest
from random_number_game import random_number_game
from unittest.mock import Mock, patch

class TestGuessing(unittest.TestCase):

    # Test getting user input
    @patch('builtins.input', side_effect=[5])
    def test_input(self, mock_input):
        self.assertEqual(random_number_game.get_input(), 5)

    # Test Main function
    @patch('builtins.input', side_effect=[6, 9, 20, 1])
    def test_complete_game_correct(self, mock_input):
        rand_nums = [6, 9, 20, 1]
        self.assertEqual(random_number_game.user_guessing(rand_nums[0]), 6)
        self.assertEqual(random_number_game.user_guessing(rand_nums[1]), 9)
        self.assertEqual(random_number_game.user_guessing(rand_nums[2]), 20)
        self.assertEqual(random_number_game.user_guessing(rand_nums[3]), 1)

    # Test Main function wrong choices
    @patch('builtins.input', side_effect=[6, 9, 20, 1])
    def test_complete_game_incorrect(self, mock_input):
        self.assertEqual(random_number_game.user_guessing(1), 0)
        self.assertEqual(random_number_game.user_guessing(20), 0)
        self.assertEqual(random_number_game.user_guessing(10), 0)
        self.assertEqual(random_number_game.user_guessing(5), 0)
