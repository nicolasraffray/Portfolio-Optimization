import unittest
import pandas as pd
from unittest.mock import patch, Mock
from unittest import TestCase
from lib.metaData import MetaData
from lib.dataCollection import DataCollection


class Test(TestCase):

    def test_generates_normal_Returns(self):
        meta = MetaData()
        meta.dataFrame = pd.DataFrame(
            [452.00, 454.00, 456.00], columns=['FB'])
        meta.generate_normal_returns()
        print(meta.normal_returns)
        self.assertEqual(round(meta.normal_returns.iloc[1][0],5), 1.00442)
