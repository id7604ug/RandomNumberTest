import unittest
from random_number_game import random_number_game
from unittest.mock import Mock, patch

class TestGuessing(unittest.TestCase):

    # self.assertEqual(5, user_guessing(5))
    # @patch('builtins.input', return_value=5)
    # @patch('random_number_game.random.randrange', return=5)
    # @patch('random_number_game.get_random_number()', side_effect=[5])
    # def test_complete_game(self, mock_randint, mock_input):
    #     self.assertEqual(random_number_game.main(), 'Good guess, you got it! The number was: 5')



    # 'random_number_game.get_input', side_effect=[5]

    # Test getting user input
    @patch('builtins.input', side_effect=[5])
    def test_input(self, mock_input):
        self.assertEqual(random_number_game.get_input(), 5)

    # Test Main function
    @patch('random_number_game.get_input', side_effect=[6])
    @patch('random_number_game.get_random_number', side_effect=[6])
    def test_complete_game(self, mock_randrange, mock_input):
        # random_number = random_number_game.get_random_number
        # random_number_game.get_random_number = Mock()
        random_number_game.main()
        self.assertEqual(random_number_game.main(),'Good guess, you got it! The number was: 6' )
