import unittest
import pytest
import pandas
import pandas_datareader
from unittest import TestCase
from unittest.mock import patch, Mock
from lib.dataCollection import DataCollection


class Test(TestCase):

    pandas_datareader.DataReader = Mock(
        return_value=pandas.DataFrame(
            [450.00, 451.00], 
            columns=['Adj Close']
        )
    )
    def test_add_data(self):
        DataCollection.get('FB', '20-10-2015', '20-10-2019')
        pandas_datareader.DataReader.called_with(
            'FB', '20-10-2015', '20-10-2019', 'yahoo')
        print(DataCollection.dataFrame)
        self.assertEqual(DataCollection.dataFrame.columns.values[0], 'FB')
        self.assertEqual(DataCollection.dataFrame.iloc[0][0], 450.00)

