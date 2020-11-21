from .metaData import MetaData
import matplotlib.pyplot as plt
import pandas as pd


class Plotting(MetaData):

    def __init__(self, MetaDataClass=None):
        super().__init__()
        # if MetaDataClass != None:
        #     self.dataFrame = MetaDataClass.dataFrame
        #     self.log_returns = MetaDataClass.log_returns
        #     self.normal_returns = MetaDataClass.normal_returns

    def prices(self):
        self.dataFrame.plot(figsize=(12, 8))
        plt.show()

    def show_normal_returns(self):
        self.normal_returns.plot(figsize=(12,8))
        plt.show()


    def log_returns_hist(self):
        self.log_returns.hist(bins=100, figsize=(14, 7))
        plt.tight_layout()
        plt.show()
