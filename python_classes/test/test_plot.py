import unittest
import pandas as pd
import matplotlib.pyplot as plt
from unittest.mock import patch, Mock
from unittest import TestCase
from lib.plotting import Plotting


class Test(TestCase):
    def test_plot_prices(self):
        with patch('lib.metaData.MetaData') as MockClass:
            MockClass.dataFrame.plot.return_value = True

        plot = Plotting(MockClass)

        with patch('matplotlib.pyplot.plot') as patched_plot, \
                patch('matplotlib.pyplot.show') as patched_show:
            patched_show.return_value = True

            result = plot.prices()
            self.assertTrue(patched_show.called)
            self.assertTrue(MockClass.dataFrame.plot.called)
