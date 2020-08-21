import unittest
from unittest.mock import patch
from unittest import TestCase
from lib.display import Display


class Test(TestCase):

    @patch('builtins.input', side_effect=['GooG', 'FB', 'Finish'])
    def test_get_tickers(self, mock_inputs):
        display = Display()
        display.ask_for_tickers()
        self.assertEqual(display.tickers, ['GOOG', "FB"])


if __name__ == '__main__':
    unittest.main()
