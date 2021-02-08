import unittest 
from unittest.mock import patch

import while_loop

class TestGuess(unittest.TestCase):

    @patch('builtins.input', side_effect=['cat'])  # used to provide pretend user input
    @patch('random.choice', return_value='cat')   # force a result from the random choice 
    @patch('builtins.print')   # fake print function, remembers what it was called with 
    def test_play_game_user_guesses_correctly(self, mock_print, mock_random, mock_input):
        while_loop.play_game()
        mock_print.assert_called_with('Correct!')

        # No recursion error. Can test the play_game method. 


if __name__ == '__main__':
    unittest.main()
