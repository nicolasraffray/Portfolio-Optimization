# Portfolio Optimization

Currently working on making a more intuitive CLI but see below for how to get a plot of monte carlo simulation

## How to Run

Scroll to the bottom of the Efficient_Frontier.py file
and imput the stock tickers and the dates for which you
would like to optimize over. Example stocks used are Facebook, Apple, Amazon, Netflix, Google. From 04-01-2015 to 04-02-2020.

Note the longer the time period the longer the optimization will take.

Then save and openup the terminal and type

```
python -i Efficient_Frontier.py
# Look at stocks
stocks
# Look at log returns
log_ret
```

#

Methods:

average_daily_return(stocks): Returns Average Daily returns

correlation_matrix(stocks): Returns a correlation matrix of stocks

log_returns(stocks): Returns Log Returns of selected stocks

#

Run a monte carlo simulation for optimal weights:

```python
# 10000 is the number of portfolios you want to generate
mc = monte_carlo(stocks,10000)

opt_weights = get_optimal_weights(mc)
print(opt_weights)
# OS: Optimal (opt) Sharpe Ratio, MV: Max vol of opt Sharpe Ratio, MR: Max return of opt sharpe ratio

plot_monte_carlo(mc,opt_weights)

```

### Visualize:

#

#### plot_hist_returns(log_ret)

![log_ret](./images/log_ret_hist.png)

#

#### plot_monte_carlo(mc,opt_weights)

Red dot represents the portfolio with the highest sharpe ratio.

![monte](./images/monte_carlo.png)
