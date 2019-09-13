import unittest
from hangman_game import HangmanGame
from unittest.mock import patch

class TestHangmanGame(unittest.TestCase):
    def setUp(self):
        with patch('hangman_game.get_random_word', return_value='testing'):
            self.test_game = HangmanGame()

    def test_get_secret_word(self):
        self.assertEqual(self.test_game.get_secret_word(), 'testing')

    def test_get_latest_result_after_initialized(self):
        actual_result = self.test_game.get_latest_result()
        self.assertEqual(actual_result['latest_word_result'], '_ _ _ _ _ _ _')
        self.assertEqual(actual_result['number_of_available_guess'], 9)

    def test_update_state_with_a_char_exist_in_secret_word(self):
        self.test_game.update_state('t')
        actual_result = self.test_game.get_latest_result()
        self.assertEqual(actual_result['latest_word_result'], 't _ _ t _ _ _')
        self.assertEqual(actual_result['number_of_available_guess'], 9)

    def test_update_state_with_a_char_does_not_exist_in_secret_word(self):
        self.test_game.update_state('p')
        actual_result = self.test_game.get_latest_result()
        self.assertEqual(actual_result['latest_word_result'], '_ _ _ _ _ _ _')
        self.assertEqual(actual_result['number_of_available_guess'], 8)

    def test_update_state_with_a_wrong_word(self):
        self.test_game.update_state('testers')
        actual_result = self.test_game.get_latest_result()
        self.assertEqual(actual_result['latest_word_result'], '_ _ _ _ _ _ _')
        self.assertEqual(actual_result['number_of_available_guess'], 8)

    def test_update_state_with_a_correct_word(self):
        self.test_game.update_state('testing')
        actual_result = self.test_game.get_latest_result()
        self.assertEqual(actual_result['latest_word_result'], 't e s t i n g')
        self.assertEqual(actual_result['number_of_available_guess'], 9)

    def test_is_the_word_completed_return_false(self):
        self.assertFalse(self.test_game.is_the_word_completed())

    def test_is_the_word_completed_return_true(self):
        self.test_game.latest_result = 't e s t i n g'
        self.assertTrue(self.test_game.is_the_word_completed())


if __name__ == '__main__':
    unittest.main()