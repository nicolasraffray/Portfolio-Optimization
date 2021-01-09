from .metaData import MetaData
import matplotlib.pyplot as plt
import pandas as pd

# consider making methods static and agnostic to data
class Plotting(MetaData):

    def __init__(self, MetaDataClass=None):
        super().__init__()
        if MetaDataClass != None:
            self.dataFrame = MetaDataClass.dataFrame
            self.daily_log_returns = MetaDataClass.daily_log_returns
            self.normal_returns = MetaDataClass.normal_returns

    def prices(self):
        self.dataFrame.plot(figsize=(12, 8))
        plt.show()

    def show_normal_returns(self, normal_returns):
        normal_returns.plot(figsize=(12,8))
        plt.show()

    def log_returns_hist(self):
        if self.daily_log_returns == None:
            self.descriptive_statistics()
        self.daily_log_returns.hist(bins=100, figsize=(14, 7))
        plt.tight_layout()
        plt.show()
    
    def plot_monte_carlo(self, monte_values, optimal_SR_values):
        returns = monte_values["Ra"]
        vol = monte_values["Va"]
        sr = monte_values["Sa"]
        
        plt.figure(figsize = (16,6))
        plt.scatter(vol, returns, c = sr, cmap = 'winter')
        plt.colorbar(label = 'Sharpe Ratio')
        plt.xlabel('Volatility')
        plt.ylabel('Expected Return')


        plt.scatter(optimal_SR_values["MV"],optimal_SR_values["MR"], c='r', edgecolor = 'black')
        plt.show()

