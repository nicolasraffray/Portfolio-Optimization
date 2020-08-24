from .metaData import MetaData
import matplotlib.pyplot as plt


class Plotting(MetaData):

    def __init__(self):
        super().__init__()

    def prices(self):
        self.dataFrame.plot(figsize=(12, 8))
        plt.show()

    def log_returns(self):
        self.log_returns.hist(bins=100, figsize=(14, 7))
        plt.tight_layout()
        plt.show()
