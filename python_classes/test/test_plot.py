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

            plot.prices()
            self.assertTrue(patched_show.called)
            self.assertTrue(MockClass.dataFrame.plot.called)

    def test_log_returns(self):
        with patch('lib.metaData.MetaData') as MockClass:
            MockClass.log_returns.return_value = True

        plot = Plotting(MockClass)
        with patch('matplotlib.pyplot.hist') as patched_hist, \
                patch('matplotlib.pyplot.show') as patched_show, \
        patch('matplotlib.pyplot.tight_layout') as patched_tight_layout:
            patched_show.return_value = True
            patched_hist.return_value = True
            patched_tight_layout.return_value = True

            plot.log_returns_hist()
            self.assertTrue(plot.log_returns.hist.called)
            self.assertTrue(patched_tight_layout.called)
            self.assertTrue(patched_show.called)
