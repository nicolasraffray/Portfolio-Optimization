import unittest
import pandas as pd
from unittest.mock import patch, Mock
from unittest import TestCase
from lib.metaData import MetaData
from lib.dataCollection import DataCollection


class Test(TestCase):
    meta = MetaData()
    meta.dataFrame = pd.DataFrame(list(zip([4, 3, 9, 10, 8], [10, 25, 36, 30, 33], [
        100, 101, 98, 102, 110])), columns=['s1', 's2', 's3'])

    def test_generates_normal_Returns(self):
        self.meta.get_normal_returns()
        self.assertEqual(
            round(self.meta.normal_returns.iloc[1][0], 5), 0.75)

    def test_generates_log_returns(self):
        self.meta.get_log_returns()
        self.assertEqual(
            round(self.meta.daily_log_returns.iloc[1][0], 5), 1.09861)

    def test_generates_pairwise_covariance(self):
        self.meta.get_log_returns()
        self.meta.pairwise_covariance()
        self.assertEqual(
            round(self.meta.pair_covariance.iloc[0][1], 3), -9.271)

    def test_average_daily_return(self):
        result = self.meta.average_daily_returns()
        self.assertEqual(round(result.iloc[0], 5), 0.41528)

    def test_correlation_matrix(self):
        dataFrame = pd.DataFrame(list(zip([4, 3, 9, 10, 8], [10, 25, 36, 30, 33], [
                                 100, 101, 98, 102, 110])), columns=['s1', 's2', 's3'])
        result = self.meta.correlation_matrix()
        self.assertEqual(round(result.iloc[1][0], 5), -0.13289)

    def test_generate_portfolio_timeseries(self):
        self.meta.get_normal_returns()
        self.meta.generate_portfolio_timeseries([0.33, 0.33, 0.33])
        self.assertEqual(
            round(self.meta.dataFrame['Total Return'].iloc[1], 4), 1.4058)


if __name__ == "__main__":
    unittest.main()
