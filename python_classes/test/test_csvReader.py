import pytest
import unittest
from unittest import mock
from lib.readCSV import ReadCSV


class Test(unittest.TestCase):

  def test_readCSV(self):
    open_name = '%s.open' % __name__

    with mock.patch("builtins.open", create=True) as mock_open,\
          mock.patch('csv.reader') as patched_csv:
            patched_csv.return_value = ['FB']
            ReadCSV.get_tickers('../tickers/tickers.csv')
            mock_open.assert_called_with('../tickers/tickers.csv', newline='')
