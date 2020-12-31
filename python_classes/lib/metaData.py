#!/usr/bin/env python3
import pandas as pd
import numpy as np
from .dataCollection import DataCollection

class MetaData():

    def __init__(self, dataFrame=None):
        self.normal_returns = pd.DataFrame()
        self.daily_log_returns = None
        self.pair_covariance = None
        self.correl_matrix = None
        self._initialize_dataFrame(dataFrame)

    def descriptive_statistics(self):
        self.get_normal_returns()
        self.get_log_returns()
        av_ret = self.average_daily_returns()

        if len(self.dataFrame.columns) >= 2:
            self.pairwise_covariance()
            self.correlation_matrix()
        else:
            print('You Need More than Stocks for Covariance and Correlation')

        return av_ret, self.pair_covariance, self.correl_matrix

    def get_normal_returns(self):
        for stock in self.dataFrame:
            self.normal_returns[stock] = self.dataFrame[stock] / \
                self.dataFrame.iloc[0][stock]
        self.normal_returns = self.normal_returns.dropna()
        return self.normal_returns

    def get_log_returns(self):
        self.daily_log_returns = np.log(
            self.dataFrame/self.dataFrame.shift(1)).dropna()
        return self.daily_log_returns

    def pairwise_covariance(self):

        if not self.daily_log_returns.empty:
            cov = self.daily_log_returns.cov() * 252
            self.pair_covariance = cov
        else:
            print("there are no Log Returns to perfrom calc")

    def average_daily_returns(self):
        average_daily_return = self.dataFrame.pct_change(1).mean()
        return average_daily_return

    def correlation_matrix(self):
        self.correl_matrix = self.dataFrame.pct_change(1).dropna().corr()
        return  self.correl_matrix

    def generate_portfolio_timeseries(self, allocation):
        pf_returns = self.normal_returns * allocation
        self.dataFrame['Total Return'] = pf_returns.sum(axis=1)

    def re_initialize_data(self, data=None):
        if data == None:
            self.dataFrame = DataCollection.dataFrame
        else:
            self.dataFrame = data

    def _initialize_dataFrame(self, dataFrame):
        if dataFrame == None or dataFrame.empty:
            self.dataFrame = DataCollection.dataFrame
        else:
            self.dataFrame = dataFrame
    

