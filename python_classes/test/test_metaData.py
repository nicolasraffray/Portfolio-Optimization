import unittest
import pandas as pd
from unittest.mock import patch, Mock
from unittest import TestCase
from lib.metaData import MetaData
from lib.dataCollection import DataCollection


class Test(TestCase):
  meta = MetaData()
  meta.dataFrame = pd.DataFrame(list(zip([452.00, 454.00, 456.00],[35,36,40])), columns=['FB','AB'])

  def test_generates_normal_Returns(self):
      self.meta.get_normal_returns()
      self.assertEqual(round(self.meta.normal_returns.iloc[1][0],5), 1.00442)

  def test_generates_log_returns(self):
    self.meta.get_log_returns()
    self.assertEqual(round(self.meta.daily_log_returns.iloc[1][0],5),0.0044)

  def test_generates_pairwise_covariance(self):
    self.meta.get_log_returns()
    self.meta.pairwise_covariance()
    dataFrame = pd.DataFrame(list(zip([4.745430e-08,-1.887479e-04],[-0.000189,0.750738])), columns=['FB','AB'],index=['FB','AB'])
    self.assertEqual(round(self.meta.pair_covariance.iloc[0][0],3), round(dataFrame.iloc[0][0],5) )





      
if __name__ == "__main__":
  unittest.main()