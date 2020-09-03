import unittest
from unittest.mock import patch
from unittest import TestCase
from lib.display import Display


class Test(TestCase):
    display = Display()

    @patch('builtins.input', side_effect=['GooG', 'FB', 'Finish'])
    def test_get_tickers(self, mock_inputs):
        self.display.ask_for_tickers()
        self.assertEqual(self.display.tickers, ['GOOG', "FB"])

    @patch('builtins.input', side_effect=['1'])
    def test_give_menu_of_options(self, mock_inputs):
        result = self.display.give_menu_of_options()
        self.assertEqual(result, '1')


if __name__ == '__main__':
    unittest.main()
