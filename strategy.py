def bollinger_strategy(data, investment_type):
    """
    Strategy based on Bollinger Bands with different risk management.
    - Aggressive: Higher frequency of trades
    - Moderate: Uses SMA confirmation
    - Passive: Less frequent trades
    """
    buy_signals = []
    sell_signals = []
    position = None
    
    for i in range(len(data)):
        close = data['Close'][i]
        upper_band = data['Bollinger_Upper'][i]
        lower_band = data['Bollinger_Lower'][i]
        sma_50 = data['SMA_50'][i]

        if investment_type == 'aggressive':
            if close < lower_band and position != 'buy':
                buy_signals.append(i)
                position = 'buy'
            elif close > upper_band and position != 'sell':
                sell_signals.append(i)
                position = 'sell'

        elif investment_type == 'moderate':
            if close < lower_band and close > sma_50 and position != 'buy':
                buy_signals.append(i)
                position = 'buy'
            elif close > upper_band and close < sma_50 and position != 'sell':
                sell_signals.append(i)
                position = 'sell'

        elif investment_type == 'passive':
            if close < lower_band and position != 'buy':
                buy_signals.append(i)
                position = 'buy'
            elif close > upper_band and position != 'sell':
                sell_signals.append(i)
                position = 'sell'

    return buy_signals, sell_signals