import unittest
import api
from hangman_game import HangmanGame
from api import get_the_guess_result
from unittest.mock import patch


class TestApi(unittest.TestCase):
    def setUp(self):
        with patch('hangman_game.get_random_word', return_value='testing'):
             api.GAME = HangmanGame()

    def test_get_the_guess_result_with_correct_guess(self):
        actual_result = get_the_guess_result('testing')
        self.assertEqual(actual_result['status'], 'game over')
        self.assertEqual(actual_result['message'], 'Well done, You won')

    def test_get_the_guess_result_with_wrong_guess(self):
        actual_result = get_the_guess_result('p')
        self.assertEqual(actual_result['status'], 'continue')
        self.assertEqual(actual_result['message'], 'The game is updated')

    def test_get_the_guess_result_with_last_wrong_guess(self):
        api.GAME.number_of_available_guess = 1
        actual_result = get_the_guess_result('wrong')
        self.assertEqual(actual_result['status'], 'game over')
        self.assertEqual(actual_result['message'], 'You lost! testing was the secret word')

if __name__ == '__main__':
    unittest.main()