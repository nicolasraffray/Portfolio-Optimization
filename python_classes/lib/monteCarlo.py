import numpy as np 
import pandas as pd 
from .metaData import MetaData
from scipy.optimize import minimize 
import time
import sys




class MonteCarlo(MetaData):

  def __init__(self):
    super().__init__()
    self.optimal_SR_values = None
    self.monte_values = None
    if self.normal_returns.empty:
      self.get_log_returns()
    
  def run_simulation(self, stocks, num_ports):
    all_weights = np.zeros((num_ports, len(stocks.columns)))
    return_array = np.zeros(num_ports)
    volatility_array = np.zeros(num_ports)
    sharpe_array = np.zeros(num_ports)

    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

    for index in range(num_ports):
      time.sleep(0.1)

      # Create Random Weights
      weights = np.random.random(5)

      # Standardise weights to make sure they sum to 1
      weights = weights/np.sum(weights)

      # Save weights
      all_weights[index,:] = weights

      # Expected Returns
      return_array[index] = np.sum((self.log_returns.mean()*weights)*252)

      # Expected Volatility
      volatility_array[index] = np.sqrt(np.dot(weights.T, np.dot(self.log_returns.cov()*252,weights)))

      # Sharpe Ratio
      sharpe_array[index] = return_array[index]/volatility_array[index]

      
      sys.stdout.write("-")
      sys.stdout.flush()
    sys.stdout.write("]\n") # this ends the progress bar


    self.monte_values = { "Ra": return_array, "Va": volatility_array, "Sa": sharpe_array, "AllWeights": all_weights }
    return monte_values

  def get_optimal_weights(self):
    if self.monte_values == None:
      self.get_optimal_weights()
      
    print('Shapre Ratio:',monte_values["Sa"].max(),'\n')
    print('Max SR Location:',monte_values["Sa"].argmax())
    optimal_sharpe = self.monte_values["Sa"].argmax()

    allw = self.monte_values["AllWeights"]
    allw[optimal_sharpe,:]

    returns = monte_values["Ra"]
    vol = monte_values["Va"]
    max_sr_ret = returns[optimal_sharpe]
    max_sr_vol = vol[optimal_sharpe]

    self.optimal_SR_values = {"OS": optimal_sharpe, "MV": max_sr_vol, "MR": max_sr_ret}
    return optimal_SR_values, monte_values['AllWeights'][optimal_sharpe]


