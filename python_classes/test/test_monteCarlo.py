import unittest
import pytest
import random
import pandas as pd 
import numpy as np
from unittest import TestCase
from unittest.mock import Mock
from lib.monteCarlo import MonteCarlo


class Test(TestCase):

  def test_monteCarloSim(self):
    np.random.seed(1)
    data = pd.DataFrame(list(zip([4, 3, 9, 10, 8], 
                                 [10, 25, 36, 30, 33], 
                                 [100, 101, 98, 102, 110]
                        )), columns=['s1', 's2', 's3'])

    metaData = Mock()
    metaData.daily_log_returns = np.log(data/data.shift(1)).dropna()
    monte = MonteCarlo(metaData)
    result = monte.run_simulation(10)

    assert round(monte.monte_values['Ra'][0], 2) == 63.64
    assert round(monte.monte_values['Va'][0], 2) == 5.64
    assert round(monte.monte_values['Sa'][0], 2) == 11.29
    assert len(monte.monte_values['AllWeights']) == 10
    np.testing.assert_allclose(
      monte.optimal_weights,
      np.array([0.035928, 0.156234, 0.807838]),
      rtol = 10**-4
    )
    assert monte.optimal_SR_values == {
      'MR': 18.171065961050374, 
      'MV': 0.8648040545884282, 
      'OS': 9
    }
