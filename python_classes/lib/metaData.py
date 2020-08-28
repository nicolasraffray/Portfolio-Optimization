import pandas as pd
import numpy as np
from .dataCollection import DataCollection


class MetaData(DataCollection):

    def __init__(self):
        super().__init__()
        self.normal_returns = pd.DataFrame()
        self.daily_log_returns = None
        self.pair_covariance = None

    def get_normal_returns(self):
        if self.normal_returns.empty:
            for stock in self.dataFrame:
                self.normal_returns[stock] = self.dataFrame[stock] / \
                    self.dataFrame.iloc[0][stock]
            self.normal_returns = self.normal_returns.dropna()
        return self.normal_returns

    def get_log_returns(self):
        self.daily_log_returns = np.log(self.dataFrame/self.dataFrame.shift(1)).dropna()
        return self.daily_log_returns
    
    def pairwise_covariance(self):
        if not self.daily_log_returns.empty:
            cov = self.daily_log_returns.cov() * 252
            self.pair_covariance = cov
        else:
            print("there are no Log Returns to perfrom calc")
