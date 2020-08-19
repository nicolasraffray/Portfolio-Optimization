import unittest
import pandas
import pandas_datareader
from pretend import stub
from unittest import TestCase
from unittest.mock import patch, Mock
from lib.dataCollection import DataCollection


class Test(TestCase):

    pandas_datareader.DataReader = Mock(
        return_value=pandas.DataFrame([450.00, 451.00], columns=['Adj Close']))

    def test_add_data(self):
        data = DataCollection()
        data.get('FB', '20-10-2015', '20-10-2019')
        pandas_datareader.DataReader.called_with(
            'FB', '20-10-2015', '20-10-2019', 'yahoo')
        self.assertEqual(data.dataFrame.columns.values[0], 'FB')
        self.assertEqual(data.dataFrame.iloc[0][0], 450.00)
