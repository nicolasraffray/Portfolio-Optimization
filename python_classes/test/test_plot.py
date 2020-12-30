import unittest
import pytest
import pandas as pd
import numpy as np
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

    def test_show_normal_returns(self):
        metaData = Mock()        
        with patch('lib.metaData.MetaData') as MockClass:
            MockClass.normal_returns.return_value = pd.DataFrame([1,2,3], columns=["numbers"])
            plot = Plotting(MockClass)
        
        plot = Plotting(MockClass)
        with patch('matplotlib.pyplot.plot') as patched_plot, \
            patch('matplotlib.pyplot.show') as patched_show:
                patched_show.return_value = True
                patched_plot.return_value = True

                plot.show_normal_returns()
                self.assertTrue(plot.normal_returns.plot.called)
                self.assertTrue(patched_show.called)

    def test_plot_monte_carl(self):
        plot = Plotting(Mock())
        mockedMonte = Mock()
        monte_values = {
            'Ra': np.array([63.64]),
            'Va': np.array([5.64]),
            'Sa': np.array([11.29]),
            'AllWeights': np.array(
                [
                    [3.66625362e-01, 6.33274085e-01, 1.00552749e-04],
                    [5.58399452e-01, 2.71053854e-01, 1.70546694e-01],
                    [2.00584251e-01, 3.72135515e-01, 4.27280234e-01]
                ]
            )
        }

        optimal_SR_values = {
            'MR': 18.171065961050374, 
            'MV': 0.8648040545884282, 
            'OS': 9
        }

        with patch('matplotlib.pyplot.scatter') as patched_scatter, \
            patch('matplotlib.pyplot.show') as patched_show, \
                patch('matplotlib.pyplot.colorbar') as patched_colorbar:
                    patched_show.return_value = True 
                    patched_scatter.return_value = True
                    patched_colorbar.return_value = True
                    

                    plot.plot_monte_carlo(monte_values, optimal_SR_values)

                    self.assertTrue(patched_colorbar.called)
                    self.assertTrue(patched_show.called)
                    patched_scatter.asset_call_with(np.array([5.64]))
                    patched_scatter.asset_call_with(np.array([63.64]))
                    patched_scatter.asset_call_with(18.171065961050374)
                    patched_scatter.asset_call_with(0.8648040545884282)



        

