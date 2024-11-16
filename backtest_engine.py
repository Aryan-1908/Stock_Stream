import numpy as np

def backtest(data, buy_signals, sell_signals, initial_capital):
    capital = initial_capital
    position = None
    returns = []
    
    for i in range(len(data)):
        close = data['Close'][i]

        if i in buy_signals and position != 'buy':
            position = 'buy'
            entry_price = close

        elif i in sell_signals and position == 'buy':
            position = 'sell'
            profit = (close - entry_price) / entry_price
            returns.append(profit)
            capital *= (1 + profit)

    hodl_return = (data['Close'][-1] - data['Close'][0]) / data['Close'][0]
    
    return capital, np.mean(returns), hodl_return
