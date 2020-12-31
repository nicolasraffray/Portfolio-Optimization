import unittest
import pytest
from unittest.mock import patch
from unittest import TestCase
from lib.display import Display


class Test(TestCase):
    display = Display()

    @patch('builtins.input', side_effect=['GooG', 'FB', ''])
    def test_get_tickers(self, mock_inputs):
        self.display.ask_for_tickers()
        self.assertEqual(self.display.tickers, ['GOOG', "FB"])

    # TODO: Make a first question test
    # @patch('builtins.input', side_effect=['fake', ''])
    # @patch('builtins.print')
    # def test_give_menu_of_options(self,mock_input, mock_print):
    #     self.display.give_menu_of_options().next().next()
    #     print(mock_print)
    #     assert 1 == 2 
    #     # mock_print.assert_called_with('Choose from the following\n\
    #     #         1) Show Tickers\n\
    #     #         2) Portfolio Descriptive Statistics\n\
    #     #         3) Run Monte Carlo Simulation\n\n')

