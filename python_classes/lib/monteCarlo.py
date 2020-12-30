import numpy as np 
import pandas as pd 
from .metaData import MetaData
from scipy.optimize import minimize 
import time
import sys

class MonteCarlo():

  def __init__(self, metaData):
    self.optimal_SR_values = None
    self.monte_values = None
    if metaData.normal_returns.empty or metaData.daily_log_returns.empty:
      metaData.descriptive_statistics()
    self.metaData = metaData

  def run_simulation(self):
    self.simulation(self.metaData.daily_log_returns, 10000)
    self.get_optimal_weights()

  def simulation(self, stocks, num_ports):
    all_weights = np.zeros((num_ports, len(stocks.columns)))
    return_array = np.zeros(num_ports)
    volatility_array = np.zeros(num_ports)
    sharpe_array = np.zeros(num_ports)

    # setup toolbar
    toolbar_width = round(num_ports/1000)

    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1))

    for index in range(num_ports):

      # Create Random Weights
      weights = np.random.random(4)

      # Standardise weights to make sure they sum to 1
      weights = weights/np.sum(weights)

      # Save weights
      all_weights[index,:] = weights

      # Expected Returns
      return_array[index] = np.sum((self.metaData.daily_log_returns.mean()*weights)*252)

      # Expected Volatility
      volatility_array[index] = np.sqrt(np.dot(weights.T, np.dot(self.metaData.daily_log_returns.cov()*252,weights)))

      # Sharpe Ratio
      sharpe_array[index] = return_array[index]/volatility_array[index]

      if (index % 1000) == 0:
        sys.stdout.write("-")
        sys.stdout.flush()
    sys.stdout.write("]\n") # this ends the progress bar


    self.monte_values = { "Ra": return_array, "Va": volatility_array, "Sa": sharpe_array, "AllWeights": all_weights }
    return self.monte_values

  def get_optimal_weights(self):
    if self.monte_values == None:
      print('Monte Carlo Simulation Must be run')
      return 
      
    print('Shapre Ratio:',self.monte_values["Sa"].max(),'\n')
    print('Max SR Location:',self.monte_values["Sa"].argmax())
    optimal_sharpe = self.monte_values["Sa"].argmax()

    allw = self.monte_values["AllWeights"]
    allw[optimal_sharpe,:]

    returns = self.monte_values["Ra"]
    vol = self.monte_values["Va"]
    max_sr_ret = returns[optimal_sharpe]
    max_sr_vol = vol[optimal_sharpe]

    self.optimal_SR_values = {"OS": optimal_sharpe, "MV": max_sr_vol, "MR": max_sr_ret}
    return self.optimal_SR_values, self.monte_values['AllWeights'][optimal_sharpe]


