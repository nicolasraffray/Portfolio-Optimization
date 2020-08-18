import pandas as pd
import numpy as np
import pandas_datareader as web
import matplotlib.pyplot as plt
from pandas.util.testing import assert_frame_equal
from scipy.optimize import minimize 
# %matplotlib inline

# Make into loop? You want to load n stocks
def load_data(start_date, end_date, ticker1, ticker2, ticker3, ticker4, ticker5):
  # returns the price data of different stocks
  start = start_date
  end = end_date 

  stock1 = web.DataReader(ticker1, start = start, end = end, data_source = 'yahoo')
  stock2 = web.DataReader(ticker2, start = start, end = end,data_source = 'yahoo')
  stock3 = web.DataReader(ticker3 , start = start, end = end,data_source = 'yahoo')
  stock4 = web.DataReader(ticker4, start = start, end = end,data_source = 'yahoo')
  stock5 = web.DataReader(ticker5, start = start, end = end,data_source = 'yahoo')

  stocks = pd.concat([stock1['Adj Close'], 
                      stock2['Adj Close'], 
                      stock3['Adj Close'],
                      stock4['Adj Close'], 
                      stock5['Adj Close']], 
                      axis = 1)

  stocks.columns = [ticker1, ticker2, ticker3, ticker4, ticker5]
  return stocks

def average_daily_return(stocks):
  average_daily_return = stocks.pct_change(1).mean()
  print("Average Daily Return: ", average_daily_return)
  return average_daily_return


def correlation_matrix(stocks):
  correl = stocks.pct_change(1).corr()
  print("Correlation Matrix: \n", correl)
  return stocks.pct_change(1).corr()

def log_returns(stocks):
  log_ret = np.log(stocks/stocks.shift(1))
  return log_ret

def normal_returns(stocks):
    normal_returns = pd.DataFrame()
    for stock in stocks:
      normal_returns[stock] = stocks[stock] / stocks.iloc[0][stock]
    return normal_returns
      

def plot_hist_returns(log_ret):
  log_ret.hist(bins = 100, figsize = (14,7))
  plt.tight_layout()
  plt.show()

def pairwise_covariance(log_ret):
  pairwise_covariance = log_ret.cov() * 252
  return pairwise_covariance


def monte_carlo(stocks, num_ports):
  ''' Returns optimal Sharpe Ratio, the returns and vol
  associated with it.  '''

  np.random.seed(100)

  log_ret = log_returns(stocks)

  all_weights = np.zeros((num_ports, len(stocks.columns)))
  return_array = np.zeros(num_ports)
  volatility_array = np.zeros(num_ports)
  sharpe_array = np.zeros(num_ports)

  for index in range(num_ports):

    # Create Random Weights
    weights = np.random.random(5)

    # Standardise weights to make sure they sum to 1
    weights = weights/np.sum(weights)

    # Save weights
    all_weights[index,:] = weights

    # Expected Returns
    return_array[index] = np.sum((log_ret.mean()*weights)*252)

    # Expected Volatility
    volatility_array[index] = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov()*252,weights)))

    # Sharpe Ratio
    sharpe_array[index] = return_array[index]/volatility_array[index]

    
    print("Simulation is ", "%.2f" % (index/num_ports * 100),"% complete" )

  monte_values = { "Ra": return_array, "Va": volatility_array, "Sa": sharpe_array, "AllWeights": all_weights }
  return monte_values

def get_optimal_weights(monte_values):
  print('Shapre Ratio:',monte_values["Sa"].max(),'\n')
  print('Max SR Location:',monte_values["Sa"].argmax())
  optimal_sharpe = monte_values["Sa"].argmax()

  allw = monte_values["AllWeights"]
  allw[optimal_sharpe,:]

  returns = monte_values["Ra"]
  vol = monte_values["Va"]
  max_sr_ret = returns[optimal_sharpe]
  max_sr_vol = vol[optimal_sharpe]

  optimal_SR_values = {"OS": optimal_sharpe, "MV": max_sr_vol, "MR": max_sr_ret}
  return optimal_SR_values, monte_values['AllWeights'][optimal_sharpe]

def plot_monte_carlo(monte_values, optimal_SR_values):
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

