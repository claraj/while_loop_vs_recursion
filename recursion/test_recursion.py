import unittest 
from unittest.mock import patch

import recursion

class TestGuess(unittest.TestCase):

    @patch('builtins.input', return_value='cat')  # used to provide pretend user input
    def test_play_game(self, mock_input):

        # This test fails with a 
        #   RecursionError: maximum recursion depth exceeded while calling a Python object 
        # So there's no opportunity to start asserting anything or checking the code's behavior
        
        recursion.play_game()


if __name__ == '__main__':
    unittest.main()
