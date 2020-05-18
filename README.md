# CAPM

Currently working on making a more intuitive CLI but see below for how to get a plot of monte carlo simulation

## How to Run

Scroll to the bottom of the Efficient_Frontier.py file
and imput the stock tickers and the dates for which you
would like to optimize over.

Note the longer the time period the longer the optimization will take.

Then save and openup the terminal and type

```
python -i Efficient_Frontier.py
```

You can look at the logarithmic returns by typing 'log_ret' in the terminal or 'stocks' to see the stock prices.

```python
# 1000 is the number of portfolios you want to generate
mc = monte_carlo(stocks,1000)

opt_weights = get_optimal_weights(mc)
plot_monte_carlo(mc,opt_weights)

```
