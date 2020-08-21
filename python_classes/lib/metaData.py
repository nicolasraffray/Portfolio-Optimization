import pandas as pd
from lib.dataCollection import DataCollection


class MetaData(DataCollection):

    def __init__(self):
        super().__init__()
        self.normal_returns = pd.DataFrame()

    def generate_normal_returns(self):
        for stock in self.dataFrame:
            self.normal_returns[stock] = self.dataFrame[stock] / self.dataFrame.iloc[0][stock]
        self.normal_returns = self.normal_returns.dropna()
        return self.normal_returns
