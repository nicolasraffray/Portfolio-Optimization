import pandas as pd
from pandas.testing import assert_frame_equal
import pandas_datareader as web


class DataCollection():

    dataFrame = pd.DataFrame()

    @classmethod
    def get(cls, ticker, start, end):
        try:
            stock = web.DataReader(ticker, start=start,
                                   end=end, data_source='yahoo')
            if cls.dataFrame.empty:
                cls.dataFrame[ticker] = stock['Adj Close']
            else:
                cls.dataFrame = pd.concat(
                    [cls.dataFrame, stock['Adj Close']], axis=1)
                cls.dataFrame.columns.values[-1] = ticker
        except:
            return "Stock Not Found"
