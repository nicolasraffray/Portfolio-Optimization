import unittest
import pytest
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
    @patch('builtins.input')
    def test_give_menu_of_options(self, mock_inputs, mock_print):
        result = self.display.give_menu_of_options()
        print(mock_print)
        mock_print.assert_called_with('Choose from the following\n\
                1) Show Tickers\n\
                2) Get Tickers\n\
                3) Portfolio Descriptive Statistics\n\
                4) Run Monte Carlo Simulation\n\n')




if __name__ == '__main__':
    unittest.main()
