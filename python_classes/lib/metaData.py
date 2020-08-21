import pandas as pd
import numpy as np
from lib.dataCollection import DataCollection



class MetaData(DataCollection):

    def __init__(self):
        super().__init__()
        self.normal_returns = pd.DataFrame()
        self.daily_log_returns = None

    def get_normal_returns(self):
        for stock in self.dataFrame:
            self.normal_returns[stock] = self.dataFrame[stock] / self.dataFrame.iloc[0][stock]
        self.normal_returns = self.normal_returns.dropna()
        return self.normal_returns

    def get_log_returns(self):
      self.daily_log_returns = np.log(self.dataFrame/self.dataFrame.shift(1))
      return self.daily_log_returns

