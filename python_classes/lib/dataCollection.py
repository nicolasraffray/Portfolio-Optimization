import pandas as pd
from pandas.util.testing import assert_frame_equal
import pandas_datareader as web


class DataCollection():

    def __init__(self):
        self.dataFrame = pd.DataFrame()
        pass

    def get(self, ticker, start, end):
        try:
            stock = web.DataReader(ticker, start=start,
                                   end=end, data_source='yahoo')
            if self.dataFrame.empty:
                self.dataFrame[ticker] = stock['Adj Close']
            else:
                self.dataFrame = pd.concat(
                    [self.dataFrame, stock['Adj Close']], axis=1)
                self.dataFrame.columns.values[-1] = ticker
        except:
            return "Stock Not Found"