''' Finding Optimal Weights through optimization '''

def get_ret_vol_sr(weights, log_ret): 
  weights = np.array(weights)
  ret = np.sum(log_ret.mean() * weights) * 252
  vol = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov() * 252, weights)))
  sr = ret/vol
  ret_vol_sr = np.array([ret,vol,sr])
  return ret_vol_sr

# Look at documentation for minimization function. 

def neg_sharpe(ret_vol_sr): 
  ret_vol_sr[2] * -1
  return ret_vol_sr

def check_sum(weights):
  return np.sum(weights) -1

def generate_portfolio_timeseries(normal_ret, allocation):
  ''' returns dataframe of returns adjusted for allocation '''
  if len(allocation) != normal_ret.shape[-1]:
      print("Allocation does not match number of stocks")
      return
  pf_returns = normal_ret * allocation
  pf_returns['Total Return'] = pf_returns.sum(axis=1)
  return pf_returns

def plot_portfolio(pf_returns):
  pf_returns['Total Return'].plot(figsize=(10,8))
  plt.show()

def plot_portfolio_breakdown(pf_returns):
  pf_returns.drop('Total Return',axis = 1).plot(figsize=(10,8))
  plt.show()

def plot_against_benchmark(pf_returns, benchmark):
  print(pf_returns)
  pf = pd.DataFrame()
  pf['Benchmark'] = benchmark
  pf['Portfolio'] = pf_returns['Total Return']
  
  pf.plot(figsize=(10,8))
  plt.show()

# cons = ({'type':'eq', 'fun':check_sum})

# # 0-1 bounds for each weight 

# bounds = ((0,1), (0,1), (0,1), (0,1),(0,1)) # Needed to be hardcoded

# init_guess = np.array([0.2,0.2,0.2,0.2,0.2]) # Needed to be hardcoded

# opt_results = minimize(neg_sharpe,init_guess,method='SLSQP',bounds=bounds,constraints=cons)

# print(opt_results)
# print('----------')
# print('Optimal Weights')
# print(opt_results.x)
# vals = get_ret_vol_sr(opt_results.x, log_ret)
# print('Expected Return:')
# print(vals[0])
# print('Expected Volatility')
# print(vals[1])
# print('Sharpe Ratio')
# print(vals[0])


# frontier_y = np.linspace(0,0.25,10)
# print(frontier_y)

# def minimize_volatility(weights):
#     return  get_ret_vol_sr(weights)[1] 

# frontier_volatility = []

# for possible_return in frontier_y:
#     # function for return
#     cons = ({'type':'eq','fun': check_sum},
#             {'type':'eq','fun': lambda w: get_ret_vol_sr(w)[0] - possible_return})
    
#     result = minimize(minimize_volatility,init_guess,method='SLSQP',bounds=bounds,constraints=cons)
    
#     frontier_volatility.append(result['fun'])

# plt.figure(figsize=(12,8))
# plt.scatter(volatility_array,return_array,c=sharpe_array,cmap='plasma')
# plt.colorbar(label='Sharpe Ratio')
# plt.xlabel('Volatility')
# plt.ylabel('Return')


# log_ret = log_ret.dropna()
# # Add frontier line
# plt.plot(frontier_volatility,frontier_y,'g--',linewidth=3)


# # log_ret['Cummulative'] = np.sum(log_ret,1)/np.sum(log_ret,1).iloc[0]

# # spy_etf = web.DataReader('SPY', 'yahoo', start = start, end = end )

# # print(spy_etf)
# # print(log_ret['Cummulative'])

# # (log_ret['Cummulative']).plot(label = 'Cummulative Return') 
# # spy_etf['close'].plot(label = 'SPY')
# plt.show()

start = "04-01-2015"
end = "04-02-2020"
stocks = load_data(start,end, "FB", "AAPL", "AMZN","NFLX","GOOG")
log_ret = log_returns(stocks)
normal_ret = normal_returns(stocks)
spy_etf = web.DataReader('SPY', 'yahoo',start=start,end=end)
spy_etf_returns = normal_returns(spy_etf)['Adj Close']
pf_ret = generate_portfolio_timeseries(normal_ret, [0.2,0.2,0.2,0.2,0.2])
print(spy_etf_returns)
