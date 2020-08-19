import unittest
from unittest.mock import patch
from unittest import TestCase
from lib.display import Display


class Test(TestCase):

    @patch('builtins.input', side_effect=['GooG', 'FB', ''])
    def test_get_tickers(self, mock_input):
        display = Display()
        display.ask_for_tickers()
        self.assertEqual(display.tickers, ['GOOG', "FB"])


if __name__ == '__main__':
    unittest.main()
