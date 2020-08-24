import unittest
import pandas as pd
from unittest.mock import patch, Mock
from unittest import TestCase
from lib.metaData import MetaData
from lib.dataCollection import DataCollection


class Test(TestCase):
  meta = MetaData()
  meta.dataFrame = pd.DataFrame(
        [452.00, 454.00, 456.00], columns=['FB'])

  def test_generates_normal_Returns(self):
      self.meta.get_normal_returns()
      self.assertEqual(round(self.meta.normal_returns.iloc[1][0],5), 1.00442)

  def test_generates_log_returns(self):
    self.meta.get_log_returns()
    self.assertEqual(round(self.meta.daily_log_returns.iloc[1][0],5),0.00442)



      
if __name__ == "__main__":
  unittest.main()